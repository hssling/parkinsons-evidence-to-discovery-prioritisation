# Project Roadmap

This roadmap tracks the next seven extensions for the Parkinson's disease evidence-to-discovery project. The current NMJI submission and public dataset release are treated as the baseline release. Future work should preserve the current clinical guardrails: no claim of cure, no individual-level prevention guarantee, and no off-label treatment recommendation.

## Phase 1. Systematic-review Upgrade

Goal: Convert the current evidence-to-discovery workflow into a registered, librarian-assisted systematic review and evidence map.

Planned work:

- Draft protocol with explicit PICO/PECO questions for prevention, disease modification, repurposing and public-health implementation.
- Add PRISMA 2020 checklist and final PRISMA flow.
- Expand database coverage beyond the current evidence map, including PubMed/MEDLINE, Embase where accessible, CENTRAL, ClinicalTrials.gov, WHO ICTRP if feasible and key preprint/server checks where appropriate.
- Add dual-screening-ready extraction sheets.
- Add formal risk-of-bias tools by evidence type, such as RoB 2, ROBINS-I, AMSTAR 2 and Newcastle-Ottawa or equivalent.
- Add GRADE-style certainty summaries for the highest-priority prevention and trial candidates.
- Add sensitivity analysis of priority-score weights.

Deliverables:

- `protocol/`
- `data/search_results/systematic_review_search_log.csv`
- `data/extraction/risk_of_bias_assessment.csv`
- `tables/gRADE_summary_of_findings.xlsx`
- Updated manuscript methods and supplementary files.

## Phase 2. Multi-omics Expansion

Goal: Strengthen biological recurrence beyond a single blood transcriptomic dataset.

Planned work:

- Add multi-dataset transcriptomic meta-analysis across blood and brain datasets.
- Expand to substantia nigra, cortex, iPSC-derived neuron, microglia and single-cell datasets where metadata are parseable.
- Add proteomics, metabolomics, methylation and single-cell evidence where public datasets are robust enough.
- Quantify pathway recurrence across tissues and platforms.
- Separate confirmatory analyses from exploratory analyses.

Deliverables:

- `data/omics_recurrence/`
- `data/multiomics/`
- `figures/multiomics_recurrence_summary.png`
- `reproducibility/multiomics_methods_log.md`

## Phase 3. Genetic Causal Triangulation

Goal: Add causal and genetic support layers for prioritised intervention points and targets.

Planned work:

- Add GWAS-to-target mapping for PD risk loci.
- Add eQTL/pQTL colocalisation where credible summary statistics are available.
- Add Mendelian-randomisation modules for modifiable exposures such as smoking, pesticide exposure proxies where possible, air pollution proxies, metabolic traits, physical activity, BMI and diabetes.
- Add Open Targets evidence summaries.
- Add variant-to-pathway scoring for LRRK2, GBA1, SNCA, PINK1/PRKN and immune/metabolic modules.

Deliverables:

- `data/genetics/`
- `scripts/13_genetic_causal_triangulation.py`
- `tables/genetic_causal_support_matrix.xlsx`
- `figures/genetic_causal_evidence_map.png`

## Phase 4. Drug-discovery Deepening

Goal: Improve drug-repurposing and target-tractability evaluation beyond first-pass candidate ranking.

Planned work:

- Add LINCS/Connectivity Map signature-reversal scoring.
- Add ChEMBL selectivity and potency curation for shortlisted targets.
- Add ADMET and BBB/CNS plausibility heuristics with explicit limitations.
- Add docking only for targets with defensible structures and chemically relevant ligands.
- Add patent, availability, approval status and trial-feasibility review.
- Add clinical-trial gap mapping for top candidate classes.

Deliverables:

- `data/drug_discovery_deepening/`
- `scripts/14_drug_discovery_deepening.py`
- `tables/repurposing_candidate_triage_deep.xlsx`
- `figures/drug_repurposing_evidence_stack.png`

## Phase 5. Experimental-validation Roadmap

Goal: Convert prioritised pathways into actionable wet-lab validation work packages.

Planned work:

- Define iPSC dopaminergic-neuron validation modules for LRRK2, GBA1, SNCA, PINK1/PRKN and GLP1R-related hypotheses.
- Define microglia/neuron co-culture modules for TLR2, MYD88, NOD2, IL17A and MAPK-related inflammatory pathways.
- Define primary assays, secondary assays, positive controls, negative controls, toxicity counterscreens and go/no-go thresholds.
- Add sample-size and replication planning templates for experimental validation.
- Add model limitations and clinical-translation guardrails.

Deliverables:

- `validation_work_packages/`
- `tables/experimental_validation_work_packages.xlsx`
- `figures/validation_model_to_target_map.png`

## Phase 6. India-specific Prevention Framework

Goal: Convert prevention priorities into a practical, India-facing public-health research and implementation framework.

Planned work:

- Add pesticide exposure and occupational/rural surveillance framework.
- Add air-pollution, head-injury and metabolic-risk integration.
- Map prevention priorities to primary care, NCD clinics, occupational health and district public-health programmes.
- Add implementation indicators and feasibility scoring.
- Draft an India-specific policy brief and prevention research agenda.

Deliverables:

- `policy/india_prevention_framework.md`
- `data/public_health/india_prevention_indicator_matrix.csv`
- `figures/india_prevention_implementation_pathway.png`

## Phase 7. Living Dashboard and Automated Updates

Goal: Build a maintainable update system for evidence, trials, omics links and public dataset releases.

Planned work:

- Add scheduled trial-mining updates for ClinicalTrials.gov.
- Add PubMed query snapshots and evidence-map refresh logs.
- Add dashboard pages for interventions, trials, omics recurrence, target validation and claim audit.
- Add automated checks for new unsupported clinical claims.
- Add versioned releases to GitHub, Hugging Face and Kaggle.

Deliverables:

- `dashboard/`
- `.github/workflows/scheduled_update.yml`
- `data/update_logs/`
- Versioned GitHub releases and mirrored dataset updates.

## Disease-extension Backlog

Potential future disease areas for the same evidence-to-discovery path:

- Alzheimer disease and related dementias
- Amyotrophic lateral sclerosis
- Multiple sclerosis progression
- Stroke prevention and vascular cognitive impairment
- Major depressive disorder
- Type 2 diabetes complications
- Chronic kidney disease
- MASLD/non-alcoholic fatty liver disease
- COPD and air-pollution-related lung disease
- Tuberculosis host-directed therapy
