"""Execute public external-data queries for phase 2-5 extension modules.

This script runs the parts of the extension plan that are feasible with open
public APIs from the local workspace:

- Open Targets Platform target-disease association scores for Parkinson disease.
- GWAS Catalog v2 Parkinson disease association discovery and gene overlap.
- ChEMBL activity/selectivity summaries for shortlisted compounds.
- ClinicalTrials.gov v2 target/intervention trial-gap queries.
- NCBI GEO/GDS discovery searches for additional multi-omics datasets.

Restricted or input-dependent analyses remain explicitly blocked:
LINCS/Connectivity Map signature reversal needs CLUE/LINCS access and a
validated perturbation signature; formal colocalisation and MR need full GWAS
and QTL summary statistics or validated instruments.
"""

from __future__ import annotations

import csv
import json
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OPEN_TARGETS_URL = "https://api.platform.opentargets.org/api/v4/graphql"
GWAS_URL = "https://www.ebi.ac.uk/gwas/rest/api/v2/associations"
CHEMBL_ACTIVITY_URL = "https://www.ebi.ac.uk/chembl/api/data/activity.json"
CTGOV_URL = "https://clinicaltrials.gov/api/v2/studies"
NCBI_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
NCBI_ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PARKINSON_MONDO = "MONDO_0005180"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def http_json(url: str, *, data: dict[str, Any] | None = None, timeout: int = 45) -> dict[str, Any]:
    body = json.dumps(data).encode("utf-8") if data is not None else None
    headers = {"Content-Type": "application/json", "User-Agent": "pd-evidence-to-discovery/1.0"}
    request = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def query_open_targets(targets: list[dict[str, str]]) -> list[dict[str, Any]]:
    query = """
    query target($ensemblId: String!) {
      target(ensemblId: $ensemblId) {
        id
        approvedSymbol
        associatedDiseases(page: {index: 0, size: 200}) {
          rows {
            disease { id name }
            score
            datatypeScores { id score }
          }
        }
      }
    }
    """
    rows: list[dict[str, Any]] = []
    for target in targets:
        symbol = target["symbol"]
        ensembl = target.get("ensembl_id", "")
        if not ensembl:
            rows.append(error_row(symbol, "missing_ensembl_id"))
            continue
        try:
            payload = http_json(OPEN_TARGETS_URL, data={"query": query, "variables": {"ensemblId": ensembl}})
            target_data = payload.get("data", {}).get("target") or {}
            disease_rows = target_data.get("associatedDiseases", {}).get("rows", [])
            pd_rows = [r for r in disease_rows if r.get("disease", {}).get("id") == PARKINSON_MONDO or "Parkinson disease" in r.get("disease", {}).get("name", "")]
            selected = pd_rows[0] if pd_rows else {}
            datatype_scores = {item["id"]: item["score"] for item in selected.get("datatypeScores", [])}
            rows.append(
                {
                    "symbol": symbol,
                    "ensembl_id": ensembl,
                    "api_status": "ok",
                    "pd_disease_id": selected.get("disease", {}).get("id", ""),
                    "pd_disease_name": selected.get("disease", {}).get("name", ""),
                    "overall_association_score": selected.get("score", ""),
                    "genetic_association_score": datatype_scores.get("genetic_association", ""),
                    "affected_pathway_score": datatype_scores.get("affected_pathway", ""),
                    "literature_score": datatype_scores.get("literature", ""),
                    "datatype_scores_json": json.dumps(datatype_scores, sort_keys=True),
                }
            )
        except Exception as exc:  # noqa: BLE001 - persisted as audit output
            rows.append(error_row(symbol, f"{type(exc).__name__}: {exc}", ensembl))
        time.sleep(0.15)
    return rows


def error_row(symbol: str, status: str, ensembl: str = "") -> dict[str, Any]:
    return {
        "symbol": symbol,
        "ensembl_id": ensembl,
        "api_status": status,
        "pd_disease_id": "",
        "pd_disease_name": "",
        "overall_association_score": "",
        "genetic_association_score": "",
        "affected_pathway_score": "",
        "literature_score": "",
        "datatype_scores_json": "{}",
    }


