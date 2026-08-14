# Roadmap

A living, researched plan for what gets built next across both tracks of this portfolio — the
responsible-AI/data-engineering track and the science communication & research track. Every entry
here was checked against a real, currently-accessible data source or literature finding before
being listed; nothing here is a vague aspiration. Updated 2026-08-14.

The long-term goal is a **deliberate mix**: this portfolio should not drift into being "the physics
one" or "the AI one" — each wave of building should keep both tracks moving.

## In progress

| Project | Track | Status |
| --- | --- | --- |
| [Lab Notes](https://blog-interactive.lindgreendavid.workers.dev/) | Science communication / portfolio infrastructure | Live and continuously expanding with project articles, an evidence explorer, a study guide, an accessibility contract, and CI. |
| [Data Contract Observatory](https://lindgreendavid.github.io/data-contract-observatory/) | AI / data engineering | Product v1.0.0: append-only prospective evidence now runs beside the frozen fault suite and current-vintage replay. One real prospective run exists; longitudinal evidence is accumulating. |
| [Reaction Integrity Lab](https://lindgreendavid.github.io/reaction-integrity-lab/) | Science (computational chemistry / ML) | Research product v0.1.0: primary sources, data identities, checksums, official logs, and the released-data exact split audit are complete; independent model-score reproduction is next. |

## Shipped in the current wave

| Project | Track | Result |
| --- | --- | --- |
| [Folding's Edge](https://foldings-edge-interactive.lindgreendavid.workers.dev) | Science (biology) | Product v1.0.0; unchanged frozen v0.1 study, real-data pLDDT chain animation and threshold explorer. |
| [Climate Twin Frankfurt](https://climate-twin-frankfurt-interactive.lindgreendavid.workers.dev) | AI / data engineering | Product v1.0.0; unchanged frozen v0.1 study of 14,579 paired DWD days. |
| [FRB Atlas](https://frb-atlas-interactive.lindgreendavid.workers.dev) | Science (astrophysics) | Product v1.0.0; unchanged frozen v0.1 catalog analysis and documented partial replication. |
| [Three-Body Lab](https://three-body-lab-interactive.lindgreendavid.workers.dev) | Science (physics) | Product v1.0.0; unchanged frozen v0.1 42-cell Lyapunov sweep. |
| [Fairshift Lab](https://fairshift-lab.lindgreendavid.chatgpt.site) | Responsible AI | v1.3.0 live, including governed external evidence, policy analysis, and robustness stress tests. |
| [Neuro Signal Lab](https://lindgreendavid.github.io/neuro-signal-lab/) | Neuroscience | Product v1.0.0; frozen endpoint and result, with all 13 participant contrasts positive. |
| [Data Contract Observatory](https://lindgreendavid.github.io/data-contract-observatory/) | AI / data engineering | Product v1.0.0; one prospective run, 7,010 current-vintage replay prefixes, and nine controlled faults. |

## Next up — AI / data engineering track

### Mathlab WASM

**Question:** How can numerical algorithms be made inspectable rather than opaque?

An interactive mathematics teaching tool in Rust/WebAssembly, in the spirit of Kryptographie WASM
but for numerical methods (root-finding, linear solvers, optimization) — visualizing convergence,
failure modes, and numerical error rather than just producing an answer. Needs a specific
algorithm-set scope decided before building; not yet started.

### Data Contract Observatory

**Question:** When do public-data pipelines silently become unreliable?

**Status:** product v1.0.0 implemented. The selected source is the official ECB daily
US dollar/euro reference-rate series `EXR.D.USD.EUR.SP00.A`, accessed through the ECB Data Portal's
SDMX API. Protocol 1.0.0 separates hard consumer-contract failures from a conservative statistical
review signal; an unusual movement is never labelled a source error by the detector alone. The
first frozen-protocol evaluation inspected 385 observations, passed every hard check, and emitted
no review signal. The frozen nine-fault suite classified every controlled fault as expected; its
single clean control emitted no false alert. A 7,010-prefix replay is explicitly labelled as one
current historical vintage, not past revision evidence.

**Next evidence step:** accumulate auditable scheduled runs in the append-only `evidence` branch.
Revision comparison, source hashes, normalized state and the versioned fault suite are now in
place. A later results release remains review-gated and must not claim a longitudinal rate until
enough real runs exist.

## Next up — science communication & research track

The first six v1 research products are shipped. The next science wave is now active in
computational chemistry.

### A neuroscience replication (field: neuroscience)

**Selected question:** does ERP CORE's fixed P3b endpoint — target-minus-standard mean voltage at Pz
from 300–600 ms — remain positive in an independently hosted public auditory-oddball EEG dataset?

**Status:** the primary-source pass, metadata-only audit, frozen protocol, and confirmatory analysis
are complete in the public [Neuro Signal Lab](https://github.com/lindgreendavid/neuro-signal-lab)
repository. Using OpenNeuro `ds003061` v1.1.0, the mean
participant contrast was +5.65 µV, 95% CI [+4.83, +6.48], and all 13 participant contrasts were
positive. This is a cross-paradigm robustness confirmation, not a literal direct replication,
because ERP CORE used a visual task and the external dataset used an auditory task. The public
interactive laboratory and v1.0.0 research product are live.

**Why this is tractable:** [OpenNeuro](https://openneuro.org) is a real, actively maintained,
BIDS-standardized open archive of 600+ neuroimaging datasets (fMRI, EEG, MEG) covering 20,000+
participants, backed by a peer-reviewed infrastructure paper (Markiewicz et al. 2021, *eLife*,
"The OpenNeuro resource for sharing of neuroscience data" — cite and verify this paper's exact
claims before building, the same discipline used for every other project in this series). The
selected endpoint came from Kappenman et al.'s ERP CORE recommendations and was fixed before
external EEG amplitudes were inspected. Raw data stay outside Git, included recordings are verified
against pinned DataLad identities, and one truncated run is disclosed rather than silently replaced.

### Reaction Integrity Lab (field: computational chemistry / machine learning)

**Selected question:** do ORDerly's four published reaction-condition benchmark comparisons survive
an exact reproduction across role assignment and rare-condition policy?

**Status:** the public [interactive laboratory](https://lindgreendavid.github.io/reaction-integrity-lab/)
and [source repository](https://github.com/lindgreendavid/reaction-integrity-lab) have completed the
primary-source, provenance, licensing, endpoint, official-log, and first
released-data split audit. Both official version-4 Parquet files match their Figshare MD5 checksums.
They contain 625,697 training and 65,445 test rows—691,142 total, matching the final official log
count. The declared reactant/product key has zero exact train/test collisions, and the full declared
record has zero exact cross-split duplicates.

**Evidence boundary:** those findings establish exact identity separation in the released split.
They do not exclude chemical-similarity, patent-family, or temporal leakage. The published top-3
accuracy cells—31/44%, 33/47%, 4/21%, and 5/24% for baseline/model—remain reference values, not
independently reproduced results.

**Next evidence step:** execute the frozen four-cell baseline and model reproduction, record seed
variation, and evaluate whether each published value falls within the prespecified ±1
percentage-point verification rule. Then add chemistry-similarity and provenance-aware sensitivity
audits without rewriting the primary endpoint.

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
