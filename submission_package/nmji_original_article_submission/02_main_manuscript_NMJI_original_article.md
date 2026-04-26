# AI-assisted evidence mapping and prioritisation of preventive and disease-modifying strategies for Parkinson disease: an evidence-to-discovery study

## Abstract

**Background:** Parkinson disease is a growing cause of neurological disability. No intervention is established as curative, and few candidate strategies have been compared across clinical, mechanistic, translational, and public-health domains.

**Methods:** We conducted an evidence-to-discovery study integrating literature and trial evidence, ClinicalTrials.gov records, public transcriptomics, pathway enrichment, and transparent prioritisation. Candidate strategies were scored from 0 to 100 across human clinical evidence, mechanistic plausibility, genetics or omics support, safety, feasibility, and prevention relevance. Blood transcriptomic dataset GSE72267 was analysed with limma for Parkinson disease versus control differential expression, followed by Gene Ontology and Reactome enrichment of the top-ranked genes. Disease modules were then linked to modifiable intervention points and candidate actions.

**Results:** The highest-ranked strategies were pesticide-exposure reduction, structured aerobic or resistance exercise, glucagon-like peptide-1 receptor agonist pathways, Mediterranean or MIND-style dietary pattern, leucine-rich repeat kinase 2 inhibition, glucocerebrosidase or lysosomal modulation, head-injury prevention, and air-pollution reduction. Clinical-trial mining identified active and completed programmes across glucagon-like peptide-1 agonists, alpha-synuclein immunotherapies, leucine-rich repeat kinase 2 inhibitors, glucocerebrosidase or lysosomal therapies, cell or gene therapies, mitochondrial approaches, and anti-inflammatory strategies. In GSE72267, 22,277 probes were tested across 40 Parkinson disease and 19 control blood samples; no probe met the prespecified false-discovery-rate threshold for differential expression. Exploratory enrichment nevertheless highlighted immune and stress-response pathways.

**Conclusion:** The framework prioritises intervention points rather than claiming prevention or cure. The most immediately actionable low-risk package is regular exercise, reduced pesticide exposure, head-injury prevention, metabolic-health optimisation, healthy dietary pattern, and lower air-pollution exposure where feasible. Pharmacological candidates, including glucagon-like peptide-1 receptor agonists, leucine-rich repeat kinase 2 inhibitors, glucocerebrosidase or lysosomal modulators, and alpha-synuclein-directed strategies, require confirmatory trials before clinical adoption.

**Keywords:** Parkinson disease; disease modification; prevention; drug repurposing; transcriptomics; India

## Introduction

Parkinson disease is a major and increasing cause of disability worldwide.<sup>1</sup> Current therapies improve symptoms, but they do not establish prevention, cure, or confirmed disease modification.<sup>2</sup> Candidate interventions now span lifestyle measures, environmental risk reduction, repurposed metabolic drugs, genetically anchored therapies, and immune or proteinopathy-directed approaches. The difficulty is not a lack of hypotheses, but the absence of a transparent framework for comparing them across clinical evidence, biological plausibility, translational readiness, and public-health relevance.

Several disease modules are repeatedly implicated in Parkinson disease, including alpha-synuclein aggregation, mitochondrial dysfunction, lysosomal-autophagy impairment, neuroinflammation, and genetic susceptibility. Environmental exposures such as pesticides and air pollution may interact with these vulnerabilities, while exercise and metabolic health may modify physiological reserve. Glucagon-like peptide-1 receptor agonists have drawn attention after encouraging trial signals,<sup>3,4</sup> whereas major alpha-synuclein antibody studies have not shown clear efficacy.<sup>5,6</sup> Leucine-rich repeat kinase 2 and glucocerebrosidase pathways remain attractive because they are genetically and mechanistically anchored.<sup>7</sup>

We therefore aimed to identify and prioritise preventive and disease-modifying intervention points for Parkinson disease by integrating evidence mapping, clinical-trial mining, public transcriptomics, pathway analysis, and translational judgement, with explicit consideration of relevance to healthcare in India.

## Methods

### Study design

We conducted an artificial intelligence-assisted evidence-to-discovery study combining evidence mapping, clinical-trial mining, transparent scoring, public transcriptomic analysis, pathway enrichment, and pathway-to-intervention mapping.

### Evidence sources and eligibility

Evidence sources included biomedical literature, ClinicalTrials.gov records, public Gene Expression Omnibus datasets, pathway resources, and drug-target resources. Search concepts covered Parkinson disease, prevention, disease-modifying therapy, alpha-synuclein, leucine-rich repeat kinase 2, glucocerebrosidase, mitochondrial dysfunction, neuroinflammation, glucagon-like peptide-1 receptor agonists, exercise, diet, pesticides, air pollution, head injury, stem-cell therapy, gene therapy, and drug repurposing. Priority was given to systematic reviews, meta-analyses, randomised trials, cohort studies, Mendelian-randomisation analyses, public omics studies, mechanistic studies with translational relevance, and registered clinical trials. Narrative claims without traceable support were not used for scoring.

### Data extraction and prioritisation

For each candidate intervention or target, we extracted study design, population, intervention or exposure, comparator, outcomes, effect direction, mechanistic rationale, trial phase, safety concerns, and translational feasibility. Candidates were scored on a 0 to 100 scale across six domains: human clinical evidence (30 points), mechanistic plausibility (20), genetics or omics support (15), safety or tolerability (15), feasibility or scalability (10), and prevention or public-health relevance (10). Scores of 80 to 100 were classified as high translational priority, 60 to 79 as promising but requiring validation, 40 to 59 as biologically interesting with weak current human evidence, and below 40 as low current priority.

The primary outputs were the ranked intervention list, pathway-to-intervention map, trial landscape, transcriptomic differential-expression results, enrichment results, target benchmark, compound-triage matrix, and validation-model mapping. Where available from the generated analyses, numerical effect estimates are reported as scores, sample counts, fold-enrichment values, false-discovery-rate adjusted p values, benchmark scores and triage counts. Clinical effect sizes from individual trials or observational studies were not recalculated because individual participant data and harmonised outcome definitions were not available within this evidence-to-discovery workflow.

### Clinical-trial mining

ClinicalTrials.gov version 2 API searches targeted glucagon-like peptide-1 receptor agonists, alpha-synuclein antibodies or vaccines, leucine-rich repeat kinase 2 inhibitors, glucocerebrosidase or lysosomal therapies, stem-cell therapies, gene therapies, mitochondrial approaches, and anti-inflammatory therapies.<sup>8</sup> Extracted variables included trial identifier, intervention, phase, recruitment status, sample size, completion date, and results availability.

### Transcriptomic and pathway analysis

Public blood transcriptomic dataset GSE72267 was downloaded from the Gene Expression Omnibus.<sup>9,10</sup> Samples were labelled as Parkinson disease or control using deposited metadata. Expression data were quality checked and analysed with limma empirical Bayes modelling for differential expression. Multiple testing was controlled with the Benjamini-Hochberg false discovery rate. The prespecified significance threshold was false discovery rate below 0.05 with absolute log2 fold-change at least 0.25. The top-ranked 500 genes were then explored with Gene Ontology biological-process enrichment and Reactome pathway enrichment. Reactome results were treated as exploratory because leading adjusted p values did not remain below 0.05.

Computational analyses were performed in R 4.5.3 and Python using reproducible scripts retained with the analysis files. R packages included GEOquery, limma, clusterProfiler and ReactomePA for transcriptomic and enrichment analyses.

### Pathway-to-intervention framework and Indian relevance

Disease modules were mapped to intervention points and concrete actions. Modules included environmental toxicant biology, exercise-responsive metabolic and inflammatory reserve, glucagon-like peptide-1 signalling, innate immune signalling, leucine-rich repeat kinase 2 biology, glucocerebrosidase or lysosomal dysfunction, alpha-synuclein aggregation, and mitochondrial quality control. Relevance to India was considered in relation to pesticide exposure, occupational and rural surveillance, physical activity promotion, dietary quality, metabolic risk, air pollution, head-injury prevention, and implementation through primary care or non-communicable disease services.

### Downstream translational benchmarking

To extend pathway-level prioritisation into experimentally actionable outputs, we integrated the prioritised modules with protein-structure annotation, tractability and chemistry fields, cell-type context, assay mapping, and knowledge-graph exports generated in the downstream benchmark workspace. Inputs included UniProt, Protein Data Bank or AlphaFold structural availability, ChEMBL activity records, Human Protein Atlas context flags, and experimentally oriented model-assay mappings. We also reviewed cross-dataset pathway recurrence across GSE72267 blood and substantia nigra datasets GSE7621 and GSE20163 to identify themes recurring beyond a single dataset.

### Ethics

This study used public literature, public trial metadata, and de-identified public transcriptomic data. No new human participants were recruited and no identifiable patient information was collected; therefore institutional ethics approval and individual consent were not required for this analysis.

## Results

### Evidence yield

The workflow identified 1,248 records, 936 records after deduplication, 214 full-text or source records assessed, and 86 records retained for evidence mapping (Fig 1). Exclusion categories included duplicates, non-Parkinson populations, wrong outcomes, unsupported narrative claims, and mechanistic-only reports without translational linkage.

### Prioritised intervention points

The highest-ranked strategies were pesticide-exposure reduction, structured aerobic or resistance exercise, glucagon-like peptide-1 receptor agonists, Mediterranean or MIND-style dietary pattern, leucine-rich repeat kinase 2 inhibition, glucocerebrosidase or lysosomal modulation, head-injury prevention, air-pollution reduction, alpha-synuclein immunotherapy, and mitochondrial modulators (Table 1). Scores ranged from 52 to 83 out of 100. Two interventions reached the high-priority range: pesticide-exposure reduction (83/100) and structured exercise (82/100). Six additional strategies scored 60 to 72 and were classified as promising but requiring validation.

This ranking distinguished biological importance from translational readiness. Alpha-synuclein remained central to pathogenesis, but present clinical evidence lowered its immediate class-level priority because major antibody trials were mixed or negative.<sup>3,4</sup> By contrast, pesticide-exposure reduction and exercise ranked highly because they combine plausibility, safety, modifiability, and likely scalability.

### Pathway-to-intervention framework

The framework highlighted three broad translational layers. First, public-health and risk-reduction strategies targeted potentially modifiable exposures and physiological reserve through safer pesticide practices, structured exercise, head-injury prevention, metabolic optimisation, dietary quality, and lower air-pollution exposure where feasible. Second, biologically specific disease-modifying strategies centred on glucagon-like peptide-1 pathways, leucine-rich repeat kinase 2 inhibition, and glucocerebrosidase or lysosomal modulation. Third, lower-confidence but biologically important approaches included alpha-synuclein-directed strategies, broad anti-inflammatory approaches, and mitochondrial modulators. These module-to-action links are summarised in Fig 2.

### Clinical-trial landscape

Clinical-trial mining identified 59 records across the prespecified therapeutic categories, with a total planned or reported enrolment of 6,274 participants, median category size of 8 records, and trial sample sizes ranging from 0 to 601. Category counts were 8 records each for glucagon-like peptide-1-related searches, alpha-synuclein immunotherapy, glucocerebrosidase or lysosomal therapies, stem-cell strategies, gene therapy and mitochondrial approaches, 7 for anti-inflammatory approaches, and 4 for leucine-rich repeat kinase 2 inhibitor searches. Glucagon-like peptide-1 receptor agonists remained one of the most visible repurposing classes after the lixisenatide and exenatide trials.<sup>3,4</sup> Leucine-rich repeat kinase 2 inhibitors were in active clinical development and represented one of the clearest genetically anchored pipelines.<sup>7</sup> Alpha-synuclein immunotherapies, glucocerebrosidase-directed therapies, cell or gene therapies, mitochondrial strategies, and anti-inflammatory approaches remained important but heterogeneous components of the current development landscape.<sup>11</sup>

### Transcriptomic and pathway findings

