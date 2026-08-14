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
- Accessible science communication — physics, astrophysics, biology, chemistry, and neuroscience, held to the same bar as the AI work: a bounded question, real evidence (public data where possible), and honest limits, not a hot take

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
US dollar/euro reference-rate series. Product v1.0.0 separates one prospective live run, a
7,010-prefix replay of the current historical vintage, and a nine-fault synthetic suite. The
append-only `evidence` branch now records source hashes, normalized state and revisions between
future runs. At release there is one real prospective run, not longitudinal evidence.
[Source code](https://github.com/lindgreendavid/data-contract-observatory) · [v1.0.0 release](https://github.com/lindgreendavid/data-contract-observatory/releases/tag/v1.0.0)

`Python` · `Data Contracts` · `Observability` · `SDMX` · `Public Data` · `Scientific UI/UX`

### [FRB Atlas — open the interactive laboratory](https://frb-atlas-interactive.lindgreendavid.workers.dev)

A reproducible reanalysis of the real, public CHIME/FRB Catalog 1 (536 fast radio bursts, Amiri et al. 2021): does the dispersion measure of repeating bursts actually differ from non-repeating ones, as the original paper's own preregistered test claims it doesn't? The frozen v0.1 study cleanly replicates the paper's pulse-width/bandwidth finding as a validation check, then reports a genuine discrepancy on dispersion measure — traced honestly to sample composition (two prolific nearby repeaters dominating the burst sample) rather than smoothed over. Product v1.0.0 preserves this study. [Source code](https://github.com/lindgreendavid/frb-atlas) · [v1.0.0 release](https://github.com/lindgreendavid/frb-atlas/releases/tag/v1.0.0)

`Python` · `TypeScript` · `Astrophysics` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Folding's Edge — open the interactive laboratory](https://foldings-edge-interactive.lindgreendavid.workers.dev)

A reproducible test of how well AlphaFold2's per-residue confidence score (pLDDT) predicts real, curated intrinsic disorder. 387 human proteins from DisProt (228,662 residues) joined to real AlphaFold DB predictions by UniProt accession — no model training, just a fresh statistical test of a specific published claim (Alderson et al. 2023, PNAS). The frozen v0.1 study confirms pLDDT is a strong overall signal (43-point median gap, p≈0) but names exactly where it fails: precision collapses on regions that can conditionally fold (6.3% vs. 31% baseline) and on disorder evidenced by HDX-MS, with specific proteins named rather than only aggregate rates. Its hero animation traces one of those named proteins' real per-residue pLDDT values as a wiggling chain, and an interactive threshold explorer lets you drag the pLDDT cutoff and watch precision/recall/F1/MCC update live from the real data, with one click back to the actual preregistered threshold. Product v1.0.0 preserves this study. [Source code](https://github.com/lindgreendavid/foldings-edge) · [v1.0.0 release](https://github.com/lindgreendavid/foldings-edge/releases/tag/v1.0.0)

`Python` · `TypeScript` · `Structural Biology` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Three-Body Lab — open the interactive laboratory](https://three-body-lab-interactive.lindgreendavid.workers.dev)

A reproducible computational-physics laboratory mapping the boundary between quasi-periodic and chaotic motion in the planar gravitational three-body problem, via empirically estimated Lyapunov exponents. Visitors can watch a reference trajectory and a near-identical perturbed twin diverge in real time, export a clip of the divergence, and inspect a frozen, preregistered sweep that tests the figure-eight, Lagrange equilateral, and Euler collinear special solutions against that boundary. The frozen v0.1 study does not claim to solve the three-body problem — it reports what a disclosed numerical method actually finds, including two hypotheses it falsified. Product v1.0.0 preserves this study. [Source code](https://github.com/lindgreendavid/three-body-lab) · [v1.0.0 release](https://github.com/lindgreendavid/three-body-lab/releases/tag/v1.0.0)

`Python` · `TypeScript` · `Computational Physics` · `Chaos Theory` · `Numerical Integration` · `Scientific UI/UX`

### [Climate Twin Frankfurt — open the interactive laboratory](https://climate-twin-frankfurt-interactive.lindgreendavid.workers.dev)

A reproducible measurement of Frankfurt's urban heat island from real DWD station records: the inner-city Frankfurt/Main-Westend station against Frankfurt/Main — DWD's own designated reference counterpart (physically the airport, disclosed rather than glossed over) — across every valid paired day from 1985 to 2025. The frozen v0.1 study finds a measurable but modest gap (+0.455°C, 95% CI [0.432, 0.478], excludes zero) and no statistically significant long-term trend over the 40-year record (p=0.118) — reported plainly rather than reworded into a more dramatic story. Includes an interactive station map computing the real haversine distance and bearing between the two stations from their actual coordinates, no basemap library required. Product v1.0.0 preserves this study. [Source code](https://github.com/lindgreendavid/climate-twin-frankfurt) · [v1.0.0 release](https://github.com/lindgreendavid/climate-twin-frankfurt/releases/tag/v1.0.0)

`Python` · `TypeScript` · `Climate Data` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Neuro Signal Lab — inspect the EEG result](https://lindgreendavid.github.io/neuro-signal-lab/)

A reproducible cross-dataset test of a fixed P3b endpoint in public EEG data. The electrode, 300–600 ms window, target-minus-standard contrast, artifact threshold, participant-level inference, and stopping rule were frozen before the external amplitudes were inspected. All 13 OpenNeuro participants showed a positive contrast; the mean was +5.65 µV with a 95% confidence interval of [+4.83, +6.48]. The interactive laboratory exposes every participant and both prespecified artifact-threshold sensitivity analyses while keeping the confirmatory endpoint visibly fixed. Product v1.0.0 stabilizes the research product without changing the frozen endpoint or result. [Source code](https://github.com/lindgreendavid/neuro-signal-lab) · [v1.0.0 release](https://github.com/lindgreendavid/neuro-signal-lab/releases/tag/v1.0.0)

`Python` · `EEG` · `Neuroscience` · `Statistical Inference` · `OpenNeuro` · `Scientific UI/UX`

### [Reaction Integrity Lab — inspect the benchmark](https://lindgreendavid.github.io/reaction-integrity-lab/)

A transparent known-result reproduction of ORDerly's reaction-condition benchmark. Research
product v1.0.0 verifies the primary paper, both versioned Figshare sources, official cleaning logs,
and the complete four-variant archive. All four frequency baselines reproduce within 0.46
percentage points of the final peer-reviewed values. An exact audit of 691,142 released reactions finds zero
train/test collisions on the declared reactant/product input key and zero exact full-record
duplicates across the split. The prespecified v1 audit finds 5.78% canonical product overlap,
80.84% nonempty product-scaffold overlap, and 60.5% sampled maximum product similarity ≥0.70.
Neural-model scores remain published references because exact checkpoint/prediction bundles are not
in the versioned public release; product overlap is not proof of patent-family leakage or wet-lab failure.
[Source code](https://github.com/lindgreendavid/reaction-integrity-lab) · [Lab Notes article](https://blog-interactive.lindgreendavid.workers.dev/posts/reaction-integrity-lab-cleaning-leakage) · [Research report](https://github.com/lindgreendavid/reaction-integrity-lab/blob/main/docs/research-report.md)

`Python` · `Computational Chemistry` · `Machine Learning` · `Data Provenance` · `Reproducibility` · `Scientific UI/UX`

### [Mathlab WASM — inspect root finding](https://lindgreendavid.github.io/mathlab-wasm/)

An interactive Rust/WebAssembly laboratory for understanding what bisection, Newton, secant, and a
Brent–Dekker-style safeguarded hybrid actually certify. Product v0.2.0 adds five prespecified cases
to the unchanged seven-case v0.1 foundation. The skewed `x¹⁰−1` trace exposes accepted secant,
inverse-quadratic, and bisection moves while retaining a sign-changing bracket. All frozen outcomes
pass; the audit also reports and bounds a last-bit macOS/Ubuntu cosine difference instead of hiding
it. The selected teaching suites are not a representative benchmark or production-library
equivalence test. [Source code](https://github.com/lindgreendavid/mathlab-wasm) · [Lab Notes article](https://blog-interactive.lindgreendavid.workers.dev/posts/mathlab-wasm-root-finding) · [Research report](https://github.com/lindgreendavid/mathlab-wasm/blob/main/docs/research-report.md)

`Rust` · `WebAssembly` · `Numerical Analysis` · `Scientific Computing` · `Accessibility` · `Interactive Learning`

### [Kryptographie WASM](https://github.com/lindgreendavid/kryptographie-wasm)

An interactive cryptography learning application whose cryptographic domain logic is implemented in Rust and delivered through WebAssembly. It combines mathematical explanation, typed error handling, official test vectors, browser tests, accessibility checks, and a documented security model.

`Rust` · `WebAssembly` · `Cryptography` · `Accessible Education`

## Portfolio roadmap

Full researched roadmap, including grounded data sources for every future entry: [ROADMAP.md](ROADMAP.md).

| Project | Question | Primary evidence | Status |
| --- | --- | --- | --- |
| [Lab Notes](https://blog-interactive.lindgreendavid.workers.dev/) | How can technical studies become an inspectable, reusable learning experience? | Verified project reports, article citations, interactive laboratories | Live and continuously expanding |
| Fairshift Lab | Does measured fairness remain stable under distribution shift, noise, and misspecification? | ML evaluation, causal clarity, research rigor | Shipped, v1.3.0 |
| [Climate Twin Frankfurt](https://climate-twin-frankfurt-interactive.lindgreendavid.workers.dev) | How much warmer is urban Frankfurt than its rural surroundings, with what uncertainty, and how has that gap trended over time? | Real paired urban/rural DWD Climate Data Center station records | Product v1.0.0; frozen study v0.1 |
| [Mathlab WASM](https://lindgreendavid.github.io/mathlab-wasm/) | Which root-finding guarantees and failures remain visible under shared numerical rules? | NIST DLMF, Brent (1971), twelve versioned Rust/WASM traces | **Product v0.2.0.** Safeguarded interpolation and explicit bisection fallback shipped. [Release](https://github.com/lindgreendavid/mathlab-wasm/releases/tag/v0.2.0) |
| [Data Contract Observatory](https://lindgreendavid.github.io/data-contract-observatory/) | When does a public-data response cease to satisfy its declared operational contract? | Official ECB SDMX series, prospective ledger, retrospective replay, synthetic fault suite | **Product v1.0.0.** One prospective run; longitudinal evidence is beginning. [Release](https://github.com/lindgreendavid/data-contract-observatory/releases/tag/v1.0.0) |
| [Reaction Integrity Lab](https://lindgreendavid.github.io/reaction-integrity-lab/) | Do ORDerly's published reaction-condition results survive an exact reproduction? | Primary paper, complete checksum-verified archive, reproduced baselines and prespecified similarity audit | **Product v1.0.0.** Stable audited result; neural-model cells remain published references. |

## Science communication & research track

A second track, editorially distinct from the responsible-AI/data-engineering work above. Every project belongs to the same Lab Notes identity system while retaining a field-specific accent and explanatory visual language. Same standard throughout: every piece states what it contributes, what it found, and what remains unresolved — not just an explanation of settled science. Two formats:

- **Explainer builds** — an interactive simulation, design, or animation of a real phenomenon currently being discussed or studied, with the underlying model and its limits made explicit.
- **Research notes** — a short, evidence-grounded, accessible thesis built on public data or literature, testing a specific claim rather than speculating.

| Project | Field | Open question | Status |
| --- | --- | --- | --- |
| [Three-Body Lab](https://three-body-lab-interactive.lindgreendavid.workers.dev) | Physics | Where does finite-time divergence appear under the frozen numerical method? | **Product v1.0.0; frozen study v0.1.** [Release](https://github.com/lindgreendavid/three-body-lab/releases/tag/v1.0.0) |
| [FRB Atlas](https://frb-atlas-interactive.lindgreendavid.workers.dev) | Astrophysics | Which CHIME/FRB Catalog 1 comparisons replicate under the frozen analysis? | **Product v1.0.0; frozen study v0.1.** [Release](https://github.com/lindgreendavid/frb-atlas/releases/tag/v1.0.0) |
| [Folding's Edge](https://foldings-edge-interactive.lindgreendavid.workers.dev) | Biology | When does AlphaFold confidence predict curated disorder? | **Product v1.0.0; frozen study v0.1.** [Release](https://github.com/lindgreendavid/foldings-edge/releases/tag/v1.0.0) |
| [Neuro Signal Lab](https://lindgreendavid.github.io/neuro-signal-lab/) | Neuroscience | Does a fixed P3b target enhancement survive an independent auditory dataset? | **Product v1.0.0; frozen endpoint and result.** [Release](https://github.com/lindgreendavid/neuro-signal-lab/releases/tag/v1.0.0) |
| [Reaction Integrity Lab](https://lindgreendavid.github.io/reaction-integrity-lab/) | Computational chemistry / ML | Does ORDerly's published condition-prediction gap survive an exact reproduction? | **Product v1.0.0.** Four baselines and prespecified similarity/provenance audit complete; neural-model artifacts remain unavailable. |

The four stable studies and the new chemistry reproduction are collected in Lab Notes. Reaction
Integrity Lab's source and released-data audits are public; its model-score reproduction remains
open and is stated as such throughout the repository, live laboratory, and article.

## Engineering principles

1. **Research questions before dashboards.** Every analytical project begins with a falsifiable, bounded question and a protocol appropriate to its design. Known-result reproductions are labelled explicitly rather than presented as blinded or preregistered work.
2. **Evidence before claims.** Baselines, uncertainty, negative results, and limitations are first-class outputs — falsified hypotheses are reported, not quietly reframed.
3. **Sources are verified, not assumed.** Every citation and external claim is checked against a primary source before it ships — including in a published paper's own stated methodology, not just its abstract.
4. **Architecture proportional to the problem.** Clear modules and contracts matter; complexity without evidence does not.
5. **Reproducibility by default.** Locked dependencies, seeds, tests, CI, citation metadata, versioned releases, and — where the underlying data allows it — a fetch-at-build-time pipeline instead of committing raw third-party data.
6. **Responsible delivery.** Accessibility (WCAG AA, automatically checked), security, privacy, provenance, bias, and prohibited uses are documented for every release.

## Skills demonstrated

`Python` · `Rust` · `TypeScript` · `WebAssembly` · `Machine Learning` · `Statistics` · `Statistical Inference` · `Causal Reasoning` · `Data Analytics` · `Testing` · `CI/CD` · `Security` · `Accessibility (WCAG AA)` · `UI/UX` · `Technical Writing`

## Connect

Explore the repositories above or open a GitHub discussion on the relevant project. I am especially interested in work that connects rigorous quantitative methods with products people can understand and trust.
