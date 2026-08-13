# David Lindgreen

### Building trustworthy data products from mathematical foundations to accessible interfaces

I work at the intersection of **responsible AI**, **data science**, **mathematics**, **analytics engineering**, and **scientific UI/UX**. My projects emphasize explicit assumptions, reproducible experiments, strong software architecture, and honest limits—not just attractive outputs.

## Current focus

- Fairness and robustness under distribution shift
- Uncertainty-aware machine learning and model evaluation
- Explainable, accessible research interfaces
- Mathematical algorithms in Rust and WebAssembly
- Data quality, observability, and reproducible analytics
- Accessible science communication — physics, astrophysics, and biology, held to the same bar as the AI work: a bounded question, real evidence (public data where possible), and honest limits, not a hot take

## Featured work

### [Fairshift Lab — open the interactive laboratory](https://fairshift-lab.lindgreendavid.chatgpt.site)

A reproducible Responsible AI laboratory for exploring how distribution shift changes probability calibration, threshold-sensitive decisions, performance, and group-fairness measurements. Visitors can manipulate the population and decision threshold, compare source and target reliability, and inspect uncertainty without installing anything. Version 1.3.0 adds a Robustness Lab — a preregistered synthetic stress study comparing two model families under label noise, measurement error, an unobserved subgroup, and structural misspecification — on top of v1.1's Policy Studio and v1.2's governed external evidence from real 1994 Census data. [Source code](https://github.com/lindgreendavid/fairshift-lab) · [v1.3.0 release](https://github.com/lindgreendavid/fairshift-lab/releases/tag/v1.3.0)

`Python` · `TypeScript` · `Probability Calibration` · `Distribution Shift` · `Responsible AI` · `Scientific UI/UX`

### [FRB Atlas — open the interactive laboratory](https://frb-atlas-interactive.lindgreendavid.workers.dev)

A reproducible reanalysis of the real, public CHIME/FRB Catalog 1 (536 fast radio bursts, Amiri et al. 2021): does the dispersion measure of repeating bursts actually differ from non-repeating ones, as the original paper's own preregistered test claims it doesn't? Version 0.1.0 cleanly replicates the paper's pulse-width/bandwidth finding as a validation check, then reports a genuine discrepancy on dispersion measure — traced honestly to sample composition (two prolific nearby repeaters dominating the burst sample) rather than smoothed over. [Source code](https://github.com/lindgreendavid/frb-atlas) · [Research report](https://github.com/lindgreendavid/frb-atlas/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Astrophysics` · `Statistical Inference` · `Real Public Data` · `Scientific UI/UX`

### [Three-Body Lab — open the interactive laboratory](https://three-body-lab-interactive.lindgreendavid.workers.dev)

A reproducible computational-physics laboratory mapping the boundary between quasi-periodic and chaotic motion in the planar gravitational three-body problem, via empirically estimated Lyapunov exponents. Visitors can watch a reference trajectory and a near-identical perturbed twin diverge in real time, export a clip of the divergence, and inspect a frozen, preregistered sweep that tests the figure-eight, Lagrange equilateral, and Euler collinear special solutions against that boundary. Version 0.1.0 does not claim to solve the three-body problem — it reports what a disclosed numerical method actually finds, including two hypotheses it falsified. [Source code](https://github.com/lindgreendavid/three-body-lab) · [Research report](https://github.com/lindgreendavid/three-body-lab/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Computational Physics` · `Chaos Theory` · `Numerical Integration` · `Scientific UI/UX`

### [Kryptographie WASM](https://github.com/lindgreendavid/kryptographie-wasm)

An interactive cryptography learning application whose cryptographic domain logic is implemented in Rust and delivered through WebAssembly. It combines mathematical explanation, typed error handling, official test vectors, browser tests, accessibility checks, and a documented security model.

`Rust` · `WebAssembly` · `Cryptography` · `Accessible Education`

## Portfolio roadmap

| Project | Question | Primary evidence |
| --- | --- | --- |
| Fairshift Lab | Does measured fairness remain stable under distribution shift, noise, and misspecification? | ML evaluation, causal clarity, research rigor |
| Climate Twin Frankfurt | How can local heat risk be communicated with uncertainty? | Time series, geospatial data, scientific UX |
| Mathlab WASM | How can numerical algorithms be made inspectable? | Mathematics, Rust/WASM, interactive teaching |
| Data Contract Observatory | When do public-data pipelines silently become unreliable? | Data engineering, observability, drift detection |

## Science communication & research track

A second track, kept visually and editorially separate from the responsible-AI/data-engineering work above — each project gets its own distinct visual identity rather than a reskin of the last one. Same standard throughout: every piece states what it contributes, what it found, and what remains unresolved — not just an explanation of settled science. Two formats:

- **Explainer builds** — an interactive simulation, design, or animation of a real phenomenon currently being discussed or studied, with the underlying model and its limits made explicit.
- **Research notes** — a short, evidence-grounded, accessible thesis built on public data or literature, testing a specific claim rather than speculating.

| Project | Field | Open question | Status |
| --- | --- | --- | --- |
| [Three-Body Lab](https://three-body-lab-interactive.lindgreendavid.workers.dev) | Physics | Where does the planar three-body problem cross from quasi-periodic to chaotic, and do the classical special solutions sit at that boundary? | **Shipped — v0.1.0 live.** A single Lyapunov-exponent threshold didn't cleanly separate the tested grid, and the Lagrange/Euler special solutions measured *less* stable than generic configurations — consistent with Routh's 1875 instability criterion. |
| [FRB Atlas](https://frb-atlas-interactive.lindgreendavid.workers.dev) | Astrophysics | Using the real, public CHIME/FRB Catalog 1, do repeating and non-repeating fast radio bursts actually show indistinguishable dispersion measures, as the original catalog paper concludes? | **Shipped — v0.1.0 live.** Pulse-width/bandwidth differences replicated cleanly (validating the method); dispersion measure did not — a discrepancy traced to two repeaters dominating the sample, reported rather than hidden. |
| Folding's Edge | Biology | Where does AlphaFold-class structure prediction break down (e.g. intrinsically disordered regions), and why? | Proposed — next up for scoping. Needs heavier ML infrastructure than the first two, so it's being scoped carefully rather than rushed. |

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
