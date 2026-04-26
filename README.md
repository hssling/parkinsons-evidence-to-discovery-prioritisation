# Parkinson's Disease Evidence-to-Discovery Prioritisation

This repository contains reproducible research assets from an AI-assisted evidence-to-discovery project on Parkinson's disease (PD) prevention, public-health translation, and disease-modifying strategy prioritisation.

The project integrates evidence mapping, ClinicalTrials.gov mining, public transcriptomics, GO/Reactome pathway enrichment, pathway-to-intervention mapping, drug-repurposing triage, manuscript assets, figures, and reproducibility audits.

The current extension release also adds structured phase 2-5 discovery assets for multi-omics expansion, genetic causal triangulation, drug-discovery deepening and experimental-validation work packages. Analyses not yet executed because they require external summary statistics, licensed services or new dataset selection are explicitly labelled as readiness or gap-mapping outputs.

## Scope

This repository is for research, education, validation, and hypothesis generation. It is not a diagnostic tool, clinical decision-support system, treatment recommendation system, or proof that any intervention prevents or cures Parkinson's disease.

## Key Outputs

- Ranked candidate intervention and target-priority tables
- Pathway-to-intervention framework
- Individual and public-health prevention-measure tables
- ClinicalTrials.gov mining output
- GSE72267 blood transcriptomic differential-expression results
- GO biological-process and exploratory Reactome enrichment outputs
- Drug-repurposing candidate ranking
- Publication figures and manuscript files
- NMJI original-article submission package
- Multi-omics expansion inventory and pathway-recurrence gap map
- Genetic causal-triangulation and variant-to-pathway matrices
- Drug-discovery deepening outputs covering LINCS readiness, ChEMBL/ADMET/BBB triage, docking readiness and trial gaps
- Experimental-validation work packages for iPSC dopaminergic neuron, microglia, organoid-compatible and co-culture follow-up
- Reproducibility logs and claim-audit files

## Repository Layout

```text
data/
  clinical_trials/      ClinicalTrials.gov mining outputs
  drug_repurposing/     Candidate drug-repurposing tables
  drug_discovery_deepening/
                         LINCS readiness, docking, ADMET/BBB and trial-gap maps
  genetics/              Genetic triangulation and variant-to-pathway scoring tables
  omics/                GSE72267 differential-expression and enrichment outputs
  omics_expansion/       Multi-omics dataset inventory and pathway recurrence outputs
  processed/            Evidence maps, intervention rankings and prevention tables
figures/                Publication figures
manuscript/             Manuscript source files and generated documents
reproducibility/        Quality checks, audit trail and methods logs
scripts/                Evidence, omics, figure and manuscript generation scripts
submission_package/     Journal-specific submission assets
tables/                 Spreadsheet exports
validation_work_packages/
                         Wet-lab validation work-package table and narrative plan
references_audit.csv    Source-backed reference audit
```

## Extension Outputs

Phase 2-5 outputs can be regenerated with:

```bash
python scripts/13_run_extension_modules.py
```

The generated files include:

- `data/omics_expansion/multi_omics_dataset_inventory.csv`
- `data/omics_expansion/multi_tissue_pathway_recurrence.csv`
- `data/genetics/genetic_causal_triangulation_matrix.csv`
- `data/genetics/variant_to_pathway_scoring.csv`
- `data/drug_discovery_deepening/drug_discovery_deepening_matrix.csv`
- `data/drug_discovery_deepening/docking_readiness.csv`
- `data/drug_discovery_deepening/clinical_trial_gap_map.csv`
- `validation_work_packages/experimental_validation_work_packages.csv`
- `validation_work_packages/experimental_validation_work_packages.md`
- `reproducibility/extension_modules_methods_log.md`

## Current Evidence Summary

The highest-ranked prevention and translational priorities are:

1. pesticide-exposure reduction;
2. structured aerobic/resistance exercise;
3. GLP-1 receptor pathway strategies;
4. Mediterranean/MIND-style dietary pattern;
5. LRRK2 inhibition;
6. GBA/lysosomal modulation;
7. head-injury prevention;
8. air-pollution reduction.

The omics analysis of GSE72267 tested 22,277 probes across 40 PD and 19 control blood samples. No probe met the prespecified FDR < 0.05 and absolute log2 fold-change >= 0.25 threshold. GO and Reactome results are therefore interpreted as exploratory and hypothesis-generating.

## Reproducibility

Run the lightweight validation used by continuous integration:

```bash
python scripts/12_validate_repository.py
```

The full R omics workflow requires R and Bioconductor dependencies:

```bash
Rscript scripts/04_omics_download_and_qc.R
Rscript scripts/05_differential_expression_meta_analysis.R
Rscript scripts/06_pathway_enrichment.R
```

## Roadmap

The next seven project extensions are tracked in `ROADMAP.md`:

1. systematic-review upgrade;
2. multi-omics expansion;
3. genetic causal triangulation;
4. drug-discovery deepening;
5. experimental-validation roadmap;
6. India-specific prevention framework;
7. living dashboard and automated updates.

## Public Mirrors

- Hugging Face Datasets: https://huggingface.co/datasets/hssling/parkinsons-evidence-to-discovery-prioritisation
- Kaggle Datasets: https://www.kaggle.com/datasets/jkhospital/parkinsons-evidence-to-discovery-prioritisation

## Related Benchmark Resource

The downstream target-to-intervention benchmark, knowledge graph, validation-model table, dashboard, compound triage outputs, and multi-dataset recurrence assets are available separately:

- GitHub: https://github.com/hssling/pd-discovery-benchmark-dashboard
- Hugging Face Datasets: https://huggingface.co/datasets/hssling/pd-discovery-benchmark-dashboard
- Kaggle Datasets: https://www.kaggle.com/datasets/jkhospital/pd-discovery-benchmark

## Citation

Please cite this repository, the public dataset mirrors, and the upstream sources listed in `references_audit.csv`. A `CITATION.cff` file is included for repository citation metadata.

## License

Generated code, tables, figures and documentation are released under CC BY 4.0 unless a file states otherwise. Users must respect the licences and citation requirements of upstream resources such as GEO, ClinicalTrials.gov, GO, Reactome and cited publications.