GSE72267 contained 59 blood samples: 40 Parkinson disease and 19 control samples. Limma tested 22,277 probes. No probe met the prespecified false-discovery-rate and fold-change threshold, arguing against overinterpretation of this dataset as a robust standalone blood signature. Gene Ontology enrichment of the top-ranked genes nevertheless identified lymph node development (6 genes; fold enrichment 14.03; adjusted p=0.011) and cellular senescence (11 genes; fold enrichment 4.87; adjusted p=0.032). Exploratory Reactome analysis highlighted neuroimmune and stress-response themes including Signaling by NTRK1 (10 genes; fold enrichment 3.56; adjusted p=0.142), Netrin-1 signalling (6 genes; fold enrichment 5.86; adjusted p=0.142), MAP kinase activation (7 genes; fold enrichment 4.55; adjusted p=0.142), Toll-like receptor TLR6:TLR2 cascade (9 genes; fold enrichment 3.32; adjusted p=0.142), interleukin-17 signalling (7 genes; fold enrichment 4.04; adjusted p=0.142) and NOD1/2 signalling (5 genes; fold enrichment 5.69; adjusted p=0.142). The volcano plot for this analysis is shown in Fig 3.

### Downstream target benchmark and recurrence evidence

The downstream benchmark converged on a high-priority validation set comprising SNCA, GLP1R, LRRK2, GBA1, MAPK1, NOD2, IL17A, TLR2, NTRK1, and SLC6A3, with benchmark consensus scores ranging from 69.1 to 77.1 out of 100. The leading target scores were SNCA 77.1, GLP1R 77.0, LRRK2 76.9, GBA1 75.5, MAPK1 75.4, NOD2 74.0, IL17A 73.8, TLR2 70.9, NTRK1 70.4 and SLC6A3 69.1. These nodes linked the pathway-level results to specific experimental systems, including dopaminergic-neuron, microglial, and co-culture models with assayable endpoints such as phospho-Rab10, glucocerebrosidase activity, alpha-synuclein burden, cytokine release, neurite survival, and mitochondrial stress readouts. The associated knowledge graph contained 138 nodes and 125 edges linking targets, pathways, compounds, model systems, and evidence types.

Cross-dataset recurrence analysis across GSE72267, GSE7621, and GSE20163 showed that although robust differential-expression signals were inconsistent at the single-gene level, broader biological themes recurred across datasets. The strongest recurring signals included cytoplasmic translation (recurrence in 2 datasets; adjusted p=5.66 x 10^-29; 94 genes), ribonucleoprotein complex biogenesis (2 datasets; adjusted p=1.81 x 10^-9; 84 genes), regulation of apoptotic signalling (2 datasets; adjusted p=3.38 x 10^-9; 74 genes), protein localisation to nucleus (2 datasets; adjusted p=1.55 x 10^-7; 62 genes), ribosome biogenesis (2 datasets; adjusted p=3.64 x 10^-7; 58 genes), and regulation of oxidative-stress-induced intrinsic apoptotic signalling (2 datasets; adjusted p=3.99 x 10^-6; 22 genes). These findings strengthened the interpretation that pathway-level convergence was more reproducible than any single blood expression hit.

### Drug-repurposing candidates

Among computationally prioritised candidates, lixisenatide, exenatide, leucine-rich repeat kinase 2 inhibitors, ambroxol, N-acetylcysteine, and anti-inflammatory comparators represented the main repurposing landscape. Their ranking reflected a balance between human evidence, biological plausibility, safety, and feasibility rather than a recommendation for clinical use (Fig 4).

The downstream chemical triage layer reviewed 48 manually curated compound records. Six were retained for deeper review, whereas 42 were explicitly classified as comparator-only or do-not-prioritise records because of polypharmacology, selectivity, or weak disease-modifying rationale. In the larger ChEMBL-derived screening layer, 305 activity records were retained for selectivity and safety review; after curation, 31 were classified as comparator-not-disease-modifying, 11 as exclude-or-comparator, 5 as manual-review-selectivity and 1 as repurposing-review-only. This step was important because superficially high-scoring compounds were often inappropriate as therapeutic leads once selectivity and mechanism were considered.

## Discussion

This study identified intervention priorities for Parkinson disease by integrating heterogeneous evidence rather than privileging a single data source. The main finding is that the strongest immediate opportunities are not necessarily the most molecularly novel ones. Exercise, reduction of pesticide exposure, head-injury prevention, metabolic health, dietary quality and air-pollution mitigation are attractive because they are low-risk, scalable and relevant to wider health systems. In contrast, pharmacological disease modification remains more biologically specific but less ready for clinical adoption, with glucagon-like peptide-1 receptor agonist pathways, leucine-rich repeat kinase 2 inhibition and glucocerebrosidase or lysosomal modulation representing the most coherent trial-facing candidates.

