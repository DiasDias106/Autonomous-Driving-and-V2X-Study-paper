# Agent Directives — IoT Survey Report (Topic 24: Internet of Vehicles and V2X)

## 1. Project Context & Objectives
- **Institution:** Faculdade de Ciências da Universidade de Lisboa (FCUL).
- **Course:** Internet das Coisas (IDC 2026/27).
- **Authors:** Francisco Dias (68462, fc68462@alunos.ciencias.ulisboa.pt), Luís Lima (62214, 62214@alunos.ciencias.ulisboa.pt), Tiago Freitas (67976, fc67976@alunos.ciencias.ulisboa.pt).
- **Topic:** 24. Internet of Vehicles and V2X.
- **Target Deliverable:** A 10-page survey report (inclusive of references) formatted using the IEEE conference class.
- **Core Requirements:**
  - Provide a thorough, critical analysis of current state-of-the-art research literature.
  - Clearly identify how IoT architectures, protocols, and paradigms underpin V2X communications.
  - Include at least 15–20 high-impact, recent peer-reviewed references.
  - Provide thorough answers to all three mandatory assignment research questions.

---

## 2. Mandatory Topic Research Questions
Every generated or revised section must directly align with and answer the three assignment questions:
1. **Technical Comparison & Deployment Status:** Compare Cellular V2X (C-V2X: LTE-V2X, 5G NR-V2X) against IEEE standards (802.11p / WAVE, 802.11bd) in PHY/MAC architecture, latency, throughput, spectrum allocation, and commercial deployment status worldwide.
2. **Cooperative Perception & Autonomous Driving:** Analyse collective perception services (sensor sharing, CPM messages), specifying exact requirements for ultra-low latency (<10 ms), high throughput, and ultra-high reliability (>99.999%).
3. **Security, Privacy & Pseudonym Systems:** Evaluate Vehicle PKI (V-PKI), pseudonym certificate rollover, pseudonym resolution/revocation mechanisms, communication overhead, and key limitations in high-density vehicular environments.

---

## 3. Page Budget & Section Layout (Strict 10-Page Cap)
The total compiled output must be exactly 10 pages (including the bibliography):
- **Section I — Introduction & IoT Foundation (approx. 1.0 page):** Evolution of connected vehicles within IoT; scopes of V2V, V2I, V2P, and V2N.
- **Section II — State of the Art: C-V2X vs. IEEE 802.11p/bd (approx. 2.5 pages):** Detailed technical taxonomy, comparative tables (PHY/MAC, modulation, sidelink modes), and deployment state (answers Question 1).
- **Section III — V2X for Cooperative Perception & Automated Driving (approx. 2.0 pages):** Sensor sharing, cooperative maneuvers, and strict QoS/latency/reliability requirement trade-offs (answers Question 2).
- **Section IV — V2X Security, Privacy & Pseudonym Lifecycles (approx. 2.0 pages):** V-PKI architectures, trust models, pseudonym revocation/management overhead, and practical attack surfaces (answers Question 3).
- **Section V — Challenges, Open Issues & Future Directions (approx. 1.5 pages):** Resource allocation in high-density scenarios, spectrum coexistence, edge-computing integration, and migration towards 6G-V2X.
- **Section VI — Conclusion (approx. 0.5 page):** Synthesis of findings.
- **References (approx. 0.5–0.75 page):** Comprehensive IEEE-formatted bibliography.

---

## 4. LaTeX Standards & Engineering Invariants
- **Class File:** Strictly use `\documentclass[conference]{IEEEtran}`. Do not tamper with margins, geometry, or font size overrides (`IEEEtran.cls` manages all layout parameters).
- **Modularity:**
  - `main.tex` only contains document configuration, package imports, and `\input{sections/...}` statements.
  - Never place main section prose directly into `main.tex`.
- **Semantic Line Breaks:**
  - Write strictly **one sentence per line**.
  - Never wrap entire paragraphs onto a single physical line. This minimizes Git diff churn and avoids merge conflicts between teammates.
- **Cross-Referencing & Labels:**
  - Use soft labels with strict prefixes: `\label{sec:...}`, `\label{fig:...}`, `\label{tab:...}`, `\label{eq:...}`.
  - Always place `\label{...}` *after* or *inside* `\caption{...}` for figures and tables.
  - Use `\eqref{eq:...}` for equations; do not write "Eq. \eqref{...}" unless starting a sentence.
  - Refer to figures as "Fig.~\ref{fig:...}".
- **Math Environments:**
  - Never use the deprecated `\begin{eqnarray}` environment. Use `align` from `amsmath` or `IEEEeqnarray`.
- **Floats & Figures (Top Placement):**
  - Try to always place figures and tables at the top of pages using `[!t]`. Never use middle-of-column floats (`[h]`).
  - Table captions appear *above* the table; figure captions appear *below*.
- **Citations & Bibliography:**
  - All citations must use `\cite{key}`.
  - Maintain all citation data strictly in `references.bib` using the `\bibliographystyle{IEEEtran}` style.
  - Avoid placing citations at the beginning of a line or sentence (e.g., `[1] ...`). Always attach `\cite{...}` to the preceding word using a non-breaking tilde `~` (e.g., `web preservation~\cite{...}`).
- **Formulas & Equation Numbering:**
  - Whenever an equation is assigned a number like (1), (2), etc. via `\begin{equation}` and `\label{eq:...}`, that number must be explicitly referenced in the text using `\eqref{eq:...}`.
  - If a formula is not referenced in the body text, remove its assigned number and label by using unnumbered math environments (`\[ ... \]` or `equation*`).
- **Last-Page Column Balancing:**
  - On page 10, balance the bibliography columns using `\IEEEtriggeratref{X}` or a manual `\newpage`.
- **Pagination:**
  - Include centered page numbers at the bottom of each page using `\pagestyle{plain}` and `\thispagestyle{plain}` after `\maketitle`.

## 5. Writing Style & Tone Guidelines
- **Target Audience & Author Voice:** This paper is meant to be written from our group of 3 non-English speaking people, and is meant to be read by a non-English person.
- **Vocabulary & Clarity:** We can all speak and write in English, but always keep a simple vocabulary, straight to the point. Avoid overly convoluted words or flowery phrases; prioritize clear, sequential, and direct explanations.
- **Language & Spelling (English UK):** Everything in the paper has to be in English (UK) (British English conventions, e.g., 'colour', 'behaviour', 'modelling', 'programme', 'analyse', 'optimise', 'prioritise'). All text, captions, figures, and tables must consistently adhere to UK English conventions.
- **Acronym Usage & Lifecycle:**
  - Avoid introducing acronyms if they are not relevant or not supposed to be remembered/used again in the paper (e.g. write out terms like "signal phase and timing" without parenthesised abbreviations if only mentioned once).
  - If an acronym is used, always make sure it has been explicitly defined (expanded) upon its first occurrence in the paper (e.g., \textit{Full Name} (FN)) before using the abbreviation.

---

## 6. Verification Protocol
Before marking any task as complete:
1. Ensure all template placeholder text from `conference_041818.tex` is removed.
2. Compile via CLI: `latexmk -pdf -interaction=nonstopmode main.tex`.
3. Check build logs to ensure zero undefined references (`?`) and zero overfull/underfull horizontal boxes.
4. Verify that total page count equals 10 pages.
5. Verify that all spelling and conventions strictly follow English (UK).
6. Verify that all acronyms used are defined on first occurrence and that single-use/throwaway acronyms are eliminated.