def query_gwas_catalog(targets: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    url = GWAS_URL + "?" + urllib.parse.urlencode({"efo_trait": "Parkinson disease", "size": 200})
    payload = http_json(url)
    associations = payload.get("_embedded", {}).get("associations", [])
    target_symbols = {row["symbol"] for row in targets}
    association_rows: list[dict[str, Any]] = []
    gene_counter: Counter[str] = Counter()
    best_p: dict[str, float] = {}
    best_or: dict[str, str] = {}
    for assoc in associations:
        mapped_genes = assoc.get("mapped_genes") or []
        for gene in mapped_genes:
            gene_counter[gene] += 1
            p_value = assoc.get("p_value")
            if isinstance(p_value, (int, float)) and (gene not in best_p or p_value < best_p[gene]):
                best_p[gene] = p_value
                best_or[gene] = str(assoc.get("or_value", "") or assoc.get("beta", ""))
        if target_symbols.intersection(mapped_genes):
            association_rows.append(
                {
                    "association_id": assoc.get("association_id", ""),
                    "accession_id": assoc.get("accession_id", ""),
                    "mapped_genes": ";".join(mapped_genes),
                    "target_overlap": ";".join(sorted(target_symbols.intersection(mapped_genes))),
                    "p_value": assoc.get("p_value", ""),
                    "or_value": assoc.get("or_value", ""),
                    "beta": assoc.get("beta", ""),
                    "risk_variant": ";".join([item.get("rs_id", "") for item in assoc.get("snp_allele", [])]),
                    "reported_trait": ";".join(assoc.get("reported_trait", [])),
                    "first_author": assoc.get("first_author", ""),
                    "pubmed_id": assoc.get("pubmed_id", ""),
                }
            )
    gene_rows = []
    for target in targets:
        symbol = target["symbol"]
        gene_rows.append(
            {
                "symbol": symbol,
                "gwas_catalog_mapped_association_count": gene_counter.get(symbol, 0),
                "best_gwas_catalog_p_value": best_p.get(symbol, ""),
                "best_gwas_catalog_effect": best_or.get(symbol, ""),
                "gwas_catalog_status": "executed_public_api",
            }
        )
    return association_rows, gene_rows


def query_chembl_selectivity(drug_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in drug_rows:
        molecule_id = row.get("top_compound_chembl_id", "")
        if not molecule_id or molecule_id in seen:
            continue
        seen.add(molecule_id)
        params = {"molecule_chembl_id": molecule_id, "limit": 1000}
        try:
            payload = http_json(CHEMBL_ACTIVITY_URL + "?" + urllib.parse.urlencode(params))
            activities = payload.get("activities", [])
            targets = {activity.get("target_chembl_id", "") for activity in activities if activity.get("target_organism") == "Homo sapiens"}
            target_names = Counter(activity.get("target_pref_name", "") for activity in activities if activity.get("target_organism") == "Homo sapiens")
            potent = [
                activity
                for activity in activities
                if activity.get("target_organism") == "Homo sapiens"
                and parse_float(activity.get("standard_value")) <= 100
                and activity.get("standard_units") in {"nM", "NM", "nmol/L"}
            ]
            potent_targets = {activity.get("target_chembl_id", "") for activity in potent}
            rows.append(
                {
                    "molecule_chembl_id": molecule_id,
                    "molecule_name": row.get("top_compound", ""),
                    "query_status": "ok",
                    "human_target_count_any_activity": len([t for t in targets if t]),
                    "human_target_count_potent_100nM": len([t for t in potent_targets if t]),
                    "activity_record_count": len(activities),
                    "top_target_names": "; ".join([name for name, _ in target_names.most_common(8) if name]),
                    "selectivity_interpretation": selectivity_label(len(potent_targets), len(targets)),
                }
            )
        except Exception as exc:  # noqa: BLE001
            rows.append(
                {
                    "molecule_chembl_id": molecule_id,
                    "molecule_name": row.get("top_compound", ""),
                    "query_status": f"{type(exc).__name__}: {exc}",
                    "human_target_count_any_activity": "",
                    "human_target_count_potent_100nM": "",
                    "activity_record_count": "",
                    "top_target_names": "",
                    "selectivity_interpretation": "not_available",
                }
            )
        time.sleep(0.15)
    return rows


def parse_float(value: Any) -> float:
    try:
        if value in ("", None):
            return float("inf")
        return float(value)
    except (TypeError, ValueError):
        return float("inf")


def selectivity_label(potent_targets: int, all_targets: int) -> str:
    if potent_targets == 0 and all_targets == 0:
        return "no_human_activity_records_retrieved"
    if potent_targets <= 1 and all_targets <= 5:
        return "relatively_selective_by_public_activity_count"
    if potent_targets <= 5:
        return "moderate_polypharmacology"
    return "broad_polypharmacology_or_tool_compound"


def query_clinical_trials(targets: list[dict[str, str]], drug_rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    drug_lookup = {row["symbol"]: row for row in drug_rows}
    rows: list[dict[str, Any]] = []
    for target in targets:
        symbol = target["symbol"]
        compound = drug_lookup.get(symbol, {}).get("top_compound", "")
        term_parts = [symbol]
        if compound and compound != "no_compound_in_shortlist" and not compound.startswith("CHEMBL"):
            term_parts.append(compound)
        term = " OR ".join(term_parts)
        params = {
            "query.cond": "Parkinson Disease",
            "query.term": term,
            "pageSize": 25,
            "format": "json",
        }
        try:
            payload = http_json(CTGOV_URL + "?" + urllib.parse.urlencode(params))
            studies = payload.get("studies", [])
            status_counts: Counter[str] = Counter()
            phase_counts: Counter[str] = Counter()
            examples = []
            for study in studies:
                protocol = study.get("protocolSection", {})
                status = protocol.get("statusModule", {}).get("overallStatus", "")
                status_counts[status] += 1
                design = protocol.get("designModule", {})
                for phase in design.get("phases", []) or ["NOT_SPECIFIED"]:
                    phase_counts[phase] += 1
                ident = protocol.get("identificationModule", {})
                examples.append(f"{ident.get('nctId', '')}: {ident.get('briefTitle', '')}")
            rows.append(
                {
                    "symbol": symbol,
                    "query_term": term,
                    "ctgov_status": "ok",
                    "study_count_returned": len(studies),
                    "status_counts": json.dumps(dict(status_counts), sort_keys=True),
                    "phase_counts": json.dumps(dict(phase_counts), sort_keys=True),
                    "example_studies": " | ".join(examples[:5]),
                    "trial_gap_interpretation": trial_gap_label(len(studies), status_counts),
                }
            )
        except Exception as exc:  # noqa: BLE001
            rows.append(
                {
                    "symbol": symbol,
                    "query_term": term,
                    "ctgov_status": f"{type(exc).__name__}: {exc}",
                    "study_count_returned": "",
                    "status_counts": "{}",
                    "phase_counts": "{}",
                    "example_studies": "",
                    "trial_gap_interpretation": "not_available",
                }
            )
        time.sleep(0.15)
    return rows


def trial_gap_label(study_count: int, statuses: Counter[str]) -> str:
    if study_count == 0:
        return "no_pd_trial_found_for_target_query"
    if statuses.get("RECRUITING", 0) or statuses.get("ACTIVE_NOT_RECRUITING", 0):
        return "active_or_recruiting_pd_trial_signal"
    return "historical_pd_trial_signal_no_active_recruiting_hit_in_query"


def query_geo_discovery() -> list[dict[str, Any]]:
    searches = [
        ("brain transcriptomics", "Parkinson disease brain transcriptomics"),
        ("blood transcriptomics", "Parkinson disease blood transcriptomics"),
        ("proteomics", "Parkinson disease proteomics"),
        ("metabolomics", "Parkinson disease metabolomics"),
        ("DNA methylation", "Parkinson disease methylation"),
        ("single-cell transcriptomics", "Parkinson disease single cell substantia nigra"),
    ]
    rows: list[dict[str, Any]] = []
    for layer, term in searches:
        params = {"db": "gds", "term": term, "retmode": "json", "retmax": 10}
        try:
            search = http_json(NCBI_ESEARCH_URL + "?" + urllib.parse.urlencode(params))
            result = search.get("esearchresult", {})
            ids = result.get("idlist", [])
            summaries = {}
            if ids:
                sum_params = {"db": "gds", "id": ",".join(ids), "retmode": "json"}
                summaries = http_json(NCBI_ESUMMARY_URL + "?" + urllib.parse.urlencode(sum_params)).get("result", {})
            for gid in ids:
                summary = summaries.get(gid, {})
                rows.append(
                    {
                        "omics_layer": layer,
                        "search_term": term,
                        "ncbi_gds_id": gid,
                        "accession": summary.get("accession", ""),
                        "title": summary.get("title", ""),
                        "taxon": summary.get("taxon", ""),
                        "entry_type": summary.get("entrytype", ""),
                        "sample_count": summary.get("n_samples", ""),
                        "search_total_count": result.get("count", ""),
                        "discovery_status": "executed_public_api_dataset_discovery",
                    }
                )
        except Exception as exc:  # noqa: BLE001
            rows.append(
                {
                    "omics_layer": layer,
                    "search_term": term,
                    "ncbi_gds_id": "",
                    "accession": "",
                    "title": "",
                    "taxon": "",
                    "entry_type": "",
                    "sample_count": "",
                    "search_total_count": "",
                    "discovery_status": f"{type(exc).__name__}: {exc}",
                }
            )
        time.sleep(0.34)
    return rows


def update_existing_matrices(
    open_targets_rows: list[dict[str, Any]],
    gwas_gene_rows: list[dict[str, Any]],
    selectivity_rows: list[dict[str, Any]],
    trial_rows: list[dict[str, Any]],
) -> None:
    ot = {row["symbol"]: row for row in open_targets_rows}
    gwas = {row["symbol"]: row for row in gwas_gene_rows}
    trials = {row["symbol"]: row for row in trial_rows}
    selectivity = {row["molecule_chembl_id"]: row for row in selectivity_rows}

    genetics_path = ROOT / "data" / "genetics" / "genetic_causal_triangulation_matrix.csv"
    genetics = read_csv(genetics_path)
    for row in genetics:
        symbol = row["symbol"]
        row["opentargets_public_api_status"] = ot.get(symbol, {}).get("api_status", "")
        row["opentargets_pd_overall_score"] = ot.get(symbol, {}).get("overall_association_score", "")
        row["opentargets_pd_genetic_score"] = ot.get(symbol, {}).get("genetic_association_score", "")
        row["gwas_catalog_status"] = gwas.get(symbol, {}).get("gwas_catalog_status", "")
        row["gwas_catalog_mapped_association_count"] = gwas.get(symbol, {}).get("gwas_catalog_mapped_association_count", "")
        row["colocalisation_status"] = "blocked_requires_full_gwas_and_qtl_summary_statistics"
        row["mendelian_randomisation_status"] = "blocked_requires_validated_instruments_and_outcome_summary_statistics"
        row["eqtl_pqtl_mapping_status"] = "blocked_requires_tissue_matched_qtl_summary_statistics"
    write_csv(genetics_path, genetics)

    drug_path = ROOT / "data" / "drug_discovery_deepening" / "drug_discovery_deepening_matrix.csv"
    drug = read_csv(drug_path)
    for row in drug:
        molecule_id = row.get("top_compound_chembl_id", "")
        symbol = row["symbol"]
        row["chembl_selectivity_status"] = "executed_public_api" if molecule_id in selectivity else row["chembl_selectivity_status"]
        row["chembl_human_target_count_any_activity"] = selectivity.get(molecule_id, {}).get("human_target_count_any_activity", "")
        row["chembl_human_target_count_potent_100nM"] = selectivity.get(molecule_id, {}).get("human_target_count_potent_100nM", "")
        row["chembl_selectivity_interpretation"] = selectivity.get(molecule_id, {}).get("selectivity_interpretation", "")
        row["lincs_connectivity_map_status"] = "blocked_requires_lincs_clue_credentials_and_validated_signature"
        row["clinicaltrials_public_api_status"] = trials.get(symbol, {}).get("ctgov_status", "")
        row["clinicaltrials_pd_query_count"] = trials.get(symbol, {}).get("study_count_returned", "")
        row["clinical_trial_gap"] = trials.get(symbol, {}).get("trial_gap_interpretation", row.get("clinical_trial_gap", ""))
    write_csv(drug_path, drug)


def write_execution_log() -> None:
    path = ROOT / "reproducibility" / "public_external_execution_log.md"
    text = f"""# Public External Execution Log

Generated on: {date.today().isoformat()}

Executed public API modules:

- Open Targets Platform GraphQL API for target-Parkinson disease association scores.
- GWAS Catalog REST API v2 for Parkinson disease association discovery and target-gene overlap.
- ChEMBL activity API for public activity-count selectivity summaries of top compounds.
- ClinicalTrials.gov API v2 for target/intervention trial-gap query counts and example trials.
- NCBI E-utilities GEO/GDS search for candidate public multi-omics datasets.

Remaining blocked modules:

- Formal GWAS colocalisation: requires full PD GWAS summary statistics and matched eQTL/pQTL summary statistics.
- Mendelian randomisation: requires validated exposure or cis-target instruments plus compatible PD outcome summary statistics.
- LINCS/Connectivity Map signature reversal: requires validated disease/perturbation signature and CLUE/LINCS access.
- Patent/freedom-to-operate review: requires a dedicated patent database workflow and legal/technology-transfer review.
- Decision-grade docking: requires curated experimental structures, ligand preparation, redocking controls and assay-context validation.
"""
    path.write_text(text, encoding="utf-8")


def main() -> None:
    targets = read_csv(ROOT / "data" / "genetics" / "genetic_causal_triangulation_matrix.csv")
    drug_rows = read_csv(ROOT / "data" / "drug_discovery_deepening" / "drug_discovery_deepening_matrix.csv")

    open_targets_rows = query_open_targets(targets)
    gwas_assoc_rows, gwas_gene_rows = query_gwas_catalog(targets)
    selectivity_rows = query_chembl_selectivity(drug_rows)
    trial_rows = query_clinical_trials(targets, drug_rows)
    geo_rows = query_geo_discovery()

    write_csv(ROOT / "data" / "genetics" / "opentargets_pd_association_scores.csv", open_targets_rows)
    write_csv(ROOT / "data" / "genetics" / "gwas_catalog_pd_target_overlap.csv", gwas_assoc_rows)
    write_csv(ROOT / "data" / "genetics" / "gwas_catalog_pd_gene_summary.csv", gwas_gene_rows)
    write_csv(ROOT / "data" / "drug_discovery_deepening" / "chembl_compound_selectivity_summary.csv", selectivity_rows)
    write_csv(ROOT / "data" / "drug_discovery_deepening" / "clinicaltrials_public_api_gap_query.csv", trial_rows)
    write_csv(ROOT / "data" / "omics_expansion" / "public_multiomics_dataset_discovery.csv", geo_rows)
    update_existing_matrices(open_targets_rows, gwas_gene_rows, selectivity_rows, trial_rows)
    write_execution_log()
    print("Public external analyses executed.")


if __name__ == "__main__":
    main()
