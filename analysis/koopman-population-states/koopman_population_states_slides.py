"""Slide notebook: population-state Koopman for cross-sectional scRNA-seq.

Source for /slides/koopman/. Figures write to public/slides/koopman/figures/.
Re-export with: python analysis/koopman-population-states/run.py
"""

# /// script
# [tool.marimo.display]
# theme = "dark"
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", css_file="slides-theme.css")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np

    site_root = Path(__file__).resolve().parents[2]
    figure_dir = site_root / "public" / "slides" / "koopman" / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)

    # Ink + teal so PNG assets match the site even before HTML theme injection.
    ink = "#0a0e12"
    ink_elevated = "#121820"
    text = "#e6ebe8"
    text_muted = "#9aa8a0"
    accent = "#3dcfb6"
    accent_dim = "#2a9a88"

    def style_axes(ax):
        ax.set_facecolor(ink_elevated)
        ax.figure.patch.set_facecolor(ink)
        ax.tick_params(colors=text_muted)
        for spine in ax.spines.values():
            spine.set_color(text_muted)
        ax.xaxis.label.set_color(text)
        ax.yaxis.label.set_color(text)
        ax.title.set_color(text)

    def save_fig(fig, name: str) -> Path:
        path = figure_dir / name
        fig.savefig(path, dpi=160, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close(fig)
        return path

    return (
        accent,
        accent_dim,
        figure_dir,
        ink,
        ink_elevated,
        mo,
        np,
        plt,
        save_fig,
        style_axes,
        text,
        text_muted,
    )


@app.cell
def _(mo):
    mo.md(r"""
    # Population-state Koopman for scRNA-seq

    Cross-sectional single-cell time courses do not provide persistent cell trajectories.
    The open question is whether the **population distribution** over expression space
    still carries enough structure to support dynamical claims.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## The measurement gap

    Bulk RNA-seq averages cells into one vector. scRNA-seq recovers cell states after
    dissociation removes temporal identity. Pseudotime orders cells on a shared manifold,
    but that order is not a measured trajectory of any one cell.

    Forecasting how a *distribution* of states moves is a different problem from
    reconstructing individual paths. The two operate at different scales.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Observation model: fixed supports

    Learn a fixed set of expression-space supports once (k-means or SEACells coarsening).
    At each timepoint, assign cells to those supports and record:

    - **occupancy** — fraction of cells on each support
    - **mean PC coordinates** among assigned cells
    - **observation mask** — zero-cell and below-threshold supports stay masked

    The resulting object is a time-indexed **population state**, not a cell path.
    SEACells coarsens geometry; it does not pre-linearize nonlinear dynamics.
    """)
    return


@app.cell
def _(accent, accent_dim, mo, np, plt, save_fig, style_axes, text, text_muted):
    rng = np.random.default_rng(7)
    n_supports, n_times = 6, 5
    times = np.arange(n_times)
    # Soft occupancy mass that drifts across supports (schematic only).
    base = np.linspace(0.05, 0.35, n_supports)
    occupancy = np.stack(
        [
            np.clip(
                base
                + 0.08 * np.sin(times[t] + np.arange(n_supports))
                + 0.02 * rng.normal(size=n_supports),
                0.02,
                None,
            )
            for t in times
        ]
    )
    occupancy = occupancy / occupancy.sum(axis=1, keepdims=True)

    supports_fig, supports_axes = plt.subplots(
        1, 2, figsize=(9.5, 3.8), gridspec_kw={"width_ratios": [1.2, 1]}
    )
    for supports_ax in supports_axes:
        style_axes(supports_ax)

    im = supports_axes[0].imshow(occupancy.T, aspect="auto", cmap="viridis", origin="lower")
    supports_axes[0].set_xlabel("time index")
    supports_axes[0].set_ylabel("support")
    supports_axes[0].set_title("Occupancy on fixed supports")
    supports_axes[0].set_xticks(times)
    cbar = supports_fig.colorbar(im, ax=supports_axes[0], fraction=0.046, pad=0.04)
    cbar.ax.yaxis.set_tick_params(color=text_muted)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color=text_muted)

    for s in range(n_supports):
        supports_axes[1].plot(
            times,
            occupancy[:, s],
            color=accent if s % 2 == 0 else accent_dim,
            lw=2,
            alpha=0.9,
        )
    supports_axes[1].set_xlabel("time index")
    supports_axes[1].set_ylabel("occupancy")
    supports_axes[1].set_title("Mass redistributes; supports stay fixed")
    supports_axes[1].set_ylim(0, occupancy.max() * 1.25)
    supports_fig.suptitle(
        "Population state = occupancy + masked mean PCs", color=text, fontsize=12, y=1.02
    )

    supports_path = save_fig(supports_fig, "01_population_supports.png")
    mo.vstack(
        [mo.md("### Schematic: fixed supports over time"), mo.image(src=str(supports_path))]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## What GraphKoopman learns

    A graph encoder lifts each population state into a latent vector $z_t$.
    A discrete-time linear operator advances that latent:

    $$
    z_{t+1} = K\, z_t
    $$

    Eigenvalues of $K$ describe per-step growth, decay, and rotation.
    Modes are coherent latent directions; gene loadings associate those directions
    with expression programs. Dynamic Mode Decomposition (DMD) remains the mandatory
    linear baseline: GraphKoopman should beat rank-matched DMD and persistence under
    a leakage-free protocol before predictive language is allowed.
    """)
    return


@app.cell
def _(accent, mo, np, plt, save_fig, style_axes, text, text_muted):
    plane_fig, plane_ax = plt.subplots(figsize=(5.8, 5.8))
    style_axes(plane_ax)

    theta = np.linspace(0, 2 * np.pi, 400)
    plane_ax.plot(np.cos(theta), np.sin(theta), color=text_muted, lw=1.2, label="unit circle")
    plane_ax.axhline(0, color=text_muted, lw=0.6, alpha=0.5)
    plane_ax.axvline(0, color=text_muted, lw=0.6, alpha=0.5)

    # Schematic eigenvalues (not a fitted spectrum).
    eigs = np.array(
        [
            0.92 + 0.0j,
            0.75 + 0.35j,
            0.75 - 0.35j,
            0.55 + 0.0j,
            1.08 + 0.12j,
            1.08 - 0.12j,
            -0.4 + 0.0j,
        ]
    )
    plane_ax.scatter(
        eigs.real, eigs.imag, c=accent, s=70, zorder=3, edgecolors=text, linewidths=0.6
    )

    annotations = [
        (0.92, 0.08, "near +1\nslow / near-identity"),
        (0.55, -0.22, "0 < λ < 1\ndecay"),
        (0.55, 0.55, "Im ≠ 0\noscillation"),
        (1.05, 0.35, "|λ| > 1\ngrowth"),
        (-0.4, 0.12, "λ < 0\nperiod-2"),
    ]
    for anno_x, anno_y, anno_label in annotations:
        plane_ax.annotate(
            anno_label,
            xy=(anno_x, anno_y),
            xytext=(anno_x, anno_y),
            color=text,
            fontsize=8,
            ha="center",
            va="center",
        )

    plane_ax.set_xlim(-1.35, 1.45)
    plane_ax.set_ylim(-1.35, 1.45)
    plane_ax.set_aspect("equal")
    plane_ax.set_xlabel(r"Re($\lambda$)")
    plane_ax.set_ylabel(r"Im($\lambda$)")
    plane_ax.set_title("Discrete-time eigenvalue plane (schematic)")

    plane_path = save_fig(plane_fig, "02_eigenvalue_plane.png")
    mo.vstack([mo.md("### Reading the spectrum"), mo.image(src=str(plane_path))])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Why one global $K$ is not enough

    A single finite-dimensional linear operator has a unique fixed point at the origin
    in latent coordinates. Multi-attractor or bifurcating biology — pluripotency versus
    commitment, early versus late immune response — does not live comfortably inside
    one global map. For true multi-attractor systems the exact Koopman lifting is
    infinite-dimensional.

    The v0 path in this work is **Strategy 4**: partition into locally linear segments,
    fit one operator per segment on a **shared** observation basis, then compare spectra.
    """)
    return


