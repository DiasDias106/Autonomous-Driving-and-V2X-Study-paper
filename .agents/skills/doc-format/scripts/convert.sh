#!/usr/bin/env bash
# Converts a document between formats using pandoc, with options that protect
# equations, citations, tables, and images.
# Usage: convert.sh <input> <output> [bibliography.bib]
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <input> <output> [bibliography.bib]" >&2
  exit 1
fi

IN="$1"
OUT="$2"
BIB="${3:-}"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found. Install with: pip install pypandoc_binary (or apt-get install pandoc)" >&2
  exit 2
fi

in_ext="${IN##*.}"; in_ext="$(echo "$in_ext" | tr 'A-Z' 'a-z')"
out_ext="${OUT##*.}"; out_ext="$(echo "$out_ext" | tr 'A-Z' 'a-z')"

case "$in_ext" in
  md|markdown) FROM="markdown+tex_math_dollars+pipe_tables+footnotes" ;;
  tex|latex)   FROM="latex" ;;
  docx)        FROM="docx" ;;
  html|htm)    FROM="html" ;;
  rst)         FROM="rst" ;;
  txt)         FROM="markdown" ;;
  *) echo "Unsupported input format: $in_ext" >&2; exit 3 ;;
esac

ARGS=(-f "$FROM" --wrap=none)
MEDIA_DIR="$(dirname "$OUT")/media"

case "$out_ext" in
  md|markdown)
    if [ "$in_ext" = "md" ] || [ "$in_ext" = "markdown" ]; then
      ARGS+=(-t gfm)
    else
      # Pandoc markdown flavour preserving citations as [@key];
      # gfm discards them when converting from tex/docx.
      ARGS+=(-t "markdown-smart-fenced_divs-bracketed_spans-native_divs-native_spans-header_attributes-link_attributes-simple_tables-multiline_tables-grid_tables+pipe_tables+tex_math_dollars")
    fi ;;
  tex|latex)   ARGS+=(-t latex -s --biblatex) ;;
  docx)        ARGS+=(-t docx) ;;
  html|htm)    ARGS+=(-t html -s --mathjax) ;;
  pdf)         ARGS+=(--pdf-engine=xelatex) ;;
  txt)         ARGS+=(-t plain) ;;
  rst)         ARGS+=(-t rst) ;;
  *) echo "Unsupported output format: $out_ext" >&2; exit 3 ;;
esac

# Extract images when reading docx
if [ "$in_ext" = "docx" ]; then
  ARGS+=(--extract-media="$MEDIA_DIR")
fi

# Citations
if [ -n "$BIB" ]; then
  ARGS+=(--citeproc --bibliography="$BIB")
fi

pandoc "${ARGS[@]}" "$IN" -o "$OUT"
echo "OK: $IN -> $OUT"
echo "Run now: python $(dirname "$0")/verify_conversion.py \"$IN\" \"$OUT\""
