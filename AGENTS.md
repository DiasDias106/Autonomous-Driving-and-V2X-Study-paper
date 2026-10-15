# Agent Directives — IoT Survey Report (Topic 24: Internet of Vehicles and V2X)

## 1. Project Context & Objectives
- **Institution:** Faculdade de Ci\^{e}ncias da Universidade de Lisboa (FCUL).
- **Course:** Internet das Coisas (IDC 2026/27)[cite: 2].
- **Authors:** Francisco Dias (68462, fc68462@alunos.ciencias.ulisboa.pt), Lu\'{i}s Lima (62214, 62214@alunos.ciencias.ulisboa.pt), Tiago Freitas (67976, fc67976@alunos.ciencias.ulisboa.pt).
- **Topic:** 24. Internet of Vehicles and V2X[cite: 7].
- **Target Deliverable:** A 10-page survey report (inclusive of references) formatted using the IEEE conference class[cite: 2, 38].
- **Core Requirements:**
  - Provide a thorough, critical analysis of current state-of-the-art research literature[cite: 2].
  - Clearly identify how IoT architectures, protocols, and paradigms underpin V2X communications[cite: 2].
  - Include at least 15–20 high-impact, recent peer-reviewed references[cite: 2].
  - Provide thorough answers to all three mandatory assignment research questions[cite: 2, 7].

---

## 2. Mandatory Topic Research Questions
Every generated or revised section must directly align with and answer the three assignment questions[cite: 2, 7]:
1. **Technical Comparison & Deployment Status:** Compare Cellular V2X (C-V2X: LTE-V2X, 5G NR-V2X) against IEEE standards (802.11p / WAVE, 802.11bd) in PHY/MAC architecture, latency, throughput, spectrum allocation, and commercial deployment status worldwide[cite: 7].
2. **Cooperative Perception & Autonomous Driving:** Analyse collective perception services (sensor sharing, CPM messages), specifying exact requirements for ultra-low latency (<10 ms), high throughput, and ultra-high reliability (>99.999%)[cite: 7].
3. **Security, Privacy & Pseudonym Systems:** Evaluate Vehicle PKI (V-PKI), pseudonym certificate rollover, pseudonym resolution/revocation mechanisms, communication overhead, and key limitations in high-density vehicular environments[cite: 7].

---

## 3. Page Budget & Section Layout (Strict 10-Page Cap)
The total compiled output must be exactly 10 pages (including the bibliography)[cite: 2]:
- **Section I — Introduction & IoT Foundation (approx. 1.0 page):** Evolution of connected vehicles within IoT; scopes of V2V, V2I, V2P, and V2N.
- **Section II — State of the Art: C-V2X vs. IEEE 802.11p/bd (approx. 2.5 pages):** Detailed technical taxonomy, comparative tables (PHY/MAC, modulation, sidelink modes), and deployment state (answers Question 1)[cite: 7].
- **Section III — V2X for Cooperative Perception & Automated Driving (approx. 2.0 pages):** Sensor sharing, cooperative maneuvers, and strict QoS/latency/reliability requirement trade-offs (answers Question 2)[cite: 7].
- **Section IV — V2X Security, Privacy & Pseudonym Lifecycles (approx. 2.0 pages):** V-PKI architectures, trust models, pseudonym revocation/management overhead, and practical attack surfaces (answers Question 3)[cite: 7].
- **Section V — Challenges, Open Issues & Future Directions (approx. 1.5 pages):** Resource allocation in high-density scenarios, spectrum coexistence, edge-computing integration, and migration towards 6G-V2X[cite: 2].
- **Section VI — Conclusion (approx. 0.5 page):** Synthesis of findings[cite: 2].
- **References (approx. 0.5–0.75 page):** Comprehensive IEEE-formatted bibliography[cite: 2, 24].

---

## 4. LaTeX Standards & Engineering Invariants
- **Class File:** Strictly use `\documentclass[conference]{IEEEtran}`[cite: 38]. Do not tamper with margins, geometry, or font size overrides (`IEEEtran.cls` manages all layout parameters)[cite: 10, 26, 38].
- **Modularity:**
  - `main.tex` only contains document configuration, package imports, and `\input{sections/...}` statements.
  - Never place main section prose directly into `main.tex`.
- **Semantic Line Breaks:**
  - Write strictly **one sentence per line**.
  - Never wrap entire paragraphs onto a single physical line. This minimizes Git diff churn and avoids merge conflicts between teammates.
- **Cross-Referencing & Labels:**
  - Use soft labels with strict prefixes: `\label{sec:...}`, `\label{fig:...}`, `\label{tab:...}`, `\label{eq:...}`[cite: 38].
  - Always place `\label{...}` *after* or *inside* `\caption{...}` for figures and tables[cite: 18, 26, 38].
  - Use `\eqref{eq:...}` for equations; do not write "Eq. \eqref{...}" unless starting a sentence[cite: 38].
  - Refer to figures as "Fig.~\ref{fig:...}"[cite: 18, 38, 41].
- **Math Environments:**
  - Never use the deprecated `\begin{eqnarray}` environment[cite: 16, 38]. Use `align` from `amsmath` or `IEEEeqnarray`[cite: 16, 38].
- **Floats & Figures:**
  - Float placement specifiers must favour top/bottom (`[!t]` or `[!b]`)[cite: 17, 38]. Never use middle-of-column floats (`[h]`)[cite: 17, 38].
  - Table captions appear *above* the table; figure captions appear *below*[cite: 18, 19, 38, 41].
- **Citations & Bibliography:**
  - All citations must use `\cite{key}`[cite: 16, 38].
  - Maintain all citation data strictly in `references.bib` using the `\bibliographystyle{IEEEtran}` style[cite: 24, 26, 38].
- **Last-Page Column Balancing:**
  - On page 10, balance the bibliography columns using `\IEEEtriggeratref{X}` or a manual `\newpage`[cite: 24].
- **Pagination:**
  - Include centered page numbers at the bottom of each page using `\pagestyle{plain}` and `\thispagestyle{plain}` after `\maketitle`.

## 5. Writing Style & Tone Guidelines
- **Target Audience & Author Voice:** This paper is meant to be written from our group of 3 non-English speaking people, and is meant to be read by a non-English person.
- **Vocabulary & Clarity:** We can all speak and write in English, but always keep a simple vocabulary, straight to the point. Avoid overly convoluted words or flowery phrases; prioritize clear, sequential, and direct explanations.

---

## 6. Verification Protocol
Before marking any task as complete:
1. Ensure all template placeholder text from `conference_041818.tex` is removed[cite: 38, 41].
2. Compile via CLI: `latexmk -pdf -interaction=nonstopmode main.tex`.
3. Check build logs to ensure zero undefined references (`?`) and zero overfull/underfull horizontal boxes.
4. Verify that total page count equals 10 pages[cite: 2].