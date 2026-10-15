---
name: survey-from-sources
description: Reads the source materials stored in the project's sources folder (PDFs, Word, HTML, Markdown, text, notes), filters out what is irrelevant, and writes a new text in the form of a survey (revisão/estado da arte) about a topic given by the user, connecting that topic to neighbouring topics and to its historical background while keeping the given topic as the protagonist. Use this skill whenever the user asks to write, draft, extend or rewrite a survey, state of the art, literature review, overview, "revisão da literatura", "estado da arte" or "texto tipo survey" based on the project's sources, or asks to create new text "a partir das fontes", "com base na pasta de sources", "usando a informação que deixei no folder", even if they never say the word "survey".
---

# Survey from sources

Turn the material the user has gathered in the project's sources folder into a clear, well-structured survey about a topic they name. The topic the user gives is always the protagonist; neighbouring topics and history exist only to situate it.

## Why this skill exists

The user collects sources in a folder and wants an agent that (1) actually reads them, (2) keeps only what serves the topic, (3) writes in the shape a reader of a survey expects, and (4) places the topic in context (what came before it, what sits beside it) without drifting away from it. Most failures come from one of four things: skimming instead of reading, copying everything in, losing the topic in the context, or writing a wall of text with no structure. The workflow below is built to avoid each.

## Inputs to settle first

Settle these from the conversation; ask the user only for what is missing, and ask once, briefly.

- **Main topic** (required): the subject of the survey.
- **Sources folder**: default to a folder named `sources`, `fontes` or `references` in the project; if there are several candidates or none, ask.
- **Adjacent topics** (optional): the topic(s) it sits between or next to (e.g. "between A and B"). If not given, infer them from the sources and tell the user which ones you chose.
- **Language and register**: write in the language the user writes in (European Portuguese if they write in European Portuguese) unless told otherwise. Academic but plain.
- **Length / audience**: if not given, aim for roughly 1500–3000 words for a short survey and say so.

## Workflow

### 1. Inventory the sources

Run `scripts/inventory.py <sources_folder>` to list every file and extract its text into a working folder (`.survey_work/text/`). Read the printed report: it shows which files were read, which failed (scanned PDFs, unsupported formats) and the size of each. Tell the user about any file you could not read instead of silently skipping it.

If the script cannot run, read the files directly with the tools available.

### 2. Read and filter each source

Open each extracted text and read it for real. For every source write a short note in `.survey_work/notes.md` using this shape:

```
## <file name>
- Relevance to main topic: high / medium / low / none  (one-line reason)
- Type: primary study | review | tutorial | news/blog | standard/spec | other
- Key claims (each with page/section if available):
  - ...
- Definitions, methods, datasets, results worth citing:
  - ...
- Links to adjacent topics or to history:
  - ...
- Discard: navigation text, ads, cookie banners, repeated headers/footers, reference lists copied from elsewhere, boilerplate
```

Filtering rules, and why:

- **Relevance is judged against the main topic, not against the file's own subject.** A long paper that mentions the topic in one paragraph contributes that paragraph, not its whole content.
- **Keep claims, not prose.** The survey is written fresh in your own words; sources supply facts, definitions and positions. This avoids copy-paste text and any copyright problems.
- **Deduplicate.** When several sources say the same thing, note it once and list all supporting sources; agreement across sources is useful evidence.
- **Record disagreements.** Where sources contradict each other, keep both positions; a survey is more valuable when it maps the debate.
- **Never invent.** If a point is not in the sources, it either stays out or is explicitly marked as general background knowledge that needs a source (see step 6).
- **Low and none relevance** sources are not used in the text; list them at the end of your reply so the user can confirm.

### 3. Map the topic and its neighbours

Before outlining, write a small map in `.survey_work/map.md`:

- **Main topic**: one-sentence definition from the sources.
- **Antecedents**: earlier ideas, methods or events the topic grew out of (the "past").
- **Neighbouring topics**: for each, the specific relationship (builds on, contrasts with, overlaps with, enables, competes with) and which sources support it.
- **Bridge sentences**: for each neighbour, one draft sentence that goes from the neighbour back to the main topic.

If the user said the topic sits between two others, make those two the first neighbours on the map. See `references/bridging.md` for patterns.

### 4. Outline the survey

Use the structure in `references/survey_structure.md`. Group the content by theme or approach (a taxonomy), not by source: a survey organised as "Source 1 says…, Source 2 says…" is a list of summaries, not a survey. Show the outline to the user only if the task is large or ambiguous; otherwise proceed.

### 5. Write

Rules for the writing itself:

- **Main topic first.** Roughly two thirds or more of the body should be about the main topic itself. Context sections are shorter and always end by returning to it.
- **Place the topic early.** The introduction states what the topic is, why it matters, and where it sits in relation to its neighbours and its past, in a few sentences, before the detailed sections.
- **Every adjacent topic needs a reason to be there.** Introduce it with its relationship to the main topic ("X precedes it because…", "Y addresses the same problem but differs in…"). If you cannot state the relationship in one sentence, leave the topic out.
- **One idea per paragraph, topic sentence first.** Short paragraphs, signposting sentences between sections, and no more than three levels of headings. Clarity beats density.
- **Define terms on first use** and keep terminology consistent throughout.
- **Cite as you go.** Attribute each non-trivial claim to its source with a bracketed key such as `[Silva2021]` or `[file-name]`, and finish with a reference list built from the sources actually used. Quote sparingly and briefly; paraphrase by default.
- **Use tables or short lists only where they help** (for example a comparison table of approaches). The body is prose.

### 6. Check before delivering

Go through this list and fix problems before replying:

1. Does the text open with the main topic and keep returning to it?
2. Is every adjacent topic tied to the main topic by an explicit sentence?
3. Does the structure follow the survey template, with a taxonomy rather than a source-by-source list?
4. Is every claim traceable to a source in the folder? Anything from your own background knowledge is either removed or flagged with `[needs source]`.
5. Is any paragraph confusing, over-long or repeating another? Cut or split it.
6. Is the reference list consistent with the in-text citations?

### 7. Deliver

Save the survey as a Markdown file (or the format the user asked for) in the outputs location, and reply briefly with:

- what was written and where;
- which sources were used and which were set aside, with the reason;
- which neighbouring topics were chosen and why;
- any gaps found (parts of the topic the sources do not cover) so the user knows what to add to the folder.

Keep the working notes (`.survey_work/`) so the user can audit how the text was built.

## Reference files

- `references/survey_structure.md`: the section-by-section template for the survey. Read it at step 4.
- `references/bridging.md`: how to connect the topic to its past and to neighbouring topics without losing focus. Read it at step 3.
- `scripts/inventory.py`: lists and extracts text from the files in the sources folder.
