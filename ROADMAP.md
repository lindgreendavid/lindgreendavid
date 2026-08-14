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
| [Reaction Integrity Lab](https://lindgreendavid.github.io/reaction-integrity-lab/) | Science (computational chemistry / ML) | Product v1.0.0: all four baselines, exact split, product identity, scaffold, provenance, date, and sampled similarity audits complete. |
| [Mathlab WASM](https://lindgreendavid.github.io/mathlab-wasm/) | Mathematics / scientific computing | Product v1.0.0: seventeen versioned cases across solver, safeguard, and conditioning protocols; all frozen gates pass. |
| [Snowflake Evolution Lab](https://lindgreendavid.github.io/snowflake-evolution-lab/) | Science (experimental evolution / multicellularity) | Product v0.1.0: frozen five-line reanalysis and interactive explainer shipped; combined genomic–mechanical validation is the next evidence gate. |

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
| [Jovian Resonance Lab](https://lindgreendavid.github.io/jovian-resonance-lab/) | Science (planetary dynamics) | Product v1.0.0; 14,610 JUP365 epochs across two frozen intervals, replicated ordering, passed numerical gates, and interactive convergence lab. |
| [Snowflake Evolution Lab](https://lindgreendavid.github.io/snowflake-evolution-lab/) | Science (experimental evolution) | Product v0.1.0; five of five cell-shape/cluster-size associations positive, with non-universal exploratory jump ordering and an interactive geometry model. |

## Stable mathematics / data-engineering track

### Mathlab WASM

**Question:** Across separately prespecified one-dimensional suites, which solver guarantees and
failure modes remain observable, and when does a small residual fail to track root error?

**Status:** product v1.0.0 released. The unchanged seven-case v0.1 suite covers bisection, Newton,
and secant; the five-case v0.2 extension adds a Brent–Dekker-style safeguarded hybrid. The frozen
v1.0 protocol adds five conditioning diagnostics. Three algebraically equivalent linear roots keep
the same forward error while their residuals span sixteen orders of magnitude; a local cubic
estimate passes its frozen tolerance; and a repeated root correctly receives no finite simple-root
diagnostic. All seventeen frozen cases and cross-case gates pass.

**Evidence boundary:** the cases were intentionally selected to expose established behavior. They
are not a representative sample of nonlinear equations and do not support a prevalence estimate,
universal stopping rule, rigorous enclosure, solver ranking, or production-library equivalence.
The v1 condition number is explicitly tied to additive function-value perturbations.

**Next evidence step:** v1.0.0 is complete. The next mathematical project should be a separately
designed linear-system laboratory focused on matrix conditioning, forward/backward error, and
stable versus unstable algorithms; it must begin with a new protocol rather than extending these
scalar-root results retrospectively.

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

The first stable research products are shipped, the planetary-dynamics expansion has its complete
v1.0.0 release, and the experimental-evolution expansion has a public, protocol-frozen v0.1 result.

### Snowflake Evolution Lab (field: experimental evolution / multicellularity)

**Selected question:** across the five independently evolved anaerobic MuLTEE populations, is the
association between mean cellular aspect ratio and biomass-weighted mean cluster radius positive in
every lineage over the first 600 daily transfers?

**Status:** the public [interactive laboratory](https://lindgreendavid.github.io/snowflake-evolution-lab/),
[source repository](https://github.com/lindgreendavid/snowflake-evolution-lab),
[Lab Notes article](https://blog-interactive.lindgreendavid.workers.dev/posts/snowflake-evolution-lab-individuality),
and [v0.1.0 release](https://github.com/lindgreendavid/snowflake-evolution-lab/releases/tag/v0.1.0)
are live. The protocol was public before calculation. All five population-level Spearman
correlations are positive (0.923–0.967; median 0.956), and the prespecified no-ancestor, Pearson,
and Kendall sensitivities agree directionally. PA2 day 400 remains missing rather than imputed.

**Evidence boundary:** these are published population means from the source authors, not an
independent wet-lab replication. The five lines are the inference units. Correlated time,
selection, mutations, shape, and size prevent a causal interpretation. Exploratory maximum-jump
ordering differs across populations, providing no universal temporal threshold. The explanatory
cluster animation is not microscopy or a fitted evolutionary simulator.

**Next evidence step:** freeze a new protocol that joins time-resolved ploidy/aneuploidy evidence
to morphological trajectories and tests the coupled-threshold hypothesis: genomic size
amplification may need to coincide with an entangling cellular geometry before robust macroscopic
size emerges. Confirm dataset compatibility, temporal resolution, interventions, and replicate-level
identities before defining an endpoint. Product v1.0.0 requires that independent validation; it
must not be inferred retrospectively from the v0.1 association.

### Jovian Resonance Lab (field: planetary dynamics / celestial mechanics)

**Selected question:** does the v0.1 minimum-force ordering reproduce on a non-overlapping JUP365
interval when every model shares a finer step and G4J2 must pass frozen convergence gates?

**Status:** the public [interactive laboratory](https://lindgreendavid.github.io/jovian-resonance-lab/),
[source repository](https://github.com/lindgreendavid/jovian-resonance-lab), and
[v1.0.0 release](https://github.com/lindgreendavid/jovian-resonance-lab/releases/tag/v1.0.0)
are live. The historical v0.1 protocol and its failed nominal convergence check remain unchanged.
A second protocol was committed before retrieving 3,653 non-overlapping 2031–2040 JUP365 epochs.
At a common 0.0025-day step, G4J2 again beat K2, G3, and G4. The 0.0025-versus-0.00125-day trace
difference was 0.5735° RMSE, the estimated convergence order was 1.984, and the fine trace reached
0.4699° RMSE against JUP365. Every frozen v1 gate passed.

**Evidence boundary:** JUP365 is a fitted ephemeris, not raw astrometry. Its 2031–2040 values are
predictions, not observations collected in those future years. The validation restarts from JUP365
in 2031 and is not a continuous forty-year prediction. No result establishes resonance formation,
billion-year stability, tidal parameters, internal heating, oceans, or habitability.

**Next evidence step:** v1.0.0 is complete. Any extension to solar forcing, higher Jovian harmonics,
pole evolution, or an independently constructed reference must begin with a separate protocol and
must not be folded retrospectively into either completed study.

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
primary-source, provenance, licensing, endpoint, official-log, four-cell frequency-baseline, and
released-data split audits. The complete version-3 four-variant supplement and both version-4 files match their Figshare MD5 checksums.
They contain 625,697 training and 65,445 test rows—691,142 total, matching the final official log
count. The declared reactant/product key has zero exact train/test collisions, and the full declared
record has zero exact cross-split duplicates.

**Evidence boundary:** the locally reproduced baselines are 51.57%, 52.22%, 19.55%, and 20.24%,
all within 0.46 percentage points of the peer-reviewed 52%, 52%, 20%, and 20%. The corresponding
67%, 68%, 35%, and 36% neural-model cells remain published reference values. The v1 audit finds
5.78% product-identity overlap, 80.84% nonempty scaffold overlap, and 60.5% sampled maximum product
similarity ≥0.70. None of those metrics establishes patent-family leakage or wet-lab failure.

**Next evidence step:** if exact model checkpoints, predictions, or complete run identities become
available, archive and verify them under the frozen endpoint. Separately reconstruct a verified
patent-family or temporal split before making generalization claims.

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
