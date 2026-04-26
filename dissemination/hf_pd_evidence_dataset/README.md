---
license: cc-by-4.0
language:
  - en
tags:
  - biology
  - biomedical
  - parkinsons-disease
  - neuroscience
  - bioinformatics
  - transcriptomics
  - clinical-trials
  - drug-repurposing
  - public-health
  - network-analysis
  - tabular
task_categories:
  - tabular-classification
  - feature-extraction
  - text-classification
pretty_name: "Parkinson's Disease Evidence-to-Discovery Prioritisation Dataset"
size_categories:
  - n<1K
---

# Parkinson's Disease Evidence-to-Discovery Prioritisation Dataset

This Hugging Face dataset package contains processed research assets from an AI-assisted evidence synthesis and computational validation project on Parkinson's disease (PD) prevention and disease-modifying therapeutic strategy prioritisation.

## Dataset Summary

The dataset integrates:

- evidence-priority scores for PD prevention and disease-modification candidates;
- pathway-to-intervention framework;
- individual and public-health prevention measures;
- ClinicalTrials.gov mining outputs;
- GSE72267 blood transcriptomic differential-expression outputs;
- GO biological-process enrichment;
- exploratory ReactomePA enrichment;
- drug-repurposing candidate rankings;
- multi-omics expansion inventory and pathway-recurrence gap map;
- public NCBI GEO/GDS discovery results for candidate brain, blood, proteomics, metabolomics, methylation and single-cell datasets;
- genetic causal-triangulation and variant-to-pathway scoring matrices with Open Targets and GWAS Catalog API outputs;
- drug-discovery deepening outputs covering LINCS access status, ChEMBL selectivity, ADMET/BBB triage, docking readiness and ClinicalTrials.gov trial gaps;
- experimental-validation work packages with assays, controls and go/no-go criteria;
- publication figures, scripts, tables, manuscript files, reference audits, and reproducibility logs.

The dataset is intended for research, education, validation, reproducibility, and hypothesis generation. It does not claim that a cure has been found.

## Dataset Structure

```text
data/
  processed/
    candidate_interventions_ranked.csv
    pathway_intervention_framework.csv
    individual_prevention_measures.csv
    evidence_map.csv
  clinical_trials/
    clinical_trials_landscape.csv
  omics/
    GSE72267_limma_DEG_all.csv
    GSE72267_DEG_summary.csv
    GSE72267_GO_BP_enrichment_top500.csv
    GSE72267_Reactome_enrichment_top500_exploratory.csv
  drug_repurposing/
    drug_repurposing_candidates.csv
  omics_expansion/
    multi_omics_dataset_inventory.csv
    multi_tissue_pathway_recurrence.csv
    omics_modality_gap_map.csv
    public_multiomics_dataset_discovery.csv
  genetics/
    genetic_causal_triangulation_matrix.csv
    variant_to_pathway_scoring.csv
    opentargets_pd_association_scores.csv
    gwas_catalog_pd_gene_summary.csv
    gwas_catalog_pd_target_overlap.csv
  drug_discovery_deepening/
    drug_discovery_deepening_matrix.csv
    docking_readiness.csv
    clinical_trial_gap_map.csv
    chembl_compound_selectivity_summary.csv
    clinicaltrials_public_api_gap_query.csv
figures/
scripts/
manuscript/
tables/
reproducibility/
validation_work_packages/
references_audit.csv
```

Public API modules have been executed where possible. Formal colocalisation, Mendelian randomisation, LINCS/Connectivity Map signature reversal, patent/freedom-to-operate review and decision-grade docking remain labelled as blocked where required inputs, credentials or specialist workflows are not available.

## Current Key Findings

The highest-priority candidates in the current scoring framework were:

1. pesticide-exposure reduction;
2. structured aerobic/resistance exercise;
3. GLP-1 receptor pathway strategies;
4. Mediterranean/MIND-style dietary pattern;
5. LRRK2 inhibition;
6. GBA/lysosomal modulation;
7. head-injury prevention;
8. air-pollution reduction.

GSE72267 limma analysis tested 22,277 probes across 40 PD and 19 control blood samples. No probes met the prespecified FDR < 0.05 and absolute log2 fold-change >= 0.25 threshold. GO and Reactome outputs are therefore exploratory and hypothesis-generating.

## Repository and CI

The GitHub repository with version-controlled evidence assets, scripts, manuscript files, reproducibility checks, and CI validation is available at:

https://github.com/hssling/parkinsons-evidence-to-discovery-prioritisation

The repository CI runs a lightweight validation script that checks required release assets, intervention-ranking integrity, cautionary clinical-claim language, and NMJI reference ordering.

## Intended Uses

- Validate or modify the evidence scoring rubric.
- Reanalyse pathway-intervention rankings.
- Extend drug-repurposing prioritisation.
- Reproduce GSE72267 omics analysis.
- Teach biomedical evidence synthesis workflows.
- Generate hypotheses for future PD prevention or disease-modification studies.

## Out-of-Scope Uses

This dataset must not be used as:

- a diagnostic tool;
- clinical decision support;
- a treatment recommendation system;
- evidence that any intervention cures PD;
- evidence that investigational or repurposed drugs should be used outside approved indications or clinical trials.

## Data Sources

Upstream resources include public literature records, ClinicalTrials.gov, GEO accession GSE72267, GO, Reactome, and manually curated source-backed references. See `references_audit.csv` and `reproducibility/methods_log.md`.

## Licensing

Generated processed data, code, figures, and documentation are released under CC BY 4.0. Users must respect terms and citation requirements of upstream resources.

## Citation

Please cite this dataset and the upstream resources listed in `references_audit.csv`.
