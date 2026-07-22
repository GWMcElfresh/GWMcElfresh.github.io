---
layout: post
title: "Getting Started with Spatial Transcriptomics Analysis"
date: 2025-01-15
excerpt: "A practical introduction to analyzing spatial transcriptomics data from platforms like NanoString GeoMx and CosMx."
---

# Getting Started with Spatial Transcriptomics Analysis

Spatial transcriptomics has revolutionized our ability to profile gene expression while preserving tissue architecture. In this post, I'll share some practical insights from working with platforms like NanoString GeoMx and CosMx.

## Why Spatial Transcriptomics?

Traditional bulk RNA-seq loses spatial information by homogenizing tissue samples. Single-cell RNA-seq provides cellular resolution but requires tissue dissociation, again losing spatial context. Spatial transcriptomics bridges this gap by measuring gene expression while maintaining tissue architecture.

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
- Negative probe signal (background)
- Positive control probes
- Gene detection rates
- ROI/cell coverage
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
- Moran's I for spatial autocorrelation
- Ripley's K for point pattern analysis

**Ligand-Receptor Analysis:**
- Which signaling pairs are active between proximal cells?

## Common Pitfalls

### 1. Over-interpreting Low-Abundance Genes

Spatial platforms have detection limits. Be cautious with genes detected in < 10% of ROIs/cells.

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

Spatial transcriptomics is still evolving rapidly. New platforms, analytical methods, and best practices emerge regularly. The key is to:

1. Understand your platform's strengths and limitations
2. Perform rigorous QC
3. Integrate with complementary data types when possible
4. Validate findings with orthogonal methods

Happy analyzing! Feel free to reach out if you have questions about spatial transcriptomics workflows.

---

*This is a sample blog post demonstrating the blog functionality. You can create similar posts in the `_posts/` directory.*
