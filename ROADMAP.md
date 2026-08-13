# Roadmap

A living, researched plan for what gets built next across both tracks of this portfolio — the
responsible-AI/data-engineering track and the science communication & research track. Every entry
here was checked against a real, currently-accessible data source or literature finding before
being listed; nothing here is a vague aspiration. Updated 2026-08-13.

The long-term goal is a **deliberate mix**: this portfolio should not drift into being "the physics
one" or "the AI one" — each wave of building should keep both tracks moving.

## In progress

| Project | Track | Status |
| --- | --- | --- |
| [Lab Notes](https://blog-interactive.lindgreendavid.workers.dev/) | Science communication / portfolio infrastructure | Live and continuously expanding with project articles, an evidence explorer, a study guide, an accessibility contract, and CI. |
| Next research selection | Science research | Run a full primary-source research pass on the neuroscience and chemistry candidates below, then select one bounded replication question before writing any protocol. |

## Shipped in the current wave

| Project | Track | Result |
| --- | --- | --- |
| [Folding's Edge](https://foldings-edge-interactive.lindgreendavid.workers.dev) | Science (biology) | v0.1.0 live, including its real-data pLDDT chain animation and interactive threshold explorer. |
| [Climate Twin Frankfurt](https://climate-twin-frankfurt-interactive.lindgreendavid.workers.dev) | AI / data engineering | v0.1.0 live, based on 40 years of paired DWD station records with uncertainty, provenance, and an interactive station map. |
| [FRB Atlas](https://frb-atlas-interactive.lindgreendavid.workers.dev) | Science (astrophysics) | v0.1.0 live, including a documented partial replication and sample-composition sensitivity finding. |
| [Three-Body Lab](https://three-body-lab-interactive.lindgreendavid.workers.dev) | Science (physics) | v0.1.0 live, with a validated simulator, perturbed-twin comparison, and frozen Lyapunov sweep. |
| [Fairshift Lab](https://fairshift-lab.lindgreendavid.chatgpt.site) | Responsible AI | v1.3.0 live, including governed external evidence, policy analysis, and robustness stress tests. |

## Next up — AI / data engineering track

### Mathlab WASM

**Question:** How can numerical algorithms be made inspectable rather than opaque?

An interactive mathematics teaching tool in Rust/WebAssembly, in the spirit of Kryptographie WASM
but for numerical methods (root-finding, linear solvers, optimization) — visualizing convergence,
failure modes, and numerical error rather than just producing an answer. Needs a specific
algorithm-set scope decided before building; not yet started.

### Data Contract Observatory

**Question:** When do public-data pipelines silently become unreliable?

An observability tool that ingests a real public dataset on a schedule and flags schema drift,
distributional drift, and silent breakage — a genuine data-engineering problem, demonstrated on a
real, regularly-updated public data source (a government open-data portal or similar) rather than
a synthetic pipeline. Needs a specific target data source chosen before building; not yet started.

## Next up — science communication & research track

The first three ideas (Three-Body Lab, FRB Atlas, Folding's Edge) are shipped. Two grounded
candidates for the next wave, in fields not yet covered by this track:

### A neuroscience replication (field: neuroscience)

**Candidate question:** does a specific, well-cited neuroimaging finding replicate on a fresh,
independently-drawn sample from public data?

**Why this is tractable:** [OpenNeuro](https://openneuro.org) is a real, actively maintained,
BIDS-standardized open archive of 600+ neuroimaging datasets (fMRI, EEG, MEG) covering 20,000+
participants, backed by a peer-reviewed infrastructure paper (Markiewicz et al. 2021, *eLife*,
"The OpenNeuro resource for sharing of neuroscience data" — cite and verify this paper's exact
claims before building, the same discipline used for every other project in this series). This
would need a specific, narrow, well-defined published finding chosen as the replication target
before any protocol is written — the same way Folding's Edge picked one specific paper (Alderson
et al. 2023) rather than "neuroscience" in general.

### A chemistry reproducibility check (field: chemistry)

**Candidate question:** does a published reaction-prediction benchmark result hold up under a
disclosed, careful data-cleaning pass, or does it depend on a data-quality artifact?

**Why this is tractable:** the [Open Reaction Database](https://open-reaction-database.org) and
the ORDerly benchmark tooling (Wigh et al., published in *J. Chem. Inf. Model.*, PMC11094788) are
real, open, and explicitly built around a known, disclosed problem in this literature: reaction
datasets commonly overinflate reported model performance due to cleaning/leakage issues that
aren't always published. This is a strong fit for this portfolio's standing bias toward "test
whether the claimed result actually holds up," matching what FRB Atlas and Folding's Edge already
did in their own fields.

Both of these need a full research pass (like the one that grounded FRB Atlas's exact dataset and
citation before that project was scoped) before a protocol is written — this roadmap entry is the
starting point for that research, not a substitute for it.

## Longer-horizon / not yet scoped

Ideas noted for future consideration, not yet researched to the standard this portfolio requires
before building:

- **Climate science, standalone from Climate Twin Frankfurt** — Climate Twin is scoped as an
  AI/data-engineering project (station-pair observability and uncertainty communication); a
  distinct climate-*science* research-track entry (e.g., testing a specific published claim about
  regional warming trends against reanalysis data such as Copernicus ERA5) could exist separately
  later without duplicating Climate Twin's scope.
- Further science-track fields not yet touched at all: geology/earth science, ecology,
  linguistics/NLP-as-science. No specific dataset or claim has been vetted for any of these yet —
  they are placeholders for future research passes, not commitments.
