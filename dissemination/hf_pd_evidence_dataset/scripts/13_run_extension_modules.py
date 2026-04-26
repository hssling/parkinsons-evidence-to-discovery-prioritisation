"""Generate phase 2-5 extension outputs for the PD evidence project.

The script consolidates existing local benchmark outputs into submission-grade
tables for multi-omics expansion, genetic triangulation, drug-discovery
deepening and wet-lab validation planning. Analyses that need external summary
statistics or licensed services are marked as readiness/gap outputs, not as
completed evidence.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent
BENCHMARK = PARENT / "PD_Discovery_Benchmark_Dashboard"
EXTENSION = PARENT / "PD_Target_to_Intervention_Discovery_Extension"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def fnum(value: object, default: float = 0.0) -> float:
    try:
        if value in ("", None):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def yn(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def load_inputs() -> dict[str, list[dict[str, str]]]:
    return {
        "benchmark": read_csv(BENCHMARK / "data" / "pd_discovery_target_benchmark.csv"),
        "validation": read_csv(BENCHMARK / "data" / "experimental_validation_matrix.csv"),
        "omics_summary": read_csv(BENCHMARK / "data" / "omics_recurrence" / "multi_dataset_omics_summary.csv"),
        "pathway_recurrence": read_csv(BENCHMARK / "data" / "omics_recurrence" / "pd_multi_dataset_pathway_recurrence.csv"),
        "opentargets": read_csv(EXTENSION / "data" / "processed" / "opentargets_search_summary.csv"),
        "compounds": read_csv(EXTENSION / "data" / "chemical" / "prioritised_compound_shortlist.csv"),
        "structures": read_csv(EXTENSION / "data" / "protein" / "uniprot_structure_summary.csv"),
    }


def build_multiomics(inputs: dict[str, list[dict[str, str]]]) -> None:
    tissue_lookup = {
        "GSE72267": ("blood", "bulk transcriptomics", "executed"),
        "GSE7621": ("substantia nigra", "bulk transcriptomics", "executed"),
        "GSE20163": ("substantia nigra", "bulk transcriptomics", "executed"),
    }
    inventory: list[dict[str, object]] = []
    for row in inputs["omics_summary"]:
        tissue, modality, status = tissue_lookup.get(row["dataset"], ("not classified", "bulk transcriptomics", row.get("status", "")))
        inventory.append(
            {
                "dataset_or_modality": row["dataset"],
                "tissue_or_source": tissue,
                "omics_layer": modality,
                "platform": row.get("platform", ""),
                "samples": row.get("samples", ""),
                "pd_n": row.get("pd_n", ""),
                "control_n": row.get("control_n", ""),
                "feature_count": row.get("probes", ""),
                "analysis_status": status,
                "current_result": f"DEG_FDR05_logFC025={row.get('deg_FDR05_logFC025', '')}; GO_terms_q025={row.get('go_terms_q025', '')}",
                "next_action": "retain as completed recurrence input",
            }
        )

    planned_layers = [
        ("brain proteomics", "substantia nigra/cortex/CSF where available", "proteomics"),
        ("blood or plasma proteomics", "blood/plasma/serum", "proteomics"),
        ("brain or plasma metabolomics", "brain/CSF/plasma/serum", "metabolomics"),
        ("blood/brain methylation", "blood and disease-relevant brain regions", "DNA methylation"),
        ("single-cell or single-nucleus brain atlas", "substantia nigra/midbrain/cortex", "single-cell transcriptomics"),
        ("iPSC neuron or microglia perturbation datasets", "iPSC-derived neurons/microglia/co-culture", "cell-model transcriptomics"),
    ]
    for name, tissue, layer in planned_layers:
        inventory.append(
            {
                "dataset_or_modality": name,
                "tissue_or_source": tissue,
                "omics_layer": layer,
                "platform": "to be selected",
                "samples": "",
                "pd_n": "",
                "control_n": "",
                "feature_count": "",
                "analysis_status": "ready_for_import_not_executed",
                "current_result": "not yet analysed in this repository",
                "next_action": "select public dataset, harmonise metadata, run differential/abundance analysis and pathway recurrence",
            }
        )
    write_csv(ROOT / "data" / "omics_expansion" / "multi_omics_dataset_inventory.csv", inventory)

    recurrence_rows = []
    for row in inputs["pathway_recurrence"][:100]:
        count = int(fnum(row.get("dataset_recurrence_count")))
        recurrence_rows.append(
            {
                "pathway": row.get("Description", ""),
                "dataset_recurrence_count": count,
                "best_adjusted_p": row.get("p.adjust", ""),
                "gene_count": row.get("Count", ""),
                "recurrence_score": row.get("recurrence_score", ""),
                "current_tissue_scope": "blood plus substantia nigra transcriptomic recurrence",
                "interpretation": "recurrent exploratory pathway signal" if count >= 2 else "single-dataset exploratory signal",
                "next_confirmation_layer": "test recurrence in proteomics, metabolomics, methylation and single-cell datasets",
            }
        )
    write_csv(ROOT / "data" / "omics_expansion" / "multi_tissue_pathway_recurrence.csv", recurrence_rows)

    gap_rows = [
        {
            "omics_layer": row["omics_layer"],
            "current_status": row["analysis_status"],
            "minimum_acceptance_criteria": "case-control metadata, disease-relevant tissue/cell type, documented batch variables, usable public identifiers",
            "planned_effect_size": "log2 fold-change, standardised mean difference or pathway enrichment score as appropriate",
            "guardrail": "separate confirmatory recurrence from exploratory single-dataset findings",
        }
        for row in inventory
    ]
    write_csv(ROOT / "data" / "omics_expansion" / "omics_modality_gap_map.csv", gap_rows)


def build_genetics(inputs: dict[str, list[dict[str, str]]]) -> None:
    ot = {row["symbol"]: row for row in inputs["opentargets"]}
    gene_support = {
        "SNCA": ("high", "PD GWAS/familial alpha-synuclein locus; aggregation pathway anchor", "alpha-synuclein aggregation"),
        "LRRK2": ("high", "PD GWAS and monogenic kinase locus; strong variant-to-target support", "kinase/lysosomal stress"),
        "GBA1": ("high", "major PD risk gene with lysosomal biology link", "lysosomal glucocerebrosidase pathway"),
        "PINK1": ("high_familial", "familial recessive PD gene; mitophagy anchor", "mitochondrial quality control"),
        "PRKN": ("high_familial", "familial recessive PD gene; mitophagy anchor", "mitochondrial quality control"),
        "MAPK1": ("moderate_pathway", "pathway-central inflammatory/stress kinase; requires locus-level triangulation", "MAPK stress signalling"),
        "NOD2": ("moderate_pathway", "immune innate-sensing hypothesis; requires colocalisation or MR support", "innate immune activation"),
        "IL17A": ("moderate_pathway", "immune cytokine hypothesis; requires causal triangulation", "Th17/neuroinflammation"),
        "TLR2": ("moderate_pathway", "microglial innate immune hypothesis; requires locus-level triangulation", "TLR signalling"),
        "MYD88": ("moderate_pathway", "adapter in TLR/IL1 inflammatory signalling; pathway support", "TLR/IL1 signalling"),
    }
    rows = []
    variant_rows = []
    for target in inputs["benchmark"]:
        symbol = target["symbol"]
        support, rationale, pathway = gene_support.get(
            symbol,
            ("low_to_moderate", "not yet genetically triangulated in this repository", target.get("module", "")),
        )
        ensembl = target.get("ensembl_id") or ot.get(symbol, {}).get("ensembl_id", "")
        rows.append(
            {
                "symbol": symbol,
                "module": target.get("module", ""),
                "ensembl_id": ensembl,
                "opentargets_status": ot.get(symbol, {}).get("opentargets_status", "not_imported"),
                "gwas_target_support": support,
                "gwas_rationale": rationale,
                "colocalisation_status": "ready_not_executed",
                "colocalisation_inputs_needed": "PD GWAS summary statistics plus tissue-matched eQTL/pQTL summary statistics",
                "mendelian_randomisation_status": "ready_not_executed",
                "mr_use_case": "target-mediated MR if cis instruments exist; exposure MR for pesticide/air-pollution/metabolic/activity hypotheses",
                "eqtl_pqtl_mapping_status": "ready_not_executed",
                "variant_to_pathway_score_0_100": variant_score(support, fnum(target.get("benchmark_consensus_score_0_100"))),
                "interpretation": "causal-priority candidate" if support.startswith("high") else "requires genetic triangulation before causal claim",
            }
        )
        variant_rows.append(
            {
                "symbol": symbol,
                "primary_pathway": pathway,
                "variant_evidence_class": support,
                "pathway_biological_plausibility": target.get("module", ""),
                "benchmark_consensus_score_0_100": target.get("benchmark_consensus_score_0_100", ""),
                "variant_to_pathway_score_0_100": variant_score(support, fnum(target.get("benchmark_consensus_score_0_100"))),
                "next_analysis": "map risk variants to genes, test colocalisation, add cis-eQTL/cis-pQTL and pathway burden where possible",
            }
        )
    write_csv(ROOT / "data" / "genetics" / "genetic_causal_triangulation_matrix.csv", rows)
    write_csv(ROOT / "data" / "genetics" / "variant_to_pathway_scoring.csv", variant_rows)


def variant_score(support: str, benchmark_score: float) -> int:
    base = {
        "high": 90,
        "high_familial": 82,
        "moderate_pathway": 58,
        "low_to_moderate": 42,
    }.get(support, 40)
    return round(0.65 * base + 0.35 * benchmark_score)


def build_drug_discovery(inputs: dict[str, list[dict[str, str]]]) -> None:
    compounds_by_symbol: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inputs["compounds"]:
        compounds_by_symbol[row["symbol"]].append(row)
    structures = {row["symbol"]: row for row in inputs["structures"]}
    rows = []
    docking_rows = []
    trial_rows = []
    for target in inputs["benchmark"]:
        symbol = target["symbol"]
        compounds = sorted(compounds_by_symbol.get(symbol, []), key=lambda r: fnum(r.get("compound_priority_score_0_100")), reverse=True)
        top = compounds[0] if compounds else {}
        top_name = top.get("molecule_pref_name") or top.get("molecule_label") or top.get("molecule_pref_name_detail") or "no_compound_in_shortlist"
        pdb_count = int(fnum(target.get("pdb_count") or structures.get(symbol, {}).get("pdb_count")))
        ligand_count = int(fnum(target.get("ligand_count")))
        alphafold = bool(target.get("alphafold_url") or yn(structures.get(symbol, {}).get("alphafold_available")))
        docking_status = docking_readiness(pdb_count, ligand_count, alphafold)
        safety_flags = safety_flag(top)
        rows.append(
            {
                "symbol": symbol,
                "module": target.get("module", ""),
                "chembl_target_id": target.get("chembl_target_id", ""),
                "ligand_count": ligand_count,
                "top_compound": top_name,
                "top_compound_chembl_id": top.get("molecule_chembl_id", ""),
                "top_potency_nM": top.get("standard_value", ""),
                "compound_priority_score_0_100": top.get("compound_priority_score_0_100", ""),
                "chembl_selectivity_status": "potency_available_selectivity_not_curated" if compounds else "no_shortlist_compound",
                "lincs_connectivity_map_status": "ready_not_executed",
                "signature_reversal_input_needed": "validated disease signature from recurrent brain/blood/cell-model omics",
                "admet_toxicity_filter": safety_flags,
                "bbb_rule_score_0_6": top.get("bbb_rule_score_0_6", ""),
                "cns_like_flag": top.get("cns_like_flag", ""),
                "docking_status": docking_status,
                "patent_repurposing_feasibility": feasibility(top, target),
                "clinical_trial_gap": clinical_gap(symbol, target, bool(compounds)),
                "interpretation": "drug-discovery triage candidate; not a treatment recommendation",
            }
        )
        docking_rows.append(
            {
                "symbol": symbol,
                "pdb_count": pdb_count,
                "alphafold_available": alphafold,
                "ligand_count": ligand_count,
                "docking_readiness": docking_status,
                "recommended_docking_scope": docking_scope(symbol, pdb_count, ligand_count, alphafold),
            }
        )
        trial_rows.append(
            {
                "symbol": symbol,
                "module": target.get("module", ""),
                "current_evidence_role": target.get("role", ""),
                "trial_gap": clinical_gap(symbol, target, bool(compounds)),
                "next_trial_or_preclinical_step": target.get("recommended_next_experiment", ""),
                "guardrail": "requires preclinical validation and regulatory review before clinical translation",
            }
        )
    write_csv(ROOT / "data" / "drug_discovery_deepening" / "drug_discovery_deepening_matrix.csv", rows)
    write_csv(ROOT / "data" / "drug_discovery_deepening" / "docking_readiness.csv", docking_rows)
    write_csv(ROOT / "data" / "drug_discovery_deepening" / "clinical_trial_gap_map.csv", trial_rows)


def safety_flag(compound: dict[str, str]) -> str:
    if not compound:
        return "not_available"
    flags = []
    if fnum(compound.get("black_box_warning")) > 0:
        flags.append("black_box_warning")
    if yn(compound.get("withdrawn_flag")):
        flags.append("withdrawn_flag")
    if fnum(compound.get("lipinski_violations")) > 1:
        flags.append("lipinski_violations")
    if not yn(compound.get("cns_like_flag")):
        flags.append("not_cns_like_by_rule")
    return ";".join(flags) if flags else "no_major_rule_based_flag"


def docking_readiness(pdb_count: int, ligand_count: int, alphafold: bool) -> str:
    if pdb_count > 0 and ligand_count > 0:
        return "credible_structure_and_ligands_available"
    if pdb_count > 0:
        return "credible_structure_available_ligand_set_limited"
    if alphafold and ligand_count > 0:
        return "alphafold_only_hypothesis_generating"
    if alphafold:
        return "alphafold_only_low_priority"
    return "not_ready"


def docking_scope(symbol: str, pdb_count: int, ligand_count: int, alphafold: bool) -> str:
    if pdb_count > 0 and ligand_count > 0:
        return "dock curated ligand analogues against disease-relevant experimental structures with redocking controls"
    if alphafold:
        return "avoid decision-grade docking; use only as exploratory model after pocket validation"
    return "defer docking until credible structure is available"


def feasibility(compound: dict[str, str], target: dict[str, str]) -> str:
    if not compound:
        return "target_level_only; requires chemotype and patent review"
    if fnum(compound.get("max_phase")) >= 4:
        return "approved_drug_repurposing_possible_but_indication_patent_and_safety_review_required"
    if fnum(compound.get("max_phase")) >= 2:
        return "clinical_stage_candidate; patent and freedom-to-operate review required"
    return "preclinical_or_tool_compound; repurposing feasibility uncertain"


def clinical_gap(symbol: str, target: dict[str, str], has_compounds: bool) -> str:
    if symbol == "GLP1R":
        return "trial_signal_exists; need mechanism, subgroup and long-term disease-modification confirmation"
    if symbol == "LRRK2":
        return "genetically anchored; need safety, target engagement and mutation-stratified trial evidence"
    if symbol in {"GBA1", "SNCA"}:
        return "strong biological rationale; need target engagement and disease-modification evidence"
    if has_compounds:
        return "compound tractability exists; PD-specific efficacy gap remains"
    return "preclinical validation gap before drug-development triage"


def build_validation_work_packages(inputs: dict[str, list[dict[str, str]]]) -> None:
    rows = []
    for idx, row in enumerate(inputs["validation"], start=1):
        model_type = infer_model_type(row.get("model", ""), row.get("module", ""))
        rows.append(
            {
                "work_package_id": f"WP{idx:02d}",
                "symbol": row.get("symbol", ""),
                "module": row.get("module", ""),
                "model_type": model_type,
                "experimental_model": row.get("model", ""),
                "primary_assays": row.get("primary_assay", ""),
                "secondary_endpoints": secondary_endpoints(row.get("symbol", ""), row.get("module", "")),
                "positive_controls": positive_controls(row.get("symbol", "")),
                "negative_controls": "vehicle control; isogenic corrected or wild-type control where applicable; non-targeting guide/siRNA for perturbation assays",
                "toxicity_counterscreen": "cell viability, neurite integrity, apoptosis/necrosis markers, mitochondrial stress and off-target inflammatory activation",
                "go_criteria": go_criteria(row.get("symbol", "")),
                "no_go_criteria": "no reproducible target engagement, worsening viability/inflammation, or discordant results across independent clones/batches",
                "replication_plan": "minimum two independent iPSC lines or donors per genotype where feasible, blinded image analysis, technical triplicates and independent replication",
                "recommended_next_experiment": row.get("recommended_next_experiment", ""),
            }
        )
    write_csv(ROOT / "validation_work_packages" / "experimental_validation_work_packages.csv", rows)
    write_validation_markdown(rows)


def infer_model_type(model: str, module: str) -> str:
    text = f"{model} {module}".lower()
    if "co-culture" in text:
        return "neuron-microglia or metabolic/inflammatory co-culture"
    if "microglia" in text:
        return "microglia inflammatory model"
    if "organoid" in text:
        return "midbrain organoid model"
    if "dopaminergic" in text or "ipsc" in text:
        return "iPSC-derived dopaminergic neuron model"
    if "mitochond" in text:
        return "mitochondrial stress and mitophagy cell model"
    return "target-matched cellular validation model"


def secondary_endpoints(symbol: str, module: str) -> str:
    if symbol in {"PINK1", "PRKN", "NDUFS3"}:
        return "Seahorse respiration, mitophagy flux, mitochondrial membrane potential, ROS, neurite survival"
    if symbol in {"TLR2", "MYD88", "NOD2", "IL17A"}:
        return "IL-1beta/TNF/IL-6 release, NF-kB activation, phagocytosis, neuronal bystander toxicity"
    if symbol in {"GBA1", "LAMP2"}:
        return "lysosomal pH, GCase/lysosomal enzyme activity, lipid storage, alpha-synuclein burden"
    if symbol == "SNCA":
        return "pS129 alpha-synuclein, aggregate seeding, synaptic marker preservation, neurite length"
    if symbol == "LRRK2":
        return "phospho-Rab10/Rab12, lysosomal morphology, mitochondrial function, neurite survival"
    return "target engagement, neuronal survival, inflammatory markers and mitochondrial respiration"


def positive_controls(symbol: str) -> str:
    mapping = {
        "SNCA": "alpha-synuclein PFF seeding for phenotype induction; known aggregation-modifying control where available",
        "LRRK2": "validated LRRK2 inhibitor with phospho-Rab10 reduction",
        "GBA1": "ambroxol or validated GCase modulator as assay-positive comparator",
        "GLP1R": "clinically used GLP-1 receptor agonist with receptor-engagement assay",
        "PINK1": "CCCP/mitochondrial depolarisation with mitophagy rescue control",
        "PRKN": "CCCP/mitochondrial depolarisation with Parkin translocation assay",
    }
    return mapping.get(symbol, "literature-supported pathway agonist/inhibitor matched to assay biology")


def go_criteria(symbol: str) -> str:
    if symbol in {"SNCA", "LRRK2", "GBA1"}:
        return ">=25% improvement in primary disease-relevant endpoint with preserved viability and reproduced in independent line/batch"
    if symbol in {"TLR2", "MYD88", "NOD2", "IL17A"}:
        return ">=30% reduction in pathological cytokine/neurotoxicity readout without suppressing basal viability or causing broad toxicity"
    return "statistically robust target engagement plus directionally favourable survival, mitochondrial or inflammatory endpoint"


def write_validation_markdown(rows: list[dict[str, object]]) -> None:
    path = ROOT / "validation_work_packages" / "experimental_validation_work_packages.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Experimental Validation Work Packages",
        "",
        "These work packages convert prioritised PD targets into concrete preclinical validation modules. They are research plans, not clinical recommendations.",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"## {row['work_package_id']}. {row['symbol']} - {row['module']}",
                "",
                f"- Model: {row['experimental_model']}",
                f"- Model type: {row['model_type']}",
                f"- Primary assays: {row['primary_assays']}",
                f"- Secondary endpoints: {row['secondary_endpoints']}",
                f"- Positive controls: {row['positive_controls']}",
                f"- Negative controls: {row['negative_controls']}",
                f"- Toxicity counterscreen: {row['toxicity_counterscreen']}",
                f"- Go criteria: {row['go_criteria']}",
                f"- No-go criteria: {row['no_go_criteria']}",
                f"- Replication plan: {row['replication_plan']}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_methods_log() -> None:
    path = ROOT / "reproducibility" / "extension_modules_methods_log.md"
    text = f"""# Extension Modules Methods Log

Generated on: {date.today().isoformat()}

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
"""
    path.write_text(text, encoding="utf-8")


def main() -> None:
    inputs = load_inputs()
    build_multiomics(inputs)
    build_genetics(inputs)
    build_drug_discovery(inputs)
    build_validation_work_packages(inputs)
    write_methods_log()
    print("Phase 2-5 extension outputs generated.")


if __name__ == "__main__":
    main()
