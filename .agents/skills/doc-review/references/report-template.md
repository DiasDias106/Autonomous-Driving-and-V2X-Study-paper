# Modelo do relatório de revisão

Usar esta estrutura. Omitir uma secção só se não houver nada a dizer. Escrever na língua do documento revisto.

```markdown
# Revisão: [título do documento]

**Tipo de documento:** [survey / relatório formal / relatório simples / outro] (indicar se foi inferido)
**Extensão aproximada:** [páginas ou palavras]

## 1. Resumo da avaliação
3 a 5 frases: estado geral, principal força, principal fraqueza.

## 2. Mapa da estrutura
Lista das secções com uma frase sobre o papel de cada uma.

## 3. Problemas encontrados

### 3.1 Estrutura
| # | Gravidade | Local | Problema | Sugestão |
|---|-----------|-------|----------|----------|
| E1 | Crítico/Importante/Menor | Sec. X, §Y | ... | ... |

### 3.2 Vocabulário e linguagem
(mesma tabela, ids V1, V2...)

### 3.3 Coesão intertextual
(ids C1, C2...)

### 3.4 Conexões entre partes
(ids L1, L2...)

### 3.5 Conteúdo
(ids Q1, Q2...)

## 4. Análise de prós e contras

### Prós
Para cada um: **o quê**, **porquê importa**.

### Contras
Para cada um: **o quê**, **porquê importa**, **como corrigir**.

## 5. Veredicto e prioridades
- Veredicto global (2-3 frases).
- As 3 ações com maior retorno, por ordem.

## 6. Terminologia inconsistente (anexo, se aplicável)
| Termo A | Termo B | Ocorrências | Sugestão de termo único |
```

## Notas
- Os ids (E1, V2...) permitem ao autor referir-se aos problemas numa conversa de seguimento ("aplica E1 a E4").
- A coluna "Local" tem de permitir encontrar o problema sem procurar: secção, parágrafo e, se útil, citação curta do trecho.
- Se o utilizador só pedir uma dimensão (ex.: "vê só o vocabulário"), entregar apenas essa parte mais o resumo.
- Se o relatório for longo, entregá-lo como documento (ver skill de docs) e dar no chat apenas o resumo e as prioridades.
