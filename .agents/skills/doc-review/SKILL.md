---
name: doc-review
description: Critically reviews a document (survey, report, paper, thesis, chapter) and returns a detailed diagnosis - structural flaws, vocabulary issues, lack of intertextual cohesion, weak connections between sections - plus a pros and cons analysis. Use whenever the user asks to review, critique, evaluate, provide feedback, "see if it looks good", find flaws or improve a document, even without saying "review" explicitly. Especially suitable for the IT/IoT survey project. Does not rewrite the document unless requested.
---

# Doc Review

This skill performs a critical review of a written document. The objective is to provide the author with an **actionable diagnosis**: every identified issue must point to a specific location in the text and offer a concrete suggestion for improvement. Vague feedback ("the structure could be better") is not helpful.

## Principles

- **Respond in the document's language** (if the document is written in English, the review must be in English, unless requested otherwise).
- **Be specific**: cite the section, paragraph, or sentence (using short quotes) where the issue occurs.
- **Be balanced and fair**: highlight what is well done as well. A review containing only criticisms loses credibility and leaves the author unsure of what should be preserved.
- **Do not fabricate issues**: if a specific dimension is solid, state so explicitly. Prefer a few genuine issues over many dubious ones.
- **Do not modify original document content**. The review is delivered as a separate report.

## Workflow

1. **Read the entire document before commenting.** Many flaws (repetition, unfulfilled promises, concepts used before being defined) are only visible with a global perspective. If the file is .docx, .pdf, or .tex, extract the plain text first (refer to docx/pdf skills, or pandoc).
2. **Map the structure**: list sections and subsections with a single sentence summarising the role of each. This map serves as the baseline for subsequent analyses and is included in the final report.
3. **Evaluate the five core dimensions** detailed below. For specific criteria, consult `references/checklist.md`.
4. **Conduct a pros and cons analysis.**
5. **Compile the report** using the template in `references/report-template.md`.
6. **Prioritise findings**: order issues by severity so the author knows where to focus first.

## The Five Dimensions

1. **Structure**: logical progression, balance across sections, missing or redundant sections, heading hierarchy, an introduction that accurately outlines document contents, and a conclusion that synthesises open threads.
2. **Vocabulary and Language**: inconsistent terminology (using different names for the same concept), undefined jargon, acronyms not expanded on first use, inappropriate register, ambiguity, overly long sentences, repetitive phrasing.
3. **Intertextual Cohesion** (internal consistency and engagement with literature): unsupported factual claims, references cited without discussion, bibliography entries missing in-text citations (or vice versa), contradictions between sections, lack of clear positioning relative to related work. In a survey, ensure literature is critically compared rather than merely listed.
4. **Connections Between Sections**: transitions between sections, narrative thread ("golden thread"), cross-references ("as discussed in Section 3"), promises made in the introduction delivered in subsequent sections, conclusions that logically follow from the body.
5. **Content Quality**: depth, technical rigour, topical coverage, illustrative examples, figures and tables (captioned, referenced in text, legible), argumentation quality.

## Pros and Cons

This section is an analytical evaluation, not a disconnected list of bullet points. For each pro and con:

- state **what**,
- explain **why it matters** (impact on reader comprehension or academic credibility),
- for cons, provide **how to fix it**.

Conclude with a concise **overall verdict**: current document state, primary limiting factor, and top 3 highest-impact actions.

## Severity Levels

Classify each issue to help the author prioritise:

- **Critical**: impairs comprehension or academic credibility (contradictions, missing core section, unsupported conclusion).
- **Important**: degrades quality but document remains functional (weak transitions, inconsistent terminology).
- **Minor**: stylistic polish (phrasing, repetition, minor formatting).

## Adapting to Document Type

If the user specifies the document type (survey, formal report, simple report), adapt expectations accordingly: a survey requires a clear taxonomy, literature selection criteria, and cross-comparison tables; a simple report does not need dense citations. If not specified, infer the type from the text and note this inference at the beginning of the review.

## Handling Large Documents

For long documents, review section by section and perform a final pass focused on global consistency (terminology, cross-references, intro promises vs. conclusion). If subagents are available, sections can be distributed across subagents, but the final consistency pass must evaluate the complete document.
