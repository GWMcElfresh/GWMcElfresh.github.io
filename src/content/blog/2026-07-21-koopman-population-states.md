---
title: Population-state Koopman for cross-sectional scRNA-seq
date: 2026-07-21
excerpt: Cross-sectional scRNA-seq lacks cell trajectories; population states on fixed supports turn that gap into a distribution-forecasting problem with gated dynamical claims.
---

Understanding how cell-state distributions move through a perturbation is critical to
interpreting time-course scRNA-seq, yet the assay does not record trajectories of
individual cells. Pseudotime orders cells on a shared manifold; it does not measure the
path any one cell took. The practical consequence is a scale mismatch: we often want
dynamical language (growth, decay, oscillation of programs) while the data only guarantee
cross-sectional snapshots.

Here I treat each timepoint as a **population state** on fixed expression-space supports:
occupancy of each support, masked mean principal-component coordinates among assigned cells,
and an explicit observation mask for empty or under-covered supports. A GraphKoopman model
then learns a discrete-time linear map in a latent space produced by a graph encoder.
Eigenvalues of that map describe per-step growth, decay, and rotation; they do not, by
themselves, license predictive claims.

<a class="btn" href="/slides/koopman/">Open slides</a>

<div class="slides-embed" style="aspect-ratio: 16 / 9; width: 100%; margin: 1.5rem 0 2rem;">
  <iframe
    src="/slides/koopman/"
    title="Population-state Koopman slides"
    style="width: 100%; height: 100%; border: 0; border-radius: 2px; background: #0a0e12;"
    loading="lazy"
  ></iframe>
</div>

## Why a single global operator is the wrong default

A finite-dimensional linear operator advancing $z_{t+1} = K z_t$ has a unique fixed point
at the origin in latent coordinates. Multi-attractor biology — early versus late immune
response, pluripotency versus commitment — does not sit comfortably inside one global $K$.
For true multi-attractor systems the exact Koopman lifting is infinite-dimensional. The
v0 path I use is therefore segmented and locally linear: partition the course into windows,
fit one operator per segment on a **shared** observation basis, and compare spectra rather
than forcing a single map to cover every basin.

Dynamic Mode Decomposition remains the mandatory linear baseline. GraphKoopman should beat
rank-matched DMD and persistence under a leakage-free protocol before any text says the
model is predictive. Synthetic smoke confirms the pipeline; it does not earn biological
claims.

## What the slides cover

The deck walks through the observation model, the eigenvalue-plane grammar, the global
versus segmented contrast, the four public datasets as different questions, and the claim
gates that separate description from prediction. Figures are schematics written to disk
under `/slides/koopman/figures/` so the export stays offline-stable.

Fitted spectra, bootstrap clouds, and gate outcomes live in the experiment notebooks in
`KoopmanExperimentation`. Those results are evidence-tiered (`synthetic_smoke` versus
`real_data_candidate`) for a reason: cache hits and offline fixtures must not travel as
fresh real-data evidence.

## What remains open

The scaffolding makes the next tests falsifiable. Longer matched time courses, stronger
correspondence across differentiation branches, and mixture-of-operators or attractor-anchor
losses beyond segmented fits are the productive extensions. Until held-out skill clears the
gates, the honest reading of a spectrum is descriptive structure in a population state —
not a forecast of where that population will go.
