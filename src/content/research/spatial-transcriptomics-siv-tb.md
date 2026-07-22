---
title: Spatial Transcriptomics in SIV/TB Co-infection
excerpt: SIV/TB co-infection reshapes immunity at the tissue scale, but single-cell profiles lose architecture; we integrate GeoMx, CosMx, and scRNA-seq to recover pathologically relevant cellular states in place.
status: Ongoing
order: 1
---

*Linking tissue niches to cellular state in SIV/TB co-infection*

## Overview

Understanding how SIV and *Mycobacterium tuberculosis* reshape immunity is critical for predicting disease progression in co-infected hosts. However, most high-resolution measurements collapse tissue architecture into a bag of dissociated cells, obscuring the relationship between local niches and cellular state. Here, we integrate spatial transcriptomics (NanoString GeoMx and CosMx) with single-cell RNA-seq from rhesus macaques to recover that relationship: which cell states occupy which tissue regions, and how proximity to infection sites constrains the programs those cells express.

**Status**: Ongoing  
**Collaborators**: Bimber Lab, Picker Lab, Estes Lab  
**Techniques**: Spatial transcriptomics, single-cell RNA-seq, computational integration

## Background

SIV/TB co-infection engages immune responses at two scales that are easy to conflate. At the cellular scale, single-cell RNA-seq resolves transcriptional states with high resolution, yet dissociation erases where those states sat in tissue. At the tissue scale, histopathology preserves architecture and lesion geography, but cannot assign molecular identity to the cells that form each niche. The practical consequence is similar for both approaches alone: pathologically relevant programs can be measured without knowing their location, or localized without knowing their molecular state.

Spatial transcriptomics platforms preserve tissue context while measuring gene expression, linking the two scales. Region-of-interest profiling (GeoMx) and single-cell resolution imaging (CosMx) allow us to map cell types onto tissue regions, distinguish pathological from non-pathological cellular states, quantify cell–cell neighborhoods in disease microenvironments, and connect molecular signatures to histopathology. The NHP co-infection model is well suited for this question: it produces granulomatous and non-granulomatous regions under controlled infection, providing enough structure to ask whether a given cell state is defined by identity alone or by the niche it occupies.

## Approach

### Data Generation

- **Single-cell RNA-seq**: 10X Genomics platform with cell hashing for multiplex sample processing
- **Spatial transcriptomics**:
  - NanoString GeoMx (Digital Spatial Profiler): Region-of-interest based profiling
  - NanoString CosMx: Single-cell resolution spatial imaging

### Computational Methods

We treat scRNA-seq as a reference atlas of cellular states and spatial assays as maps onto which those states must be placed. Quality control and preprocessing filter and normalize single-cell libraries, then assess spatial quality and correct background. Cell types are annotated with reference-based methods (SingleR, Azimuth) and curated against marker panels. Spatial integration uses deconvolution against the scRNA-seq reference to estimate cell-type composition in GeoMx regions and to map transcriptional states onto CosMx coordinates. Neighborhood analysis, co-localization statistics, and ligand–receptor context then test whether disease-associated programs concentrate in particular tissue geometries rather than appearing uniformly across the section.

1. **Quality Control & Preprocessing** — cell filtering and normalization; spatial quality assessment and background correction
2. **Cell Type Annotation** — reference-based annotation (SingleR, Azimuth) with marker curation
3. **Spatial Integration** — deconvolution using scRNA-seq reference; mapping cell states onto tissue
4. **Spatial Analysis** — neighborhood analysis, co-localization statistics, ligand–receptor context

## Key Findings

### Novel Pathologically Relevant Markers

Integration of spatial and single-cell data revealed cell-type signatures enriched in granulomatous regions and spatial organization patterns that track with disease progression. Marker genes further distinguished pathological from non-pathological cell states that would appear similar if measured only after dissociation. These results support the view that pathological relevance is partly a property of position: the same broad cell identity can occupy distinct programs depending on its tissue niche.

### Cellular Microenvironments

Spatial analysis revealed distinct tissue microenvironments defined by immune cell composition, transcriptional programs, and proximity to viral or bacterial infection sites. At the tissue scale, these niches organize into recurring neighborhoods; at the cellular scale, the programs within those neighborhoods are not interchangeable with the average profile of the same annotated cell type elsewhere in the section. Thus, microenvironment is not merely a descriptive backdrop—it is part of the mechanism that selects which cellular states are observed.

## Technologies Used

### Experimental Platforms
- 10X Genomics Chromium (scRNA-seq)
- NanoString GeoMx Digital Spatial Profiler
- NanoString CosMx Spatial Molecular Imager

### Computational Tools
- **R**: Seurat, Giotto, spatstat
- **Python**: Scanpy, Squidpy, pandas, numpy
- **Analysis**: Cell type deconvolution (RCTD, cell2location), spatial statistics, dimensionality reduction

## Impact

Neither scRNA-seq nor spatial imaging alone resolves the relationship between cellular state and tissue architecture in SIV/TB co-infection. Combined, they identify disease-relevant states missed by either technology in isolation, show how tissue geometry constrains cellular responses, and provide a path toward spatial biomarkers of progression. The approach converts a measurement limitation—loss of place or loss of identity—into a tractable model for asking which programs are defined by cell type, which by niche, and which by their interaction.

## Presentations

**McElfresh GW**, Busman-Sahay K, Nekorchuk M, Benjamin S, Boggy GJ, Feltham S, Mahyari E, Hansen SG, Picker LJ, Estes JD, Bimber BN. (2022). *Integration of Spatial and Single Cell Transcriptomics Identifies Novel Pathologically Relevant Markers in SIV- and Mycobacterium tuberculosis-infected Rhesus Macaques*. Nonhuman Primate Models for AIDS.

## Related Work

- [cellhashR / BFF demultiplexing](https://doi.org/10.1093/bioinformatics/btac213)

## Code & Data

*Code availability pending publication*