The ranking also separates biological centrality from practical readiness. Alpha-synuclein remains fundamental to Parkinson disease biology, but the recent experience of antibody trials argues against treating alpha-synuclein immunotherapy as an immediately actionable class. Similarly, mitochondrial and inflammatory pathways are biologically plausible but have a history of broad, non-specific therapeutic approaches producing inconsistent clinical results. By placing these mechanisms in lower-confidence tiers, the framework avoids the common translational error of converting mechanistic plausibility directly into therapeutic recommendation.

The negative differential-expression result in GSE72267 was important. It reduced the risk of overstating blood transcriptomic findings and supported a cautious interpretation: pathway-level immune and stress-response signals may be hypothesis-generating, but they are not confirmatory on their own. This distinction matters because translational prioritisation is often distorted when weak omics signals are presented as definitive evidence. The cross-dataset recurrence layer partly mitigated this by showing that broader processes such as translation, protein localisation, apoptotic signalling and oxidative-stress-related pathways recurred across more than one dataset, even when single-gene findings were inconsistent.

The framework aligned with existing trial literature for lixisenatide and exenatide,<sup>3,4</sup> with the disappointing experience of major alpha-synuclein antibody programmes,<sup>5,6</sup> and with exercise data relevant to symptom progression and feasibility.<sup>12</sup> It also provides an explanation for why different intervention types should be judged by different standards. Public-health strategies should be judged by plausibility, safety, affordability, feasibility and population benefit, whereas investigational drug strategies require target engagement, patient selection, biomarker response and clinical endpoints before they can be considered for practice.

The Indian relevance is direct. Pesticide safety, occupational exposure surveillance, head-injury prevention, air-quality action, physical activity and metabolic-health promotion are already public-health concerns in India. Parkinson disease prevention cannot currently be promised at the individual level, but these measures fit existing primary-care, occupational-health and non-communicable disease platforms. This makes them more feasible than specialist-only prevention programmes. A practical implementation model would combine rural exposure history, counselling on safer pesticide handling, community physical-activity promotion, fall and road-injury prevention, diabetes and obesity care, and referral pathways for prodromal or early Parkinson disease evaluation.

The downstream analyses made the framework more actionable. Instead of stopping at pathway nomination, the project connected high-priority modules to tractable targets, candidate assays, cell models, compound-triage filters and a structured knowledge graph. This additional layer reinforced glucagon-like peptide-1 signalling, leucine-rich repeat kinase 2, glucocerebrosidase or lysosomal biology, alpha-synuclein and neuroimmune pathways as validation-ready modules. For laboratory planning, the most defensible next experiments are genotype-informed dopaminergic-neuron assays for leucine-rich repeat kinase 2 and glucocerebrosidase biology, metabolic or inflammatory stress models for glucagon-like peptide-1 agonists, alpha-synuclein aggregation assays and microglia-neuron co-culture systems for innate immune pathways.

The compound-triage results are also clinically important. A simple potency-ranked list would have promoted several compounds with poor disease-modifying rationale or broad polypharmacology. Manual curation reduced this risk by distinguishing candidate leads from comparators and do-not-prioritise records. This is particularly relevant for repurposing research, where familiar drugs or potent in vitro compounds can appear attractive despite weak causal relevance, limited brain exposure, safety concerns or unsuitable target selectivity.

The study has limitations. It was an evidence-to-discovery analysis rather than a registered systematic review, and some prioritisation steps still depended on transparent expert judgement. Automated evidence retrieval cannot replace a librarian-assisted systematic search with formal risk-of-bias assessment. The transcriptomic component relied on public datasets with differences in tissue source, platform, sample size and metadata quality. The GSE72267 analysis used blood and therefore could not fully represent substantia nigra biology. Drug-repurposing outputs remained hypothesis-generating, and all pharmacological candidates require experimental and prospective clinical validation.

The practical message is that Parkinson disease prevention and disease modification should be pursued through two linked agendas. The public-health agenda should focus on low-risk measures with broader health value, especially exercise, safer pesticide exposure, metabolic health, head-injury prevention and air-quality improvement. The trial agenda should focus on genetically or biologically anchored disease-modifying strategies with clear target engagement and biomarker plans. Neither agenda establishes cure or individual-level prevention, but together they identify where evidence, policy and future trials should concentrate.

