#!/usr/bin/env python3
"""List and extract text from every file in a sources folder.

Usage: python inventory.py <sources_folder> [--out .survey_work/text]

Writes one .txt per source into --out and prints a report saying which files
were read, which failed, and how many words each one has. Optional libraries
(pypdf, python-docx) are used if installed; otherwise those formats are
reported as unreadable so the caller can handle them another way.
"""
import argparse, html, re, sys
from html.parser import HTMLParser
from pathlib import Path

TEXT_EXT = {".txt", ".md", ".markdown", ".rst", ".tex", ".csv", ".json", ".bib"}


class _Strip(HTMLParser):
    SKIP = {"script", "style", "nav", "footer", "header", "aside", "noscript"}

    def __init__(self):
        super().__init__()
        self.parts, self.depth = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if not self.depth and data.strip():
            self.parts.append(data.strip())


def read_html(p):
    s = _Strip()
    s.feed(p.read_text(errors="ignore"))
    return html.unescape("\n".join(s.parts))


def read_pdf(p):
    try:
        from pypdf import PdfReader
    except ImportError:
        raise RuntimeError("pypdf not installed")
    pages = []
    for i, page in enumerate(PdfReader(str(p)).pages, 1):
        pages.append(f"[page {i}]\n{page.extract_text() or ''}")
    text = "\n\n".join(pages)
    if len(re.sub(r"\[page \d+\]|\s", "", text)) < 50:
        raise RuntimeError("no extractable text (scanned PDF? needs OCR)")
    return text


def read_docx(p):
    try:
        import docx
    except ImportError:
        raise RuntimeError("python-docx not installed")
    return "\n".join(par.text for par in docx.Document(str(p)).paragraphs)


def extract(p):
    ext = p.suffix.lower()
    if ext in TEXT_EXT:
        return p.read_text(errors="ignore")
    if ext in {".html", ".htm"}:
        return read_html(p)
    if ext == ".pdf":
        return read_pdf(p)
    if ext == ".docx":
        return read_docx(p)
    raise RuntimeError(f"unsupported format {ext}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out", default=".survey_work/text")
    a = ap.parse_args()

    root = Path(a.folder)
    if not root.is_dir():
        sys.exit(f"Folder not found: {root}")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    ok, failed = [], []
    for p in sorted(f for f in root.rglob("*") if f.is_file() and not f.name.startswith(".")):
        rel = p.relative_to(root)
        try:
            text = re.sub(r"\n{3,}", "\n\n", extract(p)).strip()
            dest = out / (str(rel).replace("/", "__") + ".txt")
            dest.write_text(text)
            ok.append((str(rel), len(text.split()), str(dest)))
        except Exception as e:
            failed.append((str(rel), str(e)))

    print(f"Read {len(ok)} file(s), failed {len(failed)}\n")
    for rel, words, dest in ok:
        print(f"OK    {rel}  ({words} words) -> {dest}")
    for rel, err in failed:
        print(f"FAIL  {rel}  ({err})")


if __name__ == "__main__":
    main()
