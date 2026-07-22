# KOOPMAN POPULATION STATES

Slide-oriented marimo talk on population-state Koopman operators for cross-sectional
scRNA-seq, exported to `/slides/koopman/` and embedded from the Astro blog.

## Source

| Artifact | Path |
|----------|------|
| Marimo notebook | `analysis/koopman-population-states/koopman_population_states_slides.py` |
| Export runner | `analysis/koopman-population-states/run.py` |
| Theme injector | `scripts/inject_slides_theme.py` |
| Hosted HTML | `public/slides/koopman/index.html` |
| Figures | `public/slides/koopman/figures/*.png` |
| Blog post | `src/content/blog/2026-07-21-koopman-population-states.md` |

Experiment code and fitted notebooks live in the sibling repo `KoopmanExperimentation`
(`scrna_koopman`). This analysis folder holds the **talk** source only.

## Reproduce

```bash
python analysis/koopman-population-states/run.py
```

Requires `marimo` and `matplotlib` (the KoopmanExperimentation `.venv` is used if present).
Re-run after notebook or figure changes; commit the new HTML and PNGs.

## Notes

- Figures in the deck are schematics for explanation, not fitted spectra.
- Claim-gate and evidence-tier language follows `KoopmanExperimentation/SCIENTIFIC_AUDIT.md`.
- Primary embedded experience is static HTML + iframe; optional PDF `--as=slides` is a
  parallel download, not the default.
