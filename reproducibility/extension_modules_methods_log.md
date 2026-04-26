# Extension Modules Methods Log

Generated on: 2026-04-26

## Scope

This log covers phase 2-5 extension outputs: multi-omics expansion, genetic causal triangulation, drug-discovery deepening and experimental-validation work packages.

## Input Sources

- Local benchmark target table: `../PD_Discovery_Benchmark_Dashboard/data/pd_discovery_target_benchmark.csv`
- Local validation matrix: `../PD_Discovery_Benchmark_Dashboard/data/experimental_validation_matrix.csv`
- Local multi-dataset pathway recurrence outputs: `../PD_Discovery_Benchmark_Dashboard/data/omics_recurrence/`
- Local target-extension Open Targets, ChEMBL, structure and compound files: `../PD_Target_to_Intervention_Discovery_Extension/data/`

## Interpretation Guardrails

- Completed transcriptomic recurrence outputs are retained as exploratory unless independently replicated.
- GWAS colocalisation, Mendelian randomisation, eQTL/pQTL mapping and LINCS/Connectivity Map analyses are marked `ready_not_executed` where summary statistics or service outputs have not been run in this repository.
- Docking is marked decision-grade only when experimental structures and relevant ligands are available; AlphaFold-only docking is treated as hypothesis-generating.
- Drug outputs are target and repurposing triage only, not clinical treatment recommendations.
- Wet-lab work packages are validation plans with go/no-go criteria; they do not establish efficacy.