## Conclusions

This evidence-to-discovery study prioritised intervention points for Parkinson disease by integrating clinical evidence, public-health feasibility, transcriptomics, pathway analysis, target benchmarking, compound triage and validation-model mapping. The strongest immediately actionable priorities are exercise promotion, pesticide-exposure reduction, head-injury prevention, metabolic-health optimisation, healthy dietary patterns and air-pollution reduction where feasible. The strongest research priorities are glucagon-like peptide-1 signalling, leucine-rich repeat kinase 2 inhibition, glucocerebrosidase or lysosomal modulation, alpha-synuclein biology and selected neuroimmune pathways. These findings should guide policy-relevant prevention research and biomarker-rich validation studies, but they do not justify claims of cure, individual-level prevention or off-label pharmacological treatment.

## Acknowledgements

Data availability: Generated analysis files, figures, and supporting materials are available within the project package together with public mirrors hosted on Kaggle and Hugging Face. Public source data are available from the cited Gene Expression Omnibus accession, ClinicalTrials.gov records, and referenced literature.

Artificial intelligence disclosure: Artificial intelligence-assisted tools were used within the evidence-mapping and prioritisation workflow. All extracted evidence, analyses, interpretations, and manuscript text required and received human review before inclusion in the submission package.

Funding and competing interests: Insert final author-approved declarations on the title page and in the submission system.

## References

1. Dorsey ER, Elbaz A, Nichols E, Abbasi N, Abd-Allah F, Abdelalim A, et al. Global, regional, and national burden of Parkinson's disease, 1990-2016: a systematic analysis for the Global Burden of Disease Study 2016. *Lancet Neurol*. 2018;17(11):939-953. doi:10.1016/S1474-4422(18)30295-3
2. Fox SH, Katzenschlager R, Lim SY, Barton B, de Bie RMA, Seppi K, et al. International Parkinson and Movement Disorder Society evidence-based medicine review: update on treatments for the motor symptoms of Parkinson's disease. *Mov Disord*. 2018;33(8):1248-1266. doi:10.1002/mds.27372
3. Meissner WG, Remy P, Giordana C, Maltete D, Derkinderen P, Houeto JL, et al. Trial of lixisenatide in early Parkinson's disease. *N Engl J Med*. 2024;390(13):1176-1185. doi:10.1056/NEJMoa2312323
4. Athauda D, Maclagan K, Skene SS, Bajwa-Joseph M, Letchford D, Chowdhury K, et al. Exenatide once weekly versus placebo in Parkinson's disease: a randomised, double-blind, placebo-controlled trial. *Lancet*. 2017;390(10103):1664-1675. doi:10.1016/S0140-6736(17)31585-4
5. Pagano G, Taylor KI, Anzures-Cabrera J, Marchesi M, Simuni T, Marek K, et al. Trial of prasinezumab in early-stage Parkinson's disease. *N Engl J Med*. 2022;387(5):421-432. doi:10.1056/NEJMoa2202867
6. Lang AE, Siderowf AD, Macklin EA, Poewe W, Brooks DJ, Fernandez HH, et al. Trial of cinpanemab in early Parkinson's disease. *N Engl J Med*. 2022;387(5):408-420. doi:10.1056/NEJMoa2203395
7. Jennings D, Huntwork-Rodriguez S, Henry AG, Sasaki JC, Meisner R, Diaz D, et al. Preclinical and clinical evaluation of the LRRK2 inhibitor DNL201 for Parkinson's disease. *Sci Transl Med*. 2022;14(648):eabj2658. doi:10.1126/scitranslmed.abj2658
8. ClinicalTrials.gov API [Internet]. Bethesda (MD): National Library of Medicine; 2026 [cited 2026 Apr 26]. Available from: https://clinicaltrials.gov/data-api/api
9. Calligaris R, Banica M, Roncaglia P, Robotti E, Finaurini S, Vlachouli C, et al. Blood transcriptomics of drug-naive sporadic Parkinson's disease patients. *BMC Genomics*. 2015;16:876. doi:10.1186/s12864-015-2058-3
10. National Center for Biotechnology Information. Gene Expression Omnibus accession GSE72267 [Internet]. Bethesda (MD): National Library of Medicine; 2015 [cited 2026 Apr 26]. Available from: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE72267
11. McFarthing K, Buff S, Rafaloff G, Pitzer K, Fiske B, Navangul A, et al. Parkinson's Disease Drug Therapies in the Clinical Trial Pipeline: 2024 Update. *J Parkinsons Dis*. 2024;14(5):899-912. doi:10.3233/JPD-240272
12. Schenkman M, Moore CG, Kohrt WM, Hall DA, Delitto A, Comella CL, et al. Effect of high-intensity treadmill exercise on motor symptoms in patients with de novo Parkinson disease: a phase 2 randomized clinical trial. *JAMA Neurol*. 2018;75(2):219-226. doi:10.1001/jamaneurol.2017.3517

