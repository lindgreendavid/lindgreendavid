<p align="center">
  <img src="brand/lab-notes-mark.svg" width="112" alt="Lab Notes research-cycle mark">
</p>

# David Lindgreen

### Building trustworthy data products from mathematical foundations to accessible interfaces

I work at the intersection of **responsible AI**, **data science**, **mathematics**, **analytics engineering**, and **scientific UI/UX**. My projects emphasize explicit assumptions, reproducible experiments, strong software architecture, and honest limits—not just attractive outputs. The portfolio shares a versioned [Lab Notes identity and research-interface standard](brand/README.md): one recognisable family, with discipline-specific accents that communicate rather than decorate.

## Current focus

- Fairness and robustness under distribution shift
- Uncertainty-aware machine learning and model evaluation
- Explainable, accessible research interfaces
- Mathematical algorithms in Rust and WebAssembly
- Data quality, observability, and reproducible analytics
- Accessible science communication — physics, astrophysics, and biology, held to the same bar as the AI work: a bounded question, real evidence (public data where possible), and honest limits, not a hot take

## Featured work

### [Lab Notes — read and explore the science hub](https://blog-interactive.lindgreendavid.workers.dev/)

An accessible, continuously growing editorial home for the portfolio's research: plain-language
articles, a filterable evidence explorer, and a reusable four-step guide for reading scientific results.
Every project is presented through the same inspectable structure — question, evidence, finding,
and boundary — with direct routes into the underlying interactive laboratory and source code.
The production site is live on Cloudflare Workers. [Source code](https://github.com/lindgreendavid/blog)

`TypeScript` · `Science Communication` · `Interactive Learning` · `Accessibility` · `Scientific UI/UX`

### [Fairshift Lab — open the interactive laboratory](https://fairshift-lab.lindgreendavid.chatgpt.site)

A reproducible Responsible AI laboratory for exploring how distribution shift changes probability calibration, threshold-sensitive decisions, performance, and group-fairness measurements. Visitors can manipulate the population and decision threshold, compare source and target reliability, and inspect uncertainty without installing anything. Version 1.3.0 adds a Robustness Lab — a preregistered synthetic stress study comparing two model families under label noise, measurement error, an unobserved subgroup, and structural misspecification — on top of v1.1's Policy Studio and v1.2's governed external evidence from real 1994 Census data. [Source code](https://github.com/lindgreendavid/fairshift-lab) · [v1.3.0 release](https://github.com/lindgreendavid/fairshift-lab/releases/tag/v1.3.0)

`Python` · `TypeScript` · `Probability Calibration` · `Distribution Shift` · `Responsible AI` · `Scientific UI/UX`

### [Data Contract Observatory — break a public-data pipeline safely](https://lindgreendavid.github.io/data-contract-observatory/)

An inspectable observability case study built on the European Central Bank's official daily
US dollar/euro reference-rate series. Protocol 1.0.0 freezes the series identity, schema,
TARGET-day freshness rule, value constraints, and a separately labelled robust statistical review
signal before the full live evaluation. The first recorded run inspected 385 observations, passed
every hard contract check, and emitted no review signal. The interactive failure lab lets visitors
remove a required field, change the series identity, simulate lateness, or inject an extreme return
while showing exactly which conclusion each outcome permits. [Source code](https://github.com/lindgreendavid/data-contract-observatory) · [Frozen protocol](https://github.com/lindgreendavid/data-contract-observatory/blob/main/docs/protocol.md)

`Python` · `Data Contracts` · `Observability` · `SDMX` · `Public Data` · `Scientific UI/UX`

### [FRB Atlas — open the interactive laboratory](https://frb-atlas-interactive.lindgreendavid.workers.dev)

A reproducible reanalysis of the real, public CHIME/FRB Catalog 1 (536 fast radio bursts, Amiri et al. 2021): does the dispersion measure of repeating bursts actually differ from non-repeating ones, as the original paper's own preregistered test claims it doesn't? Version 0.1.0 cleanly replicates the paper's pulse-width/bandwidth finding as a validation check, then reports a genuine discrepancy on dispersion measure — traced honestly to sample composition (two prolific nearby repeaters dominating the burst sample) rather than smoothed over. [Source code](https://github.com/lindgreendavid/frb-atlas) · [Research report](https://github.com/lindgreendavid/frb-atlas/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Astrophysics` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Folding's Edge — open the interactive laboratory](https://foldings-edge-interactive.lindgreendavid.workers.dev)

A reproducible test of how well AlphaFold2's per-residue confidence score (pLDDT) predicts real, curated intrinsic disorder. 387 human proteins from DisProt (228,662 residues) joined to real AlphaFold DB predictions by UniProt accession — no model training, just a fresh statistical test of a specific published claim (Alderson et al. 2023, PNAS). Version 0.1.0 confirms pLDDT is a strong overall signal (43-point median gap, p≈0) but names exactly where it fails: precision collapses on regions that can conditionally fold (6.3% vs. 31% baseline) and on disorder evidenced by HDX-MS, with specific proteins named rather than only aggregate rates. Its hero animation traces one of those named proteins' real per-residue pLDDT values as a wiggling chain, and an interactive threshold explorer lets you drag the pLDDT cutoff and watch precision/recall/F1/MCC update live from the real data, with one click back to the actual preregistered threshold. [Source code](https://github.com/lindgreendavid/foldings-edge) · [Research report](https://github.com/lindgreendavid/foldings-edge/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Structural Biology` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Three-Body Lab — open the interactive laboratory](https://three-body-lab-interactive.lindgreendavid.workers.dev)

A reproducible computational-physics laboratory mapping the boundary between quasi-periodic and chaotic motion in the planar gravitational three-body problem, via empirically estimated Lyapunov exponents. Visitors can watch a reference trajectory and a near-identical perturbed twin diverge in real time, export a clip of the divergence, and inspect a frozen, preregistered sweep that tests the figure-eight, Lagrange equilateral, and Euler collinear special solutions against that boundary. Version 0.1.0 does not claim to solve the three-body problem — it reports what a disclosed numerical method actually finds, including two hypotheses it falsified. [Source code](https://github.com/lindgreendavid/three-body-lab) · [Research report](https://github.com/lindgreendavid/three-body-lab/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Computational Physics` · `Chaos Theory` · `Numerical Integration` · `Scientific UI/UX`

### [Climate Twin Frankfurt — open the interactive laboratory](https://climate-twin-frankfurt-interactive.lindgreendavid.workers.dev)

A reproducible measurement of Frankfurt's urban heat island from real DWD station records: the inner-city Frankfurt/Main-Westend station against Frankfurt/Main — DWD's own designated reference counterpart (physically the airport, disclosed rather than glossed over) — across every valid paired day from 1985 to 2025. Version 0.1.0 finds a measurable but modest gap (+0.455°C, 95% CI [0.432, 0.478], excludes zero) and no statistically significant long-term trend over the 40-year record (p=0.118) — reported plainly rather than reworded into a more dramatic story. Includes an interactive station map computing the real haversine distance and bearing between the two stations from their actual coordinates, no basemap library required. [Source code](https://github.com/lindgreendavid/climate-twin-frankfurt) · [Research report](https://github.com/lindgreendavid/climate-twin-frankfurt/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Climate Data` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Neuro Signal Lab — inspect the EEG result](https://lindgreendavid.github.io/neuro-signal-lab/)

A reproducible cross-dataset test of a fixed P3b endpoint in public EEG data. The electrode, 300–600 ms window, target-minus-standard contrast, artifact threshold, participant-level inference, and stopping rule were frozen before the external amplitudes were inspected. All 13 OpenNeuro participants showed a positive contrast; the mean was +5.65 µV with a 95% confidence interval of [+4.83, +6.48]. The interactive laboratory exposes every participant and both prespecified artifact-threshold sensitivity analyses while keeping the confirmatory endpoint visibly fixed. [Source code](https://github.com/lindgreendavid/neuro-signal-lab) · [Research report](https://github.com/lindgreendavid/neuro-signal-lab/blob/main/docs/research-report.md)

`Python` · `EEG` · `Neuroscience` · `Statistical Inference` · `OpenNeuro` · `Scientific UI/UX`

### [Kryptographie WASM](https://github.com/lindgreendavid/kryptographie-wasm)

An interactive cryptography learning application whose cryptographic domain logic is implemented in Rust and delivered through WebAssembly. It combines mathematical explanation, typed error handling, official test vectors, browser tests, accessibility checks, and a documented security model.

`Rust` · `WebAssembly` · `Cryptography` · `Accessible Education`

## Portfolio roadmap

Full researched roadmap, including grounded data sources for every future entry: [ROADMAP.md](ROADMAP.md).

| Project | Question | Primary evidence | Status |
| --- | --- | --- | --- |
| [Lab Notes](https://blog-interactive.lindgreendavid.workers.dev/) | How can technical studies become an inspectable, reusable learning experience? | Verified project reports, article citations, interactive laboratories | Live and continuously expanding |
| Fairshift Lab | Does measured fairness remain stable under distribution shift, noise, and misspecification? | ML evaluation, causal clarity, research rigor | Shipped, v1.3.0 |
| [Climate Twin Frankfurt](https://climate-twin-frankfurt-interactive.lindgreendavid.workers.dev) | How much warmer is urban Frankfurt than its rural surroundings, with what uncertainty, and how has that gap trended over time? | Real paired urban/rural DWD Climate Data Center station records | Shipped, v0.1.0 |
| Mathlab WASM | How can numerical algorithms be made inspectable? | Mathematics, Rust/WASM, interactive teaching | Not yet scoped |
| [Data Contract Observatory](https://lindgreendavid.github.io/data-contract-observatory/) | When does a public-data response cease to satisfy its declared operational contract? | Official ECB SDMX series, machine-readable contract, TARGET calendar, synthetic mutation tests | **Public v0.1.0 foundation.** Protocol frozen, live evaluation and interactive failure laboratory shipped. [Source](https://github.com/lindgreendavid/data-contract-observatory) |

## Science communication & research track

A second track, editorially distinct from the responsible-AI/data-engineering work above. Every project belongs to the same Lab Notes identity system while retaining a field-specific accent and explanatory visual language. Same standard throughout: every piece states what it contributes, what it found, and what remains unresolved — not just an explanation of settled science. Two formats:

- **Explainer builds** — an interactive simulation, design, or animation of a real phenomenon currently being discussed or studied, with the underlying model and its limits made explicit.
- **Research notes** — a short, evidence-grounded, accessible thesis built on public data or literature, testing a specific claim rather than speculating.

| Project | Field | Open question | Status |
| --- | --- | --- | --- |
| [Three-Body Lab](https://three-body-lab-interactive.lindgreendavid.workers.dev) | Physics | Where does the planar three-body problem cross from quasi-periodic to chaotic, and do the classical special solutions sit at that boundary? | **Shipped — v0.1.0 live.** A single Lyapunov-exponent threshold didn't cleanly separate the tested grid, and the Lagrange/Euler special solutions measured *less* stable than generic configurations — consistent with Routh's 1875 instability criterion. |
| [FRB Atlas](https://frb-atlas-interactive.lindgreendavid.workers.dev) | Astrophysics | Using the real, public CHIME/FRB Catalog 1, do repeating and non-repeating fast radio bursts actually show indistinguishable dispersion measures, as the original catalog paper concludes? | **Shipped — v0.1.0 live.** Pulse-width/bandwidth differences replicated cleanly (validating the method); dispersion measure did not — a discrepancy traced to two repeaters dominating the sample, reported rather than hidden. |
| [Folding's Edge](https://foldings-edge-interactive.lindgreendavid.workers.dev) | Biology | Does AlphaFold2's pLDDT confidence score predict real, curated intrinsic disorder — and where does that relationship break down? | **Shipped — v0.1.0 live.** Confirms pLDDT as a strong overall disorder signal, but precision collapses specifically on conditionally-folding regions and HDX-MS-evidenced disorder — named failure cases, not just aggregate rates. |
| [Neuro Signal Lab](https://lindgreendavid.github.io/neuro-signal-lab/) | Neuroscience | Does a P3b target enhancement survive a fixed, independently applied EEG measurement? | **Research and interactive laboratory published.** All 13 OpenNeuro participants had a positive fixed Pz 300–600 ms target-minus-standard contrast; mean +5.65 µV, 95% CI [+4.83, +6.48]. [Source](https://github.com/lindgreendavid/neuro-signal-lab) |

All four studies in this track are shipped and collected in Lab Notes, including Neuro Signal Lab's
confirmed EEG result, interactive participant explorer, and sensitivity analysis. The chemistry
reproducibility candidate remains in [ROADMAP.md](ROADMAP.md) for a later wave.

## Engineering principles

1. **Research questions before dashboards.** Every analytical project begins with a falsifiable, bounded question, written down before any result exists.
2. **Evidence before claims.** Baselines, uncertainty, negative results, and limitations are first-class outputs — falsified hypotheses are reported, not quietly reframed.
3. **Sources are verified, not assumed.** Every citation and external claim is checked against a primary source before it ships — including in a published paper's own stated methodology, not just its abstract.
4. **Architecture proportional to the problem.** Clear modules and contracts matter; complexity without evidence does not.
5. **Reproducibility by default.** Locked dependencies, seeds, tests, CI, citation metadata, versioned releases, and — where the underlying data allows it — a fetch-at-build-time pipeline instead of committing raw third-party data.
6. **Responsible delivery.** Accessibility (WCAG AA, automatically checked), security, privacy, provenance, bias, and prohibited uses are documented for every release.

## Skills demonstrated

`Python` · `Rust` · `TypeScript` · `WebAssembly` · `Machine Learning` · `Statistics` · `Statistical Inference` · `Causal Reasoning` · `Data Analytics` · `Testing` · `CI/CD` · `Security` · `Accessibility (WCAG AA)` · `UI/UX` · `Technical Writing`

## Connect

Explore the repositories above or open a GitHub discussion on the relevant project. I am especially interested in work that connects rigorous quantitative methods with products people can understand and trust.