@app.cell
def _(accent, accent_dim, mo, plt, save_fig, style_axes, text, text_muted):
    segment_fig, segment_axes = plt.subplots(1, 2, figsize=(9.2, 3.6))
    for segment_ax in segment_axes:
        style_axes(segment_ax)

    # Left: one global K trying to cover two basins.
    segment_axes[0].add_patch(plt.Circle((-0.6, 0), 0.35, fill=False, ec=accent_dim, lw=2))
    segment_axes[0].add_patch(plt.Circle((0.6, 0), 0.35, fill=False, ec=accent_dim, lw=2))
    segment_axes[0].annotate(
        "",
        xy=(0.25, 0.05),
        xytext=(-0.25, 0.05),
        arrowprops=dict(arrowstyle="->", color=accent, lw=2),
    )
    segment_axes[0].annotate(
        "",
        xy=(-0.25, -0.05),
        xytext=(0.25, -0.05),
        arrowprops=dict(arrowstyle="->", color=accent, lw=2),
    )
    segment_axes[0].text(0, 0.75, "one global K", color=text, ha="center")
    segment_axes[0].text(-0.6, -0.7, "basin A", color=text_muted, ha="center", fontsize=9)
    segment_axes[0].text(0.6, -0.7, "basin B", color=text_muted, ha="center", fontsize=9)
    segment_axes[0].set_xlim(-1.2, 1.2)
    segment_axes[0].set_ylim(-1.0, 1.0)
    segment_axes[0].set_aspect("equal")
    segment_axes[0].axis("off")
    segment_axes[0].set_title("Insufficient for multi-attractor maps")

    # Right: segmented operators.
    segment_axes[1].add_patch(plt.Circle((-0.55, 0), 0.32, fill=False, ec=accent, lw=2))
    segment_axes[1].add_patch(plt.Circle((0.55, 0), 0.32, fill=False, ec=accent_dim, lw=2))
    segment_axes[1].annotate(
        "",
        xy=(-0.35, 0.25),
        xytext=(-0.75, -0.2),
        arrowprops=dict(arrowstyle="->", color=accent, lw=2),
    )
    segment_axes[1].annotate(
        "",
        xy=(0.75, 0.2),
        xytext=(0.35, -0.25),
        arrowprops=dict(arrowstyle="->", color=accent_dim, lw=2),
    )
    segment_axes[1].text(-0.55, 0.55, r"$K_1$", color=accent, ha="center", fontsize=12)
    segment_axes[1].text(0.55, 0.55, r"$K_2$", color=accent_dim, ha="center", fontsize=12)
    segment_axes[1].text(
        0, -0.85, "shared supports · compare spectra", color=text_muted, ha="center", fontsize=9
    )
    segment_axes[1].set_xlim(-1.2, 1.2)
    segment_axes[1].set_ylim(-1.0, 1.0)
    segment_axes[1].set_aspect("equal")
    segment_axes[1].axis("off")
    segment_axes[1].set_title("Locally linear segments (v0)")

    segment_path = save_fig(segment_fig, "03_global_vs_segmented.png")
    mo.vstack(
        [
            mo.md("### Global operator versus segmented fits"),
            mo.image(src=str(segment_path)),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Datasets as different questions

    | Dataset | What it asks | Caveat |
    |---------|--------------|--------|
    | **Buettner** ESC cycle | Do local modes recover known cycle programs after circular ordering? | Pseudotime is exploratory; three FACS phases cannot identify cycle frequency |
    | **Hagai** innate time course | Early vs late windows under stimulation | Primary real perturbation dynamics setting |
    | **Kang** IFN-β PBMC | Control vs stimulated concordance by lineage | Condition-shift validation, not autonomous $K$ identification |
    | **Embryoid body** | Population forecast and branch-local models | Branch models stay descriptive without correspondence |

    Shared rule: compare spectra only on a matched observation basis
    (same preprocessing hash, PCA loadings, supports, feature order, and $\Delta t$).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Claim gates before dynamical language

    Interpretive language is gated, not aspirational:

    1. **Identifiability** — enough independent transitions per window (else `one_step_descriptive`)
    2. **Matched basis** — shared supports and preprocessing across compared segments
    3. **Forecast skill** — leakage-free held-out RMSE beats persistence and rank-matched DMD
    4. **Stability** — observation/replicate resampling separates sampling noise from spectral shifts
    5. **Conjugate pairing** — complex modes paired before gene interpretation; oscillation language needs correct $\Delta t$

    Synthetic smoke confirms the pipeline. It does not license biological claims.
    """)
    return


@app.cell
def _(accent, accent_dim, mo, plt, save_fig, style_axes, text, text_muted):
    gates = [
        ("≥ 3 transitions", True),
        ("matched shared basis", True),
        ("leakage-free protocol", True),
        ("beats persistence", False),
        ("beats rank-matched DMD", False),
    ]
    gates_fig, gates_ax = plt.subplots(figsize=(7.2, 3.4))
    style_axes(gates_ax)
    gate_ys = list(range(len(gates)))[::-1]
    gate_colors = [accent if ok else accent_dim for _, ok in gates]
    gates_ax.barh(
        gate_ys,
        [1] * len(gates),
        color=gate_colors,
        height=0.55,
        edgecolor=text_muted,
        linewidth=0.5,
    )
    for gate_y, (gate_name, gate_ok) in zip(gate_ys, gates):
        mark = "PASS gate" if gate_ok else "blocks predictive language"
        gates_ax.text(
            0.05,
            gate_y,
            f"{gate_name}  —  {mark}",
            va="center",
            ha="left",
            color=text,
            fontsize=10,
        )
    gates_ax.set_xlim(0, 1)
    gates_ax.set_yticks([])
    gates_ax.set_xticks([])
    gates_ax.set_title("PredictiveClaimGate (illustrative: skill not yet earned)")
    for spine in gates_ax.spines.values():
        spine.set_visible(False)

    gates_path = save_fig(gates_fig, "04_claim_gates.png")
    mo.vstack(
        [
            mo.md("### Gates separate description from prediction"),
            mo.image(src=str(gates_path)),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## What this reveals — and what it leaves open

    Treating scRNA time courses as evolving population states converts a missing-trajectory
    problem into a distribution-forecasting problem. Segmented operators let spectra be
    compared where a single global $K$ would blur basins together. Claim gates keep
    descriptive spectra from being read as predictive dynamics.

    What remains unresolved is when real data earn those gates: longer matched time courses,
    stronger correspondence across branches, and mixture-of-operators or attractor-anchor
    losses beyond the v0 segmented path. The present scaffolding makes those tests
    falsifiable rather than rhetorical.
    """)
    return


@app.cell
def _(figure_dir, mo):
    mo.md(f"""
    ## Source and reproducibility

    - Experiment package: sibling repo `KoopmanExperimentation` (`scrna_koopman`)
    - Slide source: `analysis/koopman-population-states/koopman_population_states_slides.py`
    - Figures on disk: `{figure_dir.as_posix()}`
    - Re-export: `python analysis/koopman-population-states/run.py`

    Figures above are **schematics** for the talk. Fitted spectra and claim-gate outcomes
    live in the experiment notebooks and are evidence-tiered (`synthetic_smoke` vs
    `real_data_candidate`).
    """)
    return


if __name__ == "__main__":
    app.run()
