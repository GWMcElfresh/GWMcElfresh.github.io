---
layout: default
title: "Spatial Transcriptomics in SIV/TB Co-infection"
---

# Spatial Transcriptomics in SIV/TB Co-infection

*Integration of spatial and single-cell data to identify pathologically relevant markers*

---

## Overview

This project integrates spatial transcriptomics (NanoString GeoMx and CosMx platforms) with single-cell RNA-sequencing data to characterize the tissue microenvironment and cellular responses in rhesus macaques co-infected with SIV and *Mycobacterium tuberculosis*.

**Status**: Ongoing  
**Collaborators**: Bimber Lab , Picker Lab, Estes Lab
**Techniques**: Spatial transcriptomics, single-cell RNA-seq, computational integration

---

## Background

SIV and TB co-infection represents a significant challenge in understanding immune responses at both the cellular and tissue levels. While single-cell RNA-seq provides high-resolution cellular profiling, it loses spatial context. Spatial transcriptomics platforms preserve tissue architecture while measuring gene expression, enabling us to:

1. Map cell types to specific tissue regions
2. Identify pathologically relevant cellular states
3. Understand cell-cell interactions in disease microenvironments
4. Connect molecular signatures to histopathology

---

## Approach

### Data Generation

- **Single-cell RNA-seq**: 10X Genomics platform with cell hashing for multiplex sample processing
- **Spatial transcriptomics**: 
  - NanoString GeoMx (Digital Spatial Profiler): Region-of-interest based profiling
  - NanoString CosMx: Single-cell resolution spatial imaging

### Computational Methods

1. **Quality Control & Preprocessing**
   - Cell filtering and normalization for scRNA-seq data
   - Spatial quality assessment and background correction

2. **Cell Type Annotation**
   - Reference-based annotation using SingleR, Azimuth
   - Manual curation based on marker genes

3. **Spatial Integration**
   - Cell type deconvolution in spatial data using scRNA-seq reference
   - Spatial mapping of cell states identified in scRNA-seq

4. **Spatial Analysis**
   - Neighborhood analysis to identify cellular niches
   - Spatial statistics to test for co-localization patterns
   - Ligand-receptor interaction analysis in spatial context

---

## Key Findings

### Novel Pathologically Relevant Markers

Through integration of spatial and single-cell data, we identified:

- Cell type signatures enriched in granulomatous regions
- Spatial organization patterns associated with disease progression
- Marker genes distinguishing pathological vs. non-pathological cell states

### Cellular Microenvironments

Spatial analysis revealed distinct tissue microenvironments characterized by:

- Immune cell composition
- Transcriptional programs
- Proximity to viral/bacterial infection sites

---

## Technologies Used

### Experimental Platforms
- 10X Genomics Chromium (scRNA-seq)
- NanoString GeoMx Digital Spatial Profiler
- NanoString CosMx Spatial Molecular Imager

### Computational Tools
- **R**: Seurat, Giotto, spatstat
- **Python**: Scanpy, Squidpy, pandas, numpy
- **Analysis**: Cell type deconvolution (RCTD, cell2location), spatial statistics, dimensionality reduction

---

## Impact

This work demonstrates the power of integrating complementary technologies to understand complex disease processes. By combining the cellular resolution of scRNA-seq with the spatial context of tissue imaging, we can:

- Identify disease-relevant cell states that would be missed by either technology alone
- Understand how tissue architecture influences cellular responses
- Develop spatial biomarkers for disease progression

---

## Presentations

**McElfresh GW**, Busman-Sahay K, Nekorchuk M, Benjamin S, Boggy GJ, Feltham S, Mahyari E, Hansen SG, Picker LJ, Estes JD, Bimber BN. (2022). *Integration of Spatial and Single Cell Transcriptomics Identifies Novel Pathologically Relevant Markers in SIV- and Mycobacterium tuberculosis-infected Rhesus Macaques*. Nonhuman Primate Models for AIDS.

---

## Related Work

- [TB Granuloma Formation Project](#)
- [Cell Hashing Demultiplexing Tools](https://doi.org/10.1093/bioinformatics/btac213)

---

## Code & Data

*Code availability pending publication*

---

*This is an example research project page. Create similar pages in `_research/` directory for each major project.*
