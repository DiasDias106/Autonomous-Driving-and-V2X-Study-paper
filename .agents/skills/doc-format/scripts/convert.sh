#!/usr/bin/env bash
# Converte um documento entre formatos usando pandoc, com opções que protegem
# equações, citações, tabelas e imagens.
# Uso: convert.sh <entrada> <saida> [bibliografia.bib]
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Uso: $0 <entrada> <saida> [bibliografia.bib]" >&2
  exit 1
fi

IN="$1"
OUT="$2"
BIB="${3:-}"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc nao encontrado. Instalar com: pip install pypandoc_binary  (ou apt-get install pandoc)" >&2
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
  *) echo "Formato de entrada nao suportado: $in_ext" >&2; exit 3 ;;
esac

ARGS=(-f "$FROM" --wrap=none)
MEDIA_DIR="$(dirname "$OUT")/media"

case "$out_ext" in
  md|markdown)
    if [ "$in_ext" = "md" ] || [ "$in_ext" = "markdown" ]; then
      ARGS+=(-t gfm)
    else
      # Sabor de markdown do pandoc que preserva citacoes como [@chave];
      # o gfm descarta-as ao converter a partir de tex/docx.
      ARGS+=(-t "markdown-smart-fenced_divs-bracketed_spans-native_divs-native_spans-header_attributes-link_attributes-simple_tables-multiline_tables-grid_tables+pipe_tables+tex_math_dollars")
    fi ;;
  tex|latex)   ARGS+=(-t latex -s --biblatex) ;;
  docx)        ARGS+=(-t docx) ;;
  html|htm)    ARGS+=(-t html -s --mathjax) ;;
  pdf)         ARGS+=(--pdf-engine=xelatex) ;;
  txt)         ARGS+=(-t plain) ;;
  rst)         ARGS+=(-t rst) ;;
  *) echo "Formato de saida nao suportado: $out_ext" >&2; exit 3 ;;
esac

# Extrair imagens ao ler docx
if [ "$in_ext" = "docx" ]; then
  ARGS+=(--extract-media="$MEDIA_DIR")
fi

# Citacoes
if [ -n "$BIB" ]; then
  ARGS+=(--citeproc --bibliography="$BIB")
fi

pandoc "${ARGS[@]}" "$IN" -o "$OUT"
echo "OK: $IN -> $OUT"
echo "Correr agora: python $(dirname "$0")/verify_conversion.py \"$IN\" \"$OUT\""
