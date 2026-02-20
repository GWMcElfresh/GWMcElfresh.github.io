---
layout: default
title: CV
permalink: /cv/
---

# Curriculum Vitae

**GW McElfresh**  
Computational Biology PhD  
Oregon Health & Science University / Oregon National Primate Research Center

[Download PDF Version](/assets/cv/McElfresh_CV.pdf)

---

## Professional Summary

Computational biologist with expertise spanning single-cell and spatial transcriptomics, mathematical modeling, machine learning, and structural biology. I build analytical frameworks that turn high-dimensional biological data into actionable insights. From co-developing a widely-used rhesus macaque immune reference atlas to authoring open-source tools that have been adopted across the single-cell sequencing community. Equally comfortable designing a stochastic model, deploying an HPC pipeline at scale, or collaborating with wet-lab immunologists to answer disease-relevant questions. Seeking to apply multiscale analytical expertise to challenging problems at the intersection of biology, data science, and translational research.

---

## Education

**PhD in Computational Biology**  
University of Kansas, Lawrence, KS  
Center for Computational Biology  
*Dissertation*: Multiscale analyses of cellular signaling and regulation in response to multiple stress conditions

**Bachelor of Science in Mathematics & Physics**  
Drury University, Springfield, MO  
*Graduated with honors*

---

## Research Experience

### Professional Experience

**Oregon National Primate Research Center / Oregon Health & Science University**  
*Computational Biologist 3* | December 2024 – Present  
*Computational Biologist 2* | November 2020 – December 2024

