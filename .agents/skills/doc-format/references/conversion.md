# Format Conversion

## Table of Contents
1. Principles
2. Pandoc Commands by Format Pair
3. LaTeX Specifics
4. Verification
5. Common Issues

## 1. Principles

- Convert from the richest format available. If the original `.tex` or `.md` exists, use that rather than a compiled PDF.
- Always keep the original file intact; write the output to a new file.
- Verify the result (Section 4). A conversion that "ran without errors" is not necessarily a lossless conversion.

## 2. Pandoc Commands

Check installation: `which pandoc || pip install pypandoc_binary` (or `apt-get install pandoc`).

| From → To | Base Command |
|-----------|--------------|
| md → tex | `pandoc in.md -f markdown -t latex -s -o out.tex` |
| md → docx | `pandoc in.md -o out.docx` |
| md → html | `pandoc in.md -s --mathjax -o out.html` |
| md → pdf | `pandoc in.md --pdf-engine=xelatex -o out.pdf` |
| tex → md | `pandoc in.tex -f latex -t markdown-smart-fenced_divs-bracketed_spans-native_divs-native_spans-header_attributes-simple_tables-multiline_tables-grid_tables+pipe_tables+tex_math_dollars --wrap=none -o out.md` (`gfm` discards `\cite{}`; this flavour preserves `[@key]`) |
| tex → docx | `pandoc in.tex -o out.docx` |
| docx → md | `pandoc in.docx -t gfm --wrap=none --extract-media=./media -o out.md` |
| docx → tex | `pandoc in.docx -t latex -s --extract-media=./media -o out.tex` |
| html → md | `pandoc in.html -t gfm --wrap=none -o out.md` |
| any → txt | `pandoc in.ext -t plain --wrap=none -o out.txt` |

Useful options:
- `--citeproc --bibliography=refs.bib` to process citations.
- `--number-sections` to number sections.
- `--toc` for table of contents.
- `--wrap=none` to avoid hard line wraps (minimises noisy diffs).
- `--standalone` (`-s`) for complete document in tex/html.
- `--extract-media=DIR` when reading docx, to extract and preserve images.

## 3. LaTeX Specifics

- Language support: use `xelatex`/`lualatex` and `\usepackage{polyglossia}`, or `\usepackage[english]{babel}` with pdflatex.
- Bibliography: prefer BibTeX (`\bibliographystyle{IEEEtran}`) or BibLaTeX (`\usepackage[backend=biber]{biblatex}`) with `\addbibresource{refs.bib}`.
- Wide tables: `\usepackage{longtable,booktabs}`; pandoc uses these automatically.
- If the original document uses custom classes or packages (IEEEtran, acmart, llncs), preserve them rather than replacing with standard article.
- When moving from md to tex in a survey or report template, map `#` → `\section`, `##` → `\subsection`, and maintain consistent `\label`/`\ref`.

## 4. Verification

Always run:

```bash
python scripts/verify_conversion.py SOURCE DESTINATION
```

The script extracts content from both files (md, tex, html, txt; for docx it uses pandoc to extract text) and compares:

- word count (small tolerance, e.g. 3%),
- number of headings/titles,
- number of tables,
- number of images/figures,
- number of equations,
- number of unique links/URLs,
- number of citations/references.

Interpretation:
- Differences in words, sections, equations, or figures: treat as data loss until proven otherwise and investigate.
- Expected differences: LaTeX commands not counting as words, automated numbering, generated document frontmatter.
- The script does not replace a quick manual check: open the output file and inspect risk zones (equations, tables, references).

## 5. Common Issues

| Symptom | Probable Cause | Solution |
|---------|----------------|----------|
| Equations appear as plain text | Markdown missing `$` or extension disabled | Use `-f markdown+tex_math_dollars` |
| Citations turn into `[?]` | Missing `--citeproc`/`.bib` | Pass `--bibliography` or preserve `\cite` in tex |
| Images disappear from docx | Omitted `--extract-media` | Add the `--extract-media=./media` flag |
| Table loses merged cells | Markdown does not support cell spans | Use HTML tables, or maintain in tex/docx |
| Broken character encoding in tex | Encoding mismatch | Ensure UTF-8, use xelatex |
| Table cells vanish (tex → md, `longtable` tables) | Pandoc parsing bug | Always check tables manually; restore missing cells or use HTML tables |
| Citations vanish in tex → md | `gfm` output format discards citations | Use Pandoc's markdown flavour (configured in `convert.sh`) |
| PDF fails to compile | Missing LaTeX package | Install the missing package or simplify preamble |
