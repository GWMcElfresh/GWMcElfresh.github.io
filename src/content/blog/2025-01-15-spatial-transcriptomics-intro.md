---
title: Getting Started with Spatial Transcriptomics Analysis
date: 2025-01-15
excerpt: Spatial assays recover expression with tissue coordinates; the practical problem is matching platform resolution and gene depth to the biological scale you need to resolve.
---

Understanding how gene expression varies across tissue is critical to interpreting microenvironment structure, pathology, and local signaling. However, the assays we use most often break that relationship: bulk RNA-seq averages over homogenized regions, while single-cell RNA-seq recovers cellular states only after dissociation removes spatial context. Spatial transcriptomics measures expression while retaining tissue architecture, but platforms differ in resolution, gene coverage, and the biases they introduce. Here, I outline practical considerations from working with NanoString GeoMx and CosMx—not as a survey of technology, but as a guide to matching the measurement to the spatial scale your question occupies.

## Why Spatial Transcriptomics?

The consequential gap is between molecular measurement and tissue organization. Bulk assays report population averages; scRNA-seq reports cell states without neighborhoods. Spatial methods sit between these regimes by treating expression as a function of location. A useful mental model is that expression $x$ at location $\mathbf{r}$ is a random field — spatial statistics (Moran's $I$, Ripley's $K$) ask whether nearby observations are more correlated than chance.

That framing determines what you can claim. ROI-level GeoMx profiles regions; CosMx approaches single-cell resolution with smaller panels. The choice is not which platform is better in the abstract, but which spatial scale and gene depth your biology requires.

### Key Applications

1. **Tissue Microenvironment Characterization**: Understanding cellular neighborhoods and niches
2. **Disease Pathology**: Mapping disease-relevant cell states to tissue regions
3. **Cell-Cell Interactions**: Identifying signaling between spatially proximal cells
4. **Biomarker Discovery**: Finding spatial signatures of disease

## Platform Considerations

### NanoString GeoMx DSP (Digital Spatial Profiler)

**Strengths:**
- High-plex gene panels (up to 18,000 genes)
- FFPE tissue compatibility
- Region-of-interest (ROI) based profiling
- Excellent for discovery

**Limitations:**
- Lower spatial resolution (ROI-based, not single-cell)
- Manual ROI selection can introduce bias

### NanoString CosMx

**Strengths:**
- Single-cell resolution
- Sub-cellular localization
- Larger field of view

**Limitations:**
- Smaller gene panels (typically 100-1000 genes)
- More expensive per sample

## Analysis Workflow

### 1. Quality Control

```r
# Example QC metrics to check
# - Negative probe signal (background)
# - Positive control probes
# - Gene detection rates
# - ROI/cell coverage
```

Key questions:
- Is background signal consistent across samples?
- Are positive controls within expected ranges?
- Any outlier ROIs or cells?

### 2. Normalization

Spatial data requires careful normalization to account for:
- Technical variability between AOIs/cells
- Background signal
- Sequencing depth (for sequencing-based platforms)

I typically use:
- Q3 normalization for GeoMx data
- Size factor normalization for cell-level data

### 3. Cell Type Deconvolution (for GeoMx)

Since GeoMx provides ROI-level data, we often need to estimate cell type composition:

```r
# Using a single-cell reference
library(Seurat)
library(spacexr)

# Run RCTD or similar deconvolution method
```

### 4. Spatial Analysis

This is where it gets interesting:

**Neighborhood Analysis:**
- Which cell types are enriched near each other?
- Are certain cell states clustered in tissue regions?

**Spatial Statistics:**
- Moran's $I$ for spatial autocorrelation
- Ripley's $K$ for point pattern analysis

**Ligand-Receptor Analysis:**
- Which signaling pairs are active between proximal cells?

## Common Pitfalls

### 1. Over-interpreting Low-Abundance Genes

Spatial platforms have detection limits. Be cautious with genes detected in &lt; 10% of ROIs/cells.

### 2. Ignoring Tissue Heterogeneity

Different tissue regions may have fundamentally different biology. Always stratify analyses by tissue type/region when appropriate.

### 3. Batch Effects

Spatial experiments often involve multiple slides or imaging rounds. Include batch as a covariate in differential expression models.

### 4. Multiple Testing

With spatial data, you're testing many hypotheses (thousands of genes × many ROIs). Use appropriate multiple testing correction (FDR, Bonferroni, etc.).

## Integration with Single-Cell Data

The real power comes from integrating spatial and single-cell data:

1. **Cell Type Annotation**: Use scRNA-seq as reference for spatial cell typing
2. **Marker Validation**: Verify scRNA-seq markers in spatial context
3. **State Mapping**: Map cellular states from scRNA-seq onto tissue

## Tools I Use

**R Packages:**
- `Seurat`: General-purpose, excellent for integration
- `Giotto`: Spatial-specific analysis framework
- `spatstat`: Spatial statistics
- `RCTD`/`cell2location`: Deconvolution

**Python:**
- `Scanpy`: Single-cell analysis
- `Squidpy`: Spatial transcriptomics extension of Scanpy
- `pandas`/`numpy`: Data manipulation

## Final Thoughts

Choosing between GeoMx and CosMx reveals what you are willing to trade: gene depth against cellular resolution, ROI selection bias against panel size. Neither platform returns a ground-truth map of tissue; each returns a projection shaped by its sampling geometry. Rigorous QC, careful normalization, and integration with scRNA-seq can constrain that projection, but they do not erase it.

What often remains unresolved is not the pipeline itself, but whether the retained spatial scale matches the process you care about—neighborhood enrichment, regional pathology, or subcellular localization. When a spatial signature becomes a biological claim, orthogonal validation is still needed to separate platform geometry from tissue biology.