- Co-developed the **Rhesus Immune Reference Atlas (RIRA)** — the first immune-focused, multi-tissue single-cell atlas for rhesus macaques — integrating data across >15 tissues and providing a community-standard reference for reconciling transcriptional profiles with established immune lineages (published *Cell Genomics*, 2025)
- Designed and deployed end-to-end single-cell RNA-seq pipelines for studies of HIV/SIV, Tuberculosis, and Yellow Fever, enabling discovery of correlates of protection in NHP vaccine models
- Authored and maintain open-source R packages on GitHub: **[cellhashR](https://github.com/BimberLab/cellhashR)** (scRNA-seq cell-hashing demultiplexing, widely adopted across the single-cell community) and **[tcrClustR](https://github.com/GWMcElfresh/tcrClustR)** (TCR repertoire clustering and analysis)
- Developed a supplemental alignment pipeline capturing allele-specific MHC-I regulation and other immune signals systematically missed by dominant scRNA-seq workflows
- Collaborated with experimental immunologists and virologists across multiple labs to translate high-dimensional data into biological hypotheses and manuscript-ready analyses

### Graduate Research
**University of Kansas** | 2015–2020  
*Advisor: J. Christian Ray, PhD*

- Characterized overlapping transcriptomic stress responses (stimulons) in *E. coli* using bulk RNA-seq, identifying shared gene expression programs across divergent stressors — co-first author on two resulting manuscripts
- Built stochastic and agent-based models of bacterial cell-cycle dynamics to reconstruct the inheritance of stress signals across generations
- Developed and benchmarked template-based protein–protein docking approaches in collaboration with the Vakser Lab (KU), contributing to best-practice guidelines for structural modeling of protein complexes
- Completed dissertation: *Multiscale analyses of cellular signaling and regulation in response to multiple stress conditions*

### Undergraduate Research
**University of Missouri** | Summer 2014  
*Advisor: Xiaoqin Zou, PhD*

- Developed multi-target molecular docking methods for protein kinase inhibitor selectivity studies, presented at the University of Missouri Summer Undergraduate Research Symposium

**Drury University** | 2013–2015  
*Advisor: Christos Deligkaris, PhD*

- Derived and implemented a vibrational entropy correction term for DNA–small molecule docking in AutoDock, improving binding free energy predictions; published as first author in *Computational Biology and Chemistry* (2018)

---

## Technical Skills

### Computational & Quantitative Skills

**Transcriptomics & Genomics**
- Bulk RNA-seq, single-cell RNA-seq (10X Genomics), spatial transcriptomics (NanoString GeoMx/CosMx)
- Transcriptomic pipelines: read alignment, quality control, differential expression (DESeq2, edgeR, kallisto/sleuth)
- Cell type deconvolution and spatial data analysis

**Machine Learning & Statistics**
- Dimensionality reduction: PCA, MDS, UMAP, t-SNE
- Classification algorithms, clustering methods (hierarchical, k-means, graph-based)
- Deep learning: CNNs, Deep Neural Networks, autoencoders (TensorFlow, PyTorch)
- Statistical inference: regression, hypothesis testing, shrinkage methods.
- Frequentist, Bayesian, and hybrid methodologies. 

**Mathematical Modeling**
- Stochastic biochemical models (Gillespie, CME)
- Agent-based models and multiscale simulations
- Dynamical systems analysis
- Graph theory and network analysis

**Structural Biology**
- Protein-protein docking (template-based and ab initio)
- Small molecule docking (AutoDock, Vina)
- Molecular dynamics simulations
- Protein design (PyRosetta)

**Programming & Tools**
- **Languages**: Python (expert), R (advanced), MATLAB, Mathematica, C++, Perl, bash, SQL, FORTRAN
- **Python Libraries**: pandas, numpy, scipy, scikit-learn, seaborn, matplotlib, TensorFlow, PyTorch
- **Bioinformatics**: Bioconductor, Seurat, Scanpy, STAR, kallisto
- **Image Analysis**: FIJI/ImageJ, Pillow, OpenCV
- **Version Control**: git, GitHub, BitBucket
- **Containerization**: Docker, Singularity/Apptainer
- **HPCs**: SLURM, PBS job schedulers; experience with high performance computing clusters

**Data & Markup**
- LaTeX, Markdown, YAML, XML, SBML, HTML/CSS, Parquet, JSON
- Database: SQL

### Experimental Laboratory Skills

- RNA-Seq sample preparation for Illumina sequencing
- Bacterial molecular genetics and culture techniques
- Microbiology: plating, antibiotic selection, cell quantification
- Aseptic technique and biosafety protocols

### Domain Knowledge

- Immunology and infectious disease
- Microbial physiology and biofilms
- Population genetics and genomics
- Epidemiological modeling
- Scientific writing and communication

---

## Teaching Experience

**Bioinformatics**  
*Lab Teaching Assistant*, University of Kansas  
Fall 2018, Fall 2019, Spring 2020
- Led hands-on computational labs for bioinformatics tools and pipelines
- Taught sequence alignment, phylogenetics, and transcriptomic analysis

**Genetics**  
*Discussion Leader & Primary Grader*, University of Kansas  
Summer 2017
- Facilitated discussion sections on Mendelian and molecular genetics
- Developed assessment materials and graded assignments

**Introduction to Cellular and Molecular Biology**  
*Lab Teaching Assistant*, University of Kansas  
Fall 2016, Fall 2017
- Supervised laboratory experiments in molecular biology
- Assisted with lecture content and grading

**Introduction to Organismal Biology**  
*Lab Teaching Assistant*, University of Kansas  
Spring 2016
- Taught lab techniques for studying organismal diversity
- Mentored undergraduate students in experimental design

**Introduction to Principles of Biology**  
*Lab Teaching Assistant*, University of Kansas  
Fall 2015
- Introduced first-year students to fundamental biology concepts
- Supervised laboratory safety and technique

---

## Publications

See [Publications page]({{ site.url }}/publications) for complete list with abstracts and DOI links.

### Selected Publications

- Mahyari E, Boggy GJ, **McElfresh GW**, et al. (2025). Enhanced interpretation of immune cell phenotype and function through a rhesus macaque single-cell atlas. *Cell Genomics*, 5(5).

- Bimber BN, Sunshine J, **McElfresh GW**, et al. (2025). Viral escape mutations do not account for non-protection from SIVmac239 challenge in RhCMV/SIV vaccinated rhesus macaques. *Frontiers in Immunology*, 15: 1444621.

- Boggy GJ, **McElfresh GW**, et al. (2022). BFF and cellhashR: analysis tools for accurate demultiplexing of cell hashing data. *Bioinformatics*, 38(10), 2791–2801.

- Wang H, **McElfresh GW**†, et al. (2023). Signatures of antibiotic tolerance and persistence in response to divergent stresses. *bioRxiv* 2023.02.05.527212.

- Chakravarty D, **McElfresh GW**, et al. (2020). How to choose templates for modeling of protein complexes. *Proteins*, 88(9), 1070–1081.

- **McElfresh GW**†, Deligkaris C. (2018). A vibrational entropy term for DNA docking with AutoDock. *Computational Biology and Chemistry*, 73, 9–14.

† Co-first / first author

---

## Presentations & Conferences

### Selected Conference Presentations

**2022** | Nonhuman Primate Models for AIDS  
*Integration of Spatial and Single Cell Transcriptomics in TB Co-infection*

**2021** | Nonhuman Primate Models for AIDS  
*Single Cell Transcriptomic Profiling of TB Granuloma Formation*

**2019** | q-bio Conference  
*Discrete timescales of stress signal effects on the cell cycle*

**2018** | Modeling of Protein Interactions  
*Reconstructing the Role of Inheritance in Stress Signaling*

[See full list on Publications page]({{ site.url }}/publications#selected-presentations)

---

## Awards & Honors

- Graduate Research Award, University of Kansas (2019)
- Outstanding Physics Student Researcher, Drury University (2015)

---

## Service & Outreach

- Peer reviewer: *Nature Communications*
- Open-source software author: [cellhashR](https://github.com/BimberLab/cellhashR) and [tcrClustR](https://github.com/GWMcElfresh/tcrClustR) (GitHub)

---

## References

Available upon request

---

*Last Updated: February 2026*
