# Conversão entre formatos

## Índice
1. Princípios
2. Comandos pandoc por par de formatos
3. LaTeX específico
4. Verificação
5. Problemas frequentes

## 1. Princípios

- Converter a partir do formato mais rico disponível. Se existir o `.tex` ou `.md` original, usar esse e não o PDF.
- Guardar sempre o original intacto; escrever a saída em ficheiro novo.
- Verificar o resultado (secção 4). Uma conversão "que correu sem erros" não é uma conversão sem perdas.

## 2. Comandos pandoc

Verificar: `which pandoc || pip install pypandoc_binary` (ou `apt-get install pandoc`).

| De → Para | Comando base |
|-----------|--------------|
| md → tex | `pandoc in.md -f markdown -t latex -s -o out.tex` |
| md → docx | `pandoc in.md -o out.docx` |
| md → html | `pandoc in.md -s --mathjax -o out.html` |
| md → pdf | `pandoc in.md --pdf-engine=xelatex -o out.pdf` |
| tex → md | `pandoc in.tex -f latex -t markdown-smart-fenced_divs-bracketed_spans-native_divs-native_spans-header_attributes-simple_tables-multiline_tables-grid_tables+pipe_tables+tex_math_dollars --wrap=none -o out.md` (o `gfm` descarta `\cite{}`; este sabor mantém `[@chave]`) |
| tex → docx | `pandoc in.tex -o out.docx` |
| docx → md | `pandoc in.docx -t gfm --wrap=none --extract-media=./media -o out.md` |
| docx → tex | `pandoc in.docx -t latex -s --extract-media=./media -o out.tex` |
| html → md | `pandoc in.html -t gfm --wrap=none -o out.md` |
| qualquer → txt | `pandoc in.ext -t plain --wrap=none -o out.txt` |

Opções úteis:
- `--citeproc --bibliography=refs.bib` para processar citações.
- `--number-sections` para numerar secções.
- `--toc` para índice.
- `--wrap=none` para não partir linhas (evita diffs ruidosos).
- `--standalone` (`-s`) para documento completo em tex/html.
- `--extract-media=DIR` ao ler docx, para não perder as imagens.

## 3. LaTeX específico

- Português: usar `xelatex`/`lualatex` e `\usepackage{polyglossia}` + `\setmainlanguage{portuguese}`, ou `\usepackage[portuguese]{babel}` com pdflatex.
- Bibliografia: preferir BibLaTeX (`\usepackage[backend=biber]{biblatex}`) com `\addbibresource{refs.bib}`.
- Tabelas largas: `\usepackage{longtable,booktabs}`; pandoc já os usa.
- Se o documento original usa classe ou pacotes próprios (IEEEtran, acmart, llncs), preservá-los em vez de os substituir pelo article.
- Ao passar de md para tex num modelo de survey ou relatório, mapear `#` → `\section`, `##` → `\subsection`, e manter `\label`/`\ref` coerentes.

## 4. Verificação

Correr sempre:

```bash
python scripts/verify_conversion.py ORIGEM DESTINO
```

O script extrai de ambos os ficheiros (md, tex, html, txt; para docx usa pandoc para texto) e compara:

- número de palavras (tolerância pequena, p. ex. 3%),
- número de títulos,
- número de tabelas,
- número de imagens/figuras,
- número de equações,
- número de links/URLs,
- número de citações/referências.

Interpretação:
- Diferença em palavras, secções, equações, figuras: tratar como perda até prova em contrário e investigar.
- Diferenças esperadas: comandos LaTeX que não contam como palavras, numeração automática, cabeçalhos de documento gerados.
- O script não substitui uma leitura rápida do resultado: abrir o ficheiro de saída e conferir as zonas de risco (equações, tabelas, referências).

## 5. Problemas frequentes

| Sintoma | Causa provável | Solução |
|---------|----------------|---------|
| Equações aparecem como texto | Markdown sem `$` ou extensão desligada | Usar `-f markdown+tex_math_dollars` |
| Citações viram `[?]` | Falta `--citeproc`/`.bib` | Passar `--bibliography` ou manter `\cite` em tex |
| Imagens desaparecem de docx | Esquecido `--extract-media` | Adicionar a opção |
| Tabela perde células fundidas | Markdown não suporta | Usar tabela HTML, ou manter em tex/docx |
| Acentos partidos em tex | Codificação | Garantir UTF-8, usar xelatex |
| Célula de tabela desaparece (tex → md, tabelas `longtable`) | Bug de leitura do pandoc | Conferir sempre as tabelas à mão; se faltar conteúdo, repor ou converter a tabela em HTML |
| Citações desaparecem em tex → md | Saída `gfm` não suporta citações | Usar o sabor markdown do pandoc (já feito em `convert.sh`) |
| PDF não compila | Falta pacote LaTeX | Instalar o pacote ou simplificar o preâmbulo |
