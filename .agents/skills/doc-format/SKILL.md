---
name: doc-format
description: Formats documents according to predefined templates (survey, formal report, simple report) and converts documents between formats (Markdown, LaTeX, DOCX, HTML, PDF, plain text) without losing content. Use whenever the user asks to format, reformat, structure, "format as survey/report", convert, convert to LaTeX, convert to Markdown, export to Word/PDF/HTML, or adapt a document to another format, even without explicitly using the word "format". Preserves all content (text, equations, tables, figures, citations, references) and validates the conversion.
---

# Doc Format

This skill combines two complementary functions: **applying a format template** (survey, formal report, simple report) and **converting between file formats** (md, LaTeX, docx, html, pdf, txt). The central rule is that **formatting and converting must never lose or alter content**: they change the form, not what is said. This is why a verification step is performed at the end.

## Choosing What to Do

Identify the user request:

| Request | Action |
|---------|--------|
| "Format this as a survey / report" | Apply template (steps A) |
| "Convert to LaTeX / md / docx..." | Convert (steps B) |
| "Turn this into a formal report in LaTeX" | A and then B |

If the template type is not specified, ask once (survey, formal report, or simple report) or, if the content makes it obvious, infer and state which was chosen. If the output format is not specified, use Markdown as default and state so.

## A. Applying a Template

The three templates are located in `references/formats.md`. Read that file, select the template, and follow these steps:

1. **Read the entire document** and inventory the content: sections, equations, tables, figures, lists, citations, references, footnotes, links, and code blocks.
2. **Map the content to the template sections.** Each existing content block goes into its corresponding section.
3. **Content without a matching place in the template**: do not delete it. Place it in the closest section, or create a subsection, and inform the user.
4. **Template sections without content**: do not fabricate text. Leave the section with a placeholder `[MISSING: description of what should be included]` and list these gaps at the end of the response. Inventing content in a research document is worse than leaving a visible gap.
5. **Do not rewrite the author's text** unless requested. Only formatting may be corrected (headings, lists, numbering, captions). If there are content errors, mention them separately (for quality analysis, use the `doc-review` skill).
6. Deliver the document and a brief summary: what was moved, what is missing.

## B. Converting Between Formats

Detailed instructions and commands are in `references/conversion.md`. Summary:

1. **Use pandoc** for structured text conversions (md, tex, docx, html, rst). Check if installed (`which pandoc`); if not, attempt installation.
2. **Convert via script**: `scripts/convert.sh <input> <output>` selects the conversion based on file type and applies flags that preserve equations, citations, and tables.
3. **Always validate** with `python scripts/verify_conversion.py <input> <output>`: compares word counts, sections, tables, figures, equations, links, and references between source and destination, flagging differences. Correct any real loss; explain expected differences to the user (e.g., automated numbering).
4. **For PDF** as destination: use the pdf skill, or LaTeX/pandoc with a PDF engine. PDF is an output format, not an editable format; warn if the user wants to convert backwards from a PDF (reverse conversion loses structure).
5. **For docx** as destination or source, consult the docx skill.

## Where Loss Risks Occur

These are common failure points in conversions. Always check:

- **Equations** (LaTeX ↔ md ↔ docx): preserve `$...$` and `$$...$$`; in docx, equations become native objects.
- **Complex tables** (merged cells, wide tables): plain Markdown may lose cell merging; use HTML tables or warn the user.
- **Citations and bibliography**: preserve BibTeX keys (`\cite{key}` ↔ `[@key]`); do not convert to loose text without warning. Keep the `.bib` file.
- **Figures**: preserve image file references, captions, and labels.
- **Cross-references** (`\ref`, `\label`): preserve them.
- **Footnotes, links, code**: confirm they survive.
- **Special characters and accents**: ensure UTF-8 encoding and appropriate font/package support in LaTeX.

## Final Output

Deliver the file and, in a few lines: template/format applied, verification result (no loss / differences found), and what was missing or moved.
