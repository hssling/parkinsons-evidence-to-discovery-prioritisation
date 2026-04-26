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
- `figures/graphical_abstract_pathway_to_intervention.png`
- `manuscript/manuscript_full_publication_ready.docx`
- `references_audit.csv`

## Summary Of Current Findings

The highest-ranked prevention or disease-modification candidates were pesticide-exposure reduction, structured exercise, GLP-1 receptor pathway strategies, Mediterranean/MIND-style dietary pattern, LRRK2 inhibition, GBA/lysosomal modulation, head-injury prevention, and air-pollution reduction.

GSE72267 limma analysis included 40 PD and 19 control blood samples. No probes met the prespecified FDR < 0.05 and absolute log2 fold-change >= 0.25 threshold. GO and Reactome outputs are therefore best interpreted as hypothesis-generating pathway exploration, not definitive molecular validation.

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
