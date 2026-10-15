---
name: doc-format
description: Formata documentos segundo modelos predefinidos (survey, relatório formal, relatório simples) e converte documentos entre formatos (Markdown, LaTeX, DOCX, HTML, PDF, texto simples) sem perder conteúdo. Usar sempre que o utilizador pedir para formatar, reformatar, estruturar, "pôr no formato de survey/relatório", converter, passar para LaTeX, passar para Markdown, exportar para Word/PDF/HTML, ou adaptar um documento a outro formato, mesmo que não use a palavra "formato". Preserva todo o conteúdo (texto, equações, tabelas, figuras, citações, referências) e valida a conversão.
---

# Doc Format

Esta skill tem duas funções que se combinam: **aplicar um modelo de formato** (survey, relatório formal, relatório simples) e **converter entre formatos de ficheiro** (md, LaTeX, docx, html, pdf, txt). A regra central é que **formatar e converter nunca podem perder nem alterar conteúdo**: mudam a forma, não o que está dito. É por isso que há uma verificação no fim.

## Escolher o que fazer

Identificar o pedido:

| Pedido | Ação |
|--------|------|
| "Formata isto como survey / relatório" | Aplicar modelo (passos A) |
| "Converte para LaTeX / md / docx..." | Converter (passos B) |
| "Passa isto para relatório formal em LaTeX" | A e depois B |

Se o tipo de modelo não for indicado, perguntar uma vez (survey, relatório formal ou relatório simples) ou, se o conteúdo o deixar óbvio, inferir e dizer qual foi escolhido. Se o formato de saída não for indicado, usar Markdown como predefinição e dizê-lo.

## A. Aplicar um modelo

Os três modelos estão em `references/formats.md`. Ler esse ficheiro, escolher o modelo e seguir estes passos:

1. **Ler o documento inteiro** e fazer um inventário do conteúdo: secções, equações, tabelas, figuras, listas, citações, referências, notas de rodapé, links, blocos de código.
2. **Mapear o conteúdo para as secções do modelo.** Cada bloco de conteúdo existente vai para a secção que lhe corresponde.
3. **Conteúdo sem lugar no modelo**: não o apagar. Colocá-lo na secção mais próxima, ou criar uma subsecção, e avisar o utilizador.
4. **Secções do modelo sem conteúdo**: não inventar texto. Deixar a secção com um marcador `[EM FALTA: descrição do que deve entrar]` e listar estas faltas no fim da resposta. Inventar conteúdo num documento de investigação é pior do que deixar uma lacuna visível.
5. **Não reescrever o texto** do autor, a menos que seja pedido. Pode-se corrigir apenas formatação (títulos, listas, numeração, legendas). Se houver erros de conteúdo, mencioná-los à parte (para análise de qualidade, existe a skill doc-review).
6. Entregar o documento e um resumo curto: o que foi movido, o que ficou em falta.

## B. Converter entre formatos

Instruções detalhadas e comandos em `references/conversion.md`. Resumo:

1. **Usar pandoc** para as conversões de texto estruturado (md, tex, docx, html, rst). Verificar se está instalado (`which pandoc`); se não, tentar instalar.
2. **Converter via script**: `scripts/convert.sh <entrada> <saida>` escolhe a conversão pelo tipo de ficheiro e aplica as opções que protegem equações, citações e tabelas.
3. **Validar sempre** com `python scripts/verify_conversion.py <entrada> <saida>`: compara contagem de palavras, secções, tabelas, figuras, equações, links e referências entre origem e destino e assinala diferenças. Corrigir o que for perda real; explicar ao utilizador o que for diferença esperada (ex.: numeração automática).
4. **Para PDF** como destino: usar a skill pdf, ou LaTeX/pandoc com motor de PDF. PDF é formato de saída, não de edição; avisar se o utilizador quiser voltar atrás a partir de um PDF (a conversão inversa perde estrutura).
5. **Para docx** como destino ou origem, consultar a skill docx.

## Onde há risco de perda

Estes são os pontos em que as conversões costumam falhar. Verificar sempre:

- **Equações** (LaTeX ↔ md ↔ docx): preservar `$...$` e `$$...$$`; em docx, equações viram objetos nativos.
- **Tabelas complexas** (células fundidas, tabelas largas): em Markdown simples podem perder a fusão de células; usar tabelas HTML ou avisar.
- **Citações e bibliografia**: manter chaves BibTeX (`\cite{key}` ↔ `[@key]`); não converter para texto solto sem avisar. Manter o ficheiro `.bib`.
- **Figuras**: manter referências a ficheiros de imagem, legendas e labels.
- **Referências cruzadas** (`\ref`, `\label`): preservar.
- **Notas de rodapé, links, código**: confirmar que sobrevivem.
- **Caracteres especiais e acentos**: garantir UTF-8 e, em LaTeX, `\usepackage[utf8]{inputenc}` ou XeLaTeX/LuaLaTeX para português.

## Resposta final

Entregar o ficheiro (com `SendUserFile`) e, em poucas linhas: modelo/formato aplicado, resultado da verificação (sem perdas / diferenças encontradas), e o que ficou em falta ou foi movido.
