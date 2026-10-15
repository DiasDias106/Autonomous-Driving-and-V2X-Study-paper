---
name: doc-review
description: Revê criticamente um documento (survey, relatório, artigo, tese, capítulo) e devolve um diagnóstico detalhado - falhas de estrutura, problemas de vocabulário, falta de coesão intertextual, ligações fracas entre secções - mais uma análise de prós e contras. Usar sempre que o utilizador pedir para rever, criticar, avaliar, fazer feedback, "ver se está bom", encontrar falhas ou melhorar um documento, mesmo que não diga "review" explicitamente. Especialmente indicado para o projeto de survey de IT. Não reescreve o documento, a menos que seja pedido.
---

# Doc Review

Esta skill faz a revisão crítica de um documento escrito. O objetivo é dar ao autor um diagnóstico que ele possa **agir de imediato**: cada problema tem de apontar para um local concreto do texto e ter uma sugestão de correção. Uma revisão vaga ("a estrutura podia ser melhor") não serve a ninguém.

## Princípios

- **Responder na língua do documento** (se o documento está em inglês, a revisão sai em inglês, salvo pedido em contrário).
- **Ser específico**: citar a secção, parágrafo ou frase (citações curtas) onde o problema ocorre.
- **Ser justo**: apontar também o que está bem feito. Uma revisão só com críticas perde credibilidade e o autor não sabe o que deve preservar.
- **Não inventar problemas**: se uma dimensão está sólida, dizê-lo. Prefira poucos problemas reais a muitos duvidosos.
- **Não alterar o conteúdo** do documento original. A revisão é um relatório à parte.

## Fluxo de trabalho

1. **Ler o documento inteiro antes de comentar.** Muitas falhas (repetição, ideias prometidas e não cumpridas, conceitos usados antes de definidos) só se veem com a visão global. Se o ficheiro for .docx, .pdf ou .tex, extrair o texto primeiro (ver as skills docx/pdf, ou pandoc).
2. **Mapear a estrutura**: listar secções e subsecções, com uma frase sobre o papel de cada uma. Este mapa serve de base para as análises seguintes e vai também para o relatório.
3. **Passar pelas cinco dimensões** descritas abaixo. Para o detalhe de cada critério, ler `references/checklist.md`.
4. **Fazer a análise de prós e contras.**
5. **Compilar o relatório** com o formato de `references/report-template.md`.
6. **Priorizar**: ordenar os problemas por gravidade, para o autor saber por onde começar.

## As cinco dimensões

1. **Estrutura**: ordem lógica, equilíbrio entre secções, secções em falta ou redundantes, hierarquia de títulos, introdução que anuncia o que o documento realmente contém, conclusão que fecha o que foi aberto.
2. **Vocabulário e linguagem**: terminologia inconsistente (o mesmo conceito com nomes diferentes), jargão não definido, acrónimos sem expansão na primeira ocorrência, registo desadequado, ambiguidade, frases demasiado longas, vícios de escrita, repetição de palavras.
3. **Coesão intertextual** (dentro do documento e com a literatura): afirmações sem suporte ou sem citação, referências citadas mas não discutidas, referências na lista final que não aparecem no texto (e vice-versa), contradições entre secções, falta de posicionamento face a trabalhos relacionados. No caso de um survey, verificar também se a literatura é comparada e não apenas listada.
4. **Conexões entre partes**: transições entre secções, fio condutor, referências cruzadas ("como visto na Secção 3"), promessas da introdução cumpridas nas secções seguintes, conclusões que realmente decorrem do corpo do texto.
5. **Qualidade do conteúdo**: profundidade, rigor, cobertura do tema, exemplos, figuras e tabelas (legendadas, referidas no texto, legíveis), argumentação.

## Prós e contras

Esta parte é uma análise, não uma lista de pontos soltos. Para cada pró e cada contra:

- dizer **o quê**,
- dizer **porquê** importa (impacto no leitor ou na credibilidade do trabalho),
- para os contras, dar **como corrigir**.

Terminar com um **veredicto global** curto: estado atual do documento, o que mais o limita, e as 3 ações com melhor retorno.

## Níveis de gravidade

Classificar cada problema para o autor poder priorizar:

- **Crítico**: compromete a compreensão ou a credibilidade (contradição, secção essencial em falta, conclusão sem suporte).
- **Importante**: prejudica a qualidade mas o documento ainda funciona (transições fracas, terminologia inconsistente).
- **Menor**: polimento (estilo, repetições, formatação).

## Adaptar ao tipo de documento

Se o utilizador disser o tipo (survey, relatório formal, relatório simples), ajustar as expectativas: um survey deve ter taxonomia/classificação clara, critérios de seleção da literatura e comparação entre trabalhos; um relatório simples não precisa da mesma densidade de referências. Se o tipo não for dito, inferi-lo do próprio texto e indicar a inferência no início da revisão.

## Quando o documento é grande

Para documentos longos, rever por partes e depois fazer uma passagem final só de consistência global (terminologia, referências cruzadas, promessas da introdução vs. conclusão). Se houver subagentes disponíveis, pode-se distribuir secções por subagentes, mas a passagem global faz-se sempre com a visão do documento completo.
