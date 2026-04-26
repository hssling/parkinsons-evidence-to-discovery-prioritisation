# Parkinson's Disease Evidence-to-Discovery Prioritisation Dataset

This Kaggle-ready package contains processed research assets from an AI-assisted evidence synthesis and computational validation project on Parkinson's disease (PD) prevention and disease-modifying therapeutic strategy prioritisation.

## What Is Included

- Evidence-priority scores for candidate interventions and targets.
- Pathway-to-intervention framework linking PD biology to modifiable intervention points.
- Individual and public-health prevention measures.
- ClinicalTrials.gov mining outputs.
- GSE72267 blood transcriptomic analysis outputs.
- GO biological-process enrichment and exploratory Reactome pathway enrichment.
- Drug-repurposing candidate rankings.
- Multi-omics expansion inventory and pathway-recurrence gap map.
- Public NCBI GEO/GDS discovery results for candidate brain, blood, proteomics, metabolomics, methylation and single-cell datasets.
- Genetic causal-triangulation and variant-to-pathway scoring matrices with Open Targets and GWAS Catalog API outputs.
- Drug-discovery deepening outputs covering LINCS access status, ChEMBL selectivity, ADMET/BBB triage, docking readiness and ClinicalTrials.gov trial gaps.
- Experimental-validation work packages with assays, controls and go/no-go criteria.
- Publication-ready figures in PNG/SVG.
- Manuscript draft, tables, scripts, reference audit, and reproducibility logs.

## Key Files

- `data/processed/candidate_interventions_ranked.csv`
- `data/processed/pathway_intervention_framework.csv`
- `data/processed/individual_prevention_measures.csv`
- `data/clinical_trials/clinical_trials_landscape.csv`
- `data/omics/GSE72267_limma_DEG_all.csv`
- `data/omics/GSE72267_GO_BP_enrichment_top500.csv`
- `data/omics/GSE72267_Reactome_enrichment_top500_exploratory.csv`
- `data/drug_repurposing/drug_repurposing_candidates.csv`
- `data/omics_expansion/multi_omics_dataset_inventory.csv`
- `data/omics_expansion/multi_tissue_pathway_recurrence.csv`
- `data/omics_expansion/public_multiomics_dataset_discovery.csv`
- `data/genetics/genetic_causal_triangulation_matrix.csv`
- `data/genetics/variant_to_pathway_scoring.csv`
- `data/genetics/opentargets_pd_association_scores.csv`
- `data/genetics/gwas_catalog_pd_gene_summary.csv`
- `data/drug_discovery_deepening/drug_discovery_deepening_matrix.csv`
- `data/drug_discovery_deepening/docking_readiness.csv`
- `data/drug_discovery_deepening/chembl_compound_selectivity_summary.csv`
- `data/drug_discovery_deepening/clinicaltrials_public_api_gap_query.csv`
- `validation_work_packages/experimental_validation_work_packages.csv`
- `figures/graphical_abstract_pathway_to_intervention.png`
- `manuscript/manuscript_full_publication_ready.docx`
- `references_audit.csv`

## Summary Of Current Findings

The highest-ranked prevention or disease-modification candidates were pesticide-exposure reduction, structured exercise, GLP-1 receptor pathway strategies, Mediterranean/MIND-style dietary pattern, LRRK2 inhibition, GBA/lysosomal modulation, head-injury prevention, and air-pollution reduction.

GSE72267 limma analysis included 40 PD and 19 control blood samples. No probes met the prespecified FDR < 0.05 and absolute log2 fold-change >= 0.25 threshold. GO and Reactome outputs are therefore best interpreted as hypothesis-generating pathway exploration, not definitive molecular validation.

The extension release executes public API modules for NCBI GEO/GDS discovery, Open Targets, GWAS Catalog, ChEMBL and ClinicalTrials.gov. Formal colocalisation, Mendelian randomisation, eQTL/pQTL mapping, LINCS/Connectivity Map scoring, patent review and decision-grade docking remain labelled as blocked where required inputs, credentials or specialist workflows are not available.

## Repository and CI

The GitHub repository with version-controlled evidence assets, scripts, manuscript files, reproducibility checks, and CI validation is available at:

https://github.com/hssling/parkinsons-evidence-to-discovery-prioritisation

The repository CI runs a lightweight validation script that checks required release assets, intervention-ranking integrity, cautionary clinical-claim language, and NMJI reference ordering.

## Intended Use

This dataset is intended for:

- independent validation of the scoring framework;
- reanalysis of evidence-priority rankings;
- pathway/network analysis experimentation;
- teaching reproducible biomedical evidence synthesis;
- generating improved public-health or trial-prioritisation hypotheses.

## Not Intended For

- diagnosis;
- clinical decision support;
- treatment recommendation;
- drug-use recommendation outside approved indications;
- claims that any intervention prevents or cures PD.

## Suggested Kaggle Tags

`parkinsons-disease`, `neuroscience`, `bioinformatics`, `clinical-trials`, `drug-repurposing`, `public-health`, `transcriptomics`, `network-analysis`

## License

Released under CC BY 4.0 for the generated processed data, figures, documentation, and code authored in this project. Users must also respect the terms of upstream public resources including GEO, ClinicalTrials.gov, Reactome, GO, and cited literature.
