# David Lindgreen

### Building trustworthy data products from mathematical foundations to accessible interfaces

I work at the intersection of **responsible AI**, **data science**, **mathematics**, **analytics engineering**, and **scientific UI/UX**. My projects emphasize explicit assumptions, reproducible experiments, strong software architecture, and honest limits—not just attractive outputs.

## Current focus

- Fairness and robustness under distribution shift
- Uncertainty-aware machine learning and model evaluation
- Explainable, accessible research interfaces
- Mathematical algorithms in Rust and WebAssembly
- Data quality, observability, and reproducible analytics
- Accessible science communication: physics, astrophysics, and biology, built the same way — a bounded question, real evidence, and honest limits, not a hot take

## Featured work

### [Fairshift Lab — open the interactive laboratory](https://fairshift-lab.lindgreendavid.chatgpt.site)

A reproducible Responsible AI laboratory for exploring how distribution shift changes probability calibration, threshold-sensitive decisions, performance, and group-fairness measurements. Visitors can manipulate the population and decision threshold, compare source and target reliability, and inspect uncertainty without installing anything. Version 0.3.1 separates training, calibration, and evaluation data while keeping interpretation limits visible. [Source code](https://github.com/lindgreendavid/fairshift-lab) · [v0.3.1 release](https://github.com/lindgreendavid/fairshift-lab/releases/tag/v0.3.1)

`Python` · `TypeScript` · `Probability Calibration` · `Threshold Sensitivity` · `Responsible AI` · `Scientific UI/UX`

### [Three-Body Lab — open the interactive laboratory](https://three-body-lab-interactive.lindgreendavid.workers.dev)

A reproducible computational-physics laboratory mapping the boundary between quasi-periodic and chaotic motion in the planar gravitational three-body problem, via empirically estimated Lyapunov exponents. Visitors can watch a reference trajectory and a near-identical perturbed twin diverge in real time, and inspect a frozen, preregistered sweep that tests the figure-eight, Lagrange equilateral, and Euler collinear special solutions against that boundary. Version 0.1.0 does not claim to solve the three-body problem — it reports what a disclosed numerical method actually finds, including two hypotheses it falsified. [Source code](https://github.com/lindgreendavid/three-body-lab) · [Research report](https://github.com/lindgreendavid/three-body-lab/blob/main/docs/research-report.md)

`Python` · `TypeScript` · `Computational Physics` · `Chaos Theory` · `Numerical Integration` · `Scientific UI/UX`

### [Kryptographie WASM](https://github.com/lindgreendavid/kryptographie-wasm)

An interactive cryptography learning application whose cryptographic domain logic is implemented in Rust and delivered through WebAssembly. It combines mathematical explanation, typed error handling, official test vectors, browser tests, accessibility checks, and a documented security model.

`Rust` · `WebAssembly` · `Cryptography` · `Accessible Education`

## Portfolio roadmap

| Project | Question | Primary evidence |
| --- | --- | --- |
| Fairshift Lab | Does measured fairness remain stable under distribution shift? | ML evaluation, causal clarity, research rigor |
| Climate Twin Frankfurt | How can local heat risk be communicated with uncertainty? | Time series, geospatial data, scientific UX |
| Mathlab WASM | How can numerical algorithms be made inspectable? | Mathematics, Rust/WASM, interactive teaching |
| Data Contract Observatory | When do public-data pipelines silently become unreliable? | Data engineering, observability, drift detection |

## Science communication & research track

A second track, kept visually and editorially separate from the responsible-AI/data-engineering work above. Same standard: every piece states what it contributes, what it found, and what remains unresolved — not just an explanation of settled science. Two formats:

- **Explainer builds** — an interactive simulation, design, or animation of a real phenomenon currently being discussed or studied, with the underlying model and its limits made explicit.
- **Research notes** — a short, evidence-grounded, accessible thesis on a genuinely unsolved or open problem, built on public data or literature rather than speculation.

| Project | Field | Open question | Status |
| --- | --- | --- | --- |
| [Three-Body Lab](https://three-body-lab-interactive.lindgreendavid.workers.dev) | Physics | Where does the planar three-body problem cross from quasi-periodic to chaotic, and do the classical special solutions sit at that boundary? | **Shipped — v0.1.0 live.** Headline finding: a single Lyapunov-exponent threshold didn't cleanly separate the tested grid, and the Lagrange/Euler special solutions measured *less* stable than generic configurations — consistent with Routh's classical instability criterion. |
| Fast Radio Burst Atlas | Astrophysics | What do public FRB catalogs (e.g. CHIME/FRB) actually support about progenitor theories, and what's still genuinely open? | Proposed — real catalog data analysis, reproducible statistical findings, an honest summary of what the data does and doesn't settle |
| Folding's Edge | Biology | Where does AlphaFold-class structure prediction break down (e.g. intrinsically disordered regions), and why? | Proposed — analysis against public structure data, accessible thesis on the boundary of current protein-structure prediction |

Status: first project shipped (Three-Body Lab, v0.1.0); Fast Radio Burst Atlas and Folding's Edge are next up for scoping.

## Engineering principles

1. **Research questions before dashboards.** Every analytical project begins with a falsifiable, bounded question.
2. **Evidence before claims.** Baselines, uncertainty, negative results, and limitations are first-class outputs.
3. **Architecture proportional to the problem.** Clear modules and contracts matter; complexity without evidence does not.
4. **Reproducibility by default.** Locked dependencies, seeds, tests, CI, citation metadata, and versioned releases.
5. **Responsible delivery.** Accessibility, security, privacy, provenance, bias, and prohibited uses are documented.

## Skills demonstrated

`Python` · `Rust` · `WebAssembly` · `Machine Learning` · `Statistics` · `Causal Reasoning` · `Data Analytics` · `Testing` · `CI/CD` · `Security` · `UI/UX` · `Technical Writing`

## Connect

Explore the repositories above or open a GitHub discussion on the relevant project. I am especially interested in work that connects rigorous quantitative methods with products people can understand and trust.