## Tables

**Table 1. Prioritised intervention points for Parkinson disease prevention and disease-modification research**

| Intervention point | Main target or pathway | Score (0-100) | Objective evidence available from this workflow | Classification |
|---|---|---:|---|---|
| Pesticide-exposure reduction | Paraquat, rotenone and occupational exposures | 83 | Highest prevention/public-health score; clinical effect size not recalculated | High translational priority |
| Structured aerobic or resistance exercise | Exercise-responsive neuroplasticity and metabolic reserve | 82 | High safety and feasibility scores; clinical effect size not recalculated | High translational priority |
| Glucagon-like peptide-1 receptor agonist pathways | Metabolic and neuroimmune signalling | 72 | 8 GLP-1-related trial records; trial sample sizes in mined records ranged from 5 to 90 | Promising but needs validation |
| Mediterranean or MIND-style dietary pattern | Metabolic, vascular and inflammatory pathways | 66 | 8-week diet/microbiome trial record in ClinicalTrials.gov mining; causal Parkinson disease effect size not recalculated | Promising but needs validation |
| Leucine-rich repeat kinase 2 inhibition | Leucine-rich repeat kinase 2 kinase pathway | 64 | 4 LRRK2-related trial records; downstream benchmark LRRK2 score 76.9/100 | Promising but needs validation |
| Glucocerebrosidase or lysosomal modulation | GBA1, glucocerebrosidase and lysosomal biology | 62 | 8 GBA/lysosomal trial records; downstream benchmark GBA1 score 75.5/100 | Promising but needs validation |
| Head-injury prevention | Traumatic brain injury and neuroinflammatory priming | 61 | Public-health plausibility and safety support; Parkinson disease-specific effect size not recalculated | Promising but needs validation |
| Air-pollution reduction | Particulate matter, inflammation and oxidative stress | 60 | Public-health plausibility and safety support; individual-level Parkinson disease effect size not recalculated | Promising but needs validation |
| Alpha-synuclein immunotherapy | Aggregated alpha-synuclein | 54 | 8 alpha-synuclein immunotherapy/mining records; SNCA benchmark score 77.1/100; major antibody trials did not establish efficacy | Biologically important but weak current human evidence |
| Mitochondrial modulators | Oxidative phosphorylation and PINK1-Parkin biology | 52 | 8 mitochondrial trial records; PINK1 validation score 78.7/100 in extension matrix | Biologically important but weak current human evidence |

All scores are prioritisation metrics for research and policy discussion; they are not clinical recommendations.

Abbreviations: GBA1, glucocerebrosidase gene; GLP-1, glucagon-like peptide-1; MIND, Mediterranean-DASH Intervention for Neurodegenerative Delay; PINK1, PTEN-induced kinase 1.

## Figure Legends

**Figure 1. Evidence flow for the prioritisation workflow.** Automated retrieval, deduplication, screening, source assessment, and final inclusion in the evidence map.

**Figure 2. Pathway-to-intervention network.** Parkinson disease modules linked to modifiable intervention points and candidate interventions.

**Figure 3. GSE72267 differential-expression volcano plot.** Limma analysis of Parkinson disease versus control blood transcriptomics.

**Figure 4. Drug-repurposing candidate landscape.** Candidate compounds ranked by target-pathway relevance, supporting evidence, safety, and feasibility.
