# Data Dictionary

## `data/processed/candidate_interventions_ranked.csv`

- `intervention_or_target`: candidate intervention, exposure, drug class, or target.
- `primary_target_pathway`: main biological or public-health pathway.
- `human_clinical_30`: score out of 30 for human clinical evidence.
- `mechanistic_20`: score out of 20 for biological plausibility.
- `genetic_omics_15`: score out of 15 for genetic or omics support.
- `safety_15`: score out of 15 for safety/tolerability.
- `feasibility_10`: score out of 10 for scalability/implementation feasibility.
- `prevention_public_health_10`: score out of 10 for prevention/public-health relevance.
- `classification`: priority class using the predefined 0-100 rubric.
- `rationale`: short traceable interpretation.
- `priority_score_0_100`: total score.

## `data/processed/pathway_intervention_framework.csv`

- `pathway_module`: PD disease-biology or exposure module.
- `key_nodes`: major genes, proteins, exposures, or processes.
- `intervention_point`: modifiable biological or implementation point.
- `actual_interventions`: candidate real-world actions or therapies.
- `validation_in_current_project`: how the current package supports or contextualises the module.
- `evidence_position`: concise evidence interpretation.
- `implementation_level`: individual, clinical, occupational, policy, or trial level.
- `caution`: overclaiming guardrail.

## `data/processed/individual_prevention_measures.csv`

- `measure`: individual or public-health action.
- `evidence_message`: cautious evidence-based framing.
- `practical_priority`: 0-5 practical implementation priority.
- `level`: individual, occupational, clinical, or policy implementation level.

## `data/omics/GSE72267_limma_DEG_all.csv`

Limma output for GSE72267 PD versus control blood samples.

- `probe_id`: platform probe identifier.
- `logFC`: log2 fold-change, PD versus control.
- `AveExpr`: average expression.
- `t`: moderated t statistic.
- `P.Value`: nominal P value.
- `adj.P.Val`: Benjamini-Hochberg adjusted P value.
- `B`: log-odds of differential expression.
- gene annotation columns are inherited from the GEO platform annotation.

## `data/omics/GSE72267_GO_BP_enrichment_top500.csv`

GO biological-process enrichment over the top-ranked 500 GSE72267 genes.

## `data/omics/GSE72267_Reactome_enrichment_top500_exploratory.csv`

Exploratory ReactomePA enrichment over the top-ranked 500 GSE72267 genes. Leading adjusted P values were not below 0.05, so these are hypothesis-generating.

## `data/drug_repurposing/drug_repurposing_candidates.csv`

- `candidate`: drug or drug class.
- `target`: primary target or pathway.
- `pathway`: biological module.
- `signature_reversal_score`: directional hypothesis score; more negative means stronger expression-reversal hypothesis.
- `target_pathway_relevance_20`: target/pathway relevance score.
- `human_safety_10`: safety score.
- `BBB_or_CNS_plausibility_10`: central nervous system plausibility score.
- `repurposing_priority_0_100`: overall repurposing priority score.
- `notes`: interpretation and caution.

