# Lab Notes portfolio identity

This is the canonical design contract for David Lindgreen's research portfolio. It makes every
project recognisably part of one research programme while preserving a meaningful visual accent for
each scientific field.

## The invariant layer

Every current and future research project uses the same:

- Lab Notes research-cycle mark and portfolio attribution;
- semantic token names, spacing scale, typography roles, and responsive content width;
- question → evidence → finding → boundary information architecture;
- visible distinction between confirmatory, sensitivity, and exploratory material;
- accessible focus treatment, keyboard interaction, reduced-motion handling, and WCAG AA contrast;
- links to the protocol, report, machine-readable result, source, licence, and citation metadata;
- README order: question, result, interactive experience, evidence, reproduction, boundary, citation;
- release and quality gate documented in [`templates/research-project/QUALITY_GATE.md`](../templates/research-project/QUALITY_GATE.md).

## The variable layer

Each discipline may select one accessible accent pair for charts and interaction. The project must
map it to `--ln-accent` and `--ln-accent-wash`; it must not redefine the semantic architecture.
Project-specific illustrations are encouraged when they explain the actual method or phenomenon.

| Family | Suggested accent | Meaning |
| --- | --- | --- |
| Portfolio / editorial | Burgundy `#7a2331` | Lab Notes and profile surfaces |
| Responsible AI | Coral / signal green | distribution shift and decisions |
| Physics | Violet / cyan | trajectories and dynamical systems |
| Astrophysics | Magenta / pulse teal | populations and radio signals |
| Structural biology | teal / leaf green | molecular structure and disorder |
| Climate | ember / deep teal | urban heat and reference stations |
| Neuroscience | violet / cyan | electrodes, contrasts, and intervals |

## Rules for new projects

1. Start from the research-project templates in this repository.
2. Copy `brand/tokens.css`, then map only the discipline accent tokens.
3. Add the Lab Notes mark and portfolio link to the README and site footer.
4. Keep the scientific boundary visible before release.
5. Run the quality gate and accessibility checks before publishing.
6. Add the project to Lab Notes and the GitHub profile only after its public evidence is inspectable.

The identity is versioned. Breaking changes require a documented migration rather than ad-hoc edits
to individual projects.
