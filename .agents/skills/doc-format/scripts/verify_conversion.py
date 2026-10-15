#!/usr/bin/env python3
"""Compares two files (source and destination of a conversion) and flags
possible content losses: words, headings, tables, images, equations,
links, and citations.

Usage: python verify_conversion.py SOURCE DESTINATION [--tol 0.03]
Formats: md, tex, html, txt (docx/rst/others via pandoc to text).
"""
import re
import subprocess
import sys
from pathlib import Path


def load_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".md", ".markdown", ".tex", ".latex", ".html", ".htm", ".txt", ".rst"}:
        return path.read_text(encoding="utf-8", errors="replace")
    # docx and others: convert to markdown via pandoc
    try:
        out = subprocess.run(
            ["pandoc", str(path), "-t", "gfm", "--wrap=none"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout
    except Exception as exc:  # noqa: BLE001
        print(f"Warning: could not read {path} ({exc})", file=sys.stderr)
        return ""


def kind(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".tex", ".latex"}:
        return "tex"
    if ext in {".html", ".htm"}:
        return "html"
    if ext in {".md", ".markdown"}:
        return "md"
    if ext == ".txt":
        return "txt"
    return "md"  # docx etc. read as markdown via pandoc


def body(text: str, k: str) -> str:
    """For LaTeX, ignores preamble (everything before \\begin{document})."""
    if k == "tex":
        m = re.search(r"\\begin\{document\}(.*?)(\\end\{document\}|$)", text, flags=re.S)
        if m:
            return m.group(1)
    return text


def strip_markup(text: str, k: str) -> str:
    if k == "tex":
        text = re.sub(r"(?m)^\s*%.*$", "", text)
        text = re.sub(r"\\begin\{(equation|align|gather)\*?\}.*?\\end\{\1\*?\}", " ", text, flags=re.S)
        text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
        text = re.sub(r"\$[^$\n]+\$", " ", text)
        text = re.sub(r"\\\(.+?\\\)|\\\[.+?\\\]", " ", text, flags=re.S)
        text = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\{[^}]*\}|\[[^\]]*\])?", " ", text)
        text = re.sub(r"\\(?:hypertarget)\{[^}]*\}", " ", text)
        text = re.sub(r"\\(?:label|ref|eqref|[a-z]*cite[a-z]*|includegraphics|input|include)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", text)
        text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", text)
        text = re.sub(r"[{}\\]", " ", text)
    elif k == "html":
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S)
        text = re.sub(r"<[^>]+>", " ", text)
    else:
        text = re.sub(r"\[@[^\]]+\]", " ", text)
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
        text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
        text = re.sub(r"\$[^$\n]+\$", " ", text)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"[#*_`>|\-]+", " ", text)
        text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return text


def count_words(text: str, k: str) -> int:
    return len(re.findall(r"\w+", strip_markup(text, k), flags=re.UNICODE))


def count_headings(text: str, k: str) -> int:
    if k == "tex":
        return len(re.findall(r"\\(part|chapter|section|subsection|subsubsection)\*?\{", text))
    if k == "html":
        return len(re.findall(r"<h[1-6][\s>]", text, flags=re.I))
    return len(re.findall(r"(?m)^#{1,6}\s+\S", text))


def count_tables(text: str, k: str) -> int:
    if k == "tex":
        return len(re.findall(r"\\begin\{(tabular|longtable|tabularx)", text))
    if k == "html":
        return len(re.findall(r"<table[\s>]", text, flags=re.I))
    return len(re.findall(r"(?m)^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", text))


def count_images(text: str, k: str) -> int:
    if k == "tex":
        return len(re.findall(r"\\includegraphics", text))
    if k == "html":
        return len(re.findall(r"<img[\s>]", text, flags=re.I))
    return len(re.findall(r"!\[[^\]]*\]\([^)]+\)", text)) + len(re.findall(r"<img[\s>]", text, flags=re.I))


def count_equations(text: str, k: str) -> int:
    n = len(re.findall(r"\\begin\{(equation|align|gather|eqnarray)\*?\}", text))
    n += len(re.findall(r"\$\$.+?\$\$", text, flags=re.S))
    # inline math
    body_text = re.sub(r"\$\$.+?\$\$", " ", text, flags=re.S)
    n += len(re.findall(r"(?<!\\)\$[^$\n]+\$", body_text))
    n += len(re.findall(r"\\\(.+?\\\)", text, flags=re.S))
    n += len(re.findall(r"\\\[.+?\\\]", text, flags=re.S))
    return n


def count_links(text: str, k: str) -> int:
    return len(set(re.findall(r"https?://[^\s)>\]}\"']+", text)))


def count_citations(text: str, k: str) -> int:
    n = len(re.findall(r"\\(?:auto|paren|text|foot|smart|super)?cite[a-z]*\*?(?:\[[^\]]*\])*\{[^}]+\}", text))
    n += len(re.findall(r"\[@[^\]]+\]", text))
    return n


METRICS = [
    ("headings", count_headings),
    ("tables", count_tables),
    ("images", count_images),
    ("equations", count_equations),
    ("unique links", count_links),
    ("citations", count_citations),
]


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Verifies content loss in a document conversion")
    ap.add_argument("source", help="source file path")
    ap.add_argument("destination", help="destination file path")
    ap.add_argument("--tol", type=float, default=0.03, help="word count tolerance (0.03 = 3%%)")
    ns = ap.parse_args()
    args, tol = [ns.source, ns.destination], ns.tol

    src, dst = Path(args[0]), Path(args[1])
    k_src, k_dst = kind(src), kind(dst)
    t_src, t_dst = body(load_text(src), k_src), body(load_text(dst), k_dst)

    problems = 0
    print(f"Source:      {src}  ({k_src})")
    print(f"Destination: {dst}  ({k_dst})\n")
    print(f"{'metric':<16}{'source':>8}{'destination':>12}   status")

    w_src, w_dst = count_words(t_src, k_src), count_words(t_dst, k_dst)
    diff = abs(w_src - w_dst) / max(w_src, 1)
    status = "ok" if diff <= tol else f"WARNING ({diff:.1%})"
    if diff > tol:
        problems += 1
    print(f"{'words':<16}{w_src:>8}{w_dst:>12}   {status}")

    for name, fn in METRICS:
        a, b = fn(t_src, k_src), fn(t_dst, k_dst)
        if a == b:
            status = "ok"
        else:
            status = "DIFFERENT"
            problems += 1
        print(f"{name:<16}{a:>8}{b:>12}   {status}")

    print()
    if problems:
        print(f"{problems} metric(s) with differences. Review manually: these may be "
              "actual losses or expected differences (formatting commands, automated numbering).")
        return 1
    print("No differences detected across verified metrics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
