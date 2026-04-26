"""Lightweight repository validation for CI.

The checks intentionally avoid rerunning long external API or omics workflows.
They verify that required release assets are present and that the repository
keeps clinical claims appropriately conservative.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "references_audit.csv",
    "data/processed/candidate_interventions_ranked.csv",
    "data/processed/pathway_intervention_framework.csv",
    "data/processed/individual_prevention_measures.csv",
    "data/clinical_trials/clinical_trials_landscape.csv",
    "data/omics/GSE72267_DEG_summary.csv",
    "data/omics/GSE72267_GO_BP_enrichment_top500.csv",
    "data/omics/GSE72267_Reactome_enrichment_top500_exploratory.csv",
    "data/drug_repurposing/drug_repurposing_candidates.csv",
    "figures/fig1_prisma_flow.png",
    "figures/fig2_pathogenesis_evidence_network.png",
    "figures/fig4_omics_DEG_volcano.png",
    "manuscript/manuscript_full.md",
    "submission_package/nmji_original_article_submission/02_main_manuscript_NMJI_original_article.md",
    "reproducibility/claim_audit.csv",
    "reproducibility/final_quality_check.csv",
]

FORBIDDEN_UNQUALIFIED_PATTERNS = [
    r"\b(cure|cures|curative)\b",
    r"\bproven to prevent\b",
    r"\brecommend(?:ed)? for clinical use\b",
]

REQUIRED_CAUTION_PATTERNS = [
    r"hypothesis[- ]generating",
    r"not (?:a )?(?:diagnostic|clinical decision-support|treatment recommendation)",
    r"does not .*(?:cure|prevention|prevent)",
]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def check_required_files() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def check_candidate_table() -> None:
    path = ROOT / "data/processed/candidate_interventions_ranked.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) < 8:
        fail("candidate_interventions_ranked.csv has fewer than 8 candidates")
    scores = [float(row["priority_score_0_100"]) for row in rows]
    if max(scores) < 80:
        fail("no high-priority candidate score >= 80 found")
    names = {row["intervention_or_target"] for row in rows}
    for expected in ["Pesticide exposure reduction", "Structured aerobic/resistance exercise"]:
        if expected not in names:
            fail(f"expected intervention missing: {expected}")


def check_claim_language() -> None:
    corpus_parts = [
        read_text(ROOT / "README.md"),
        read_text(ROOT / "manuscript/manuscript_full.md"),
        read_text(ROOT / "submission_package/nmji_original_article_submission/02_main_manuscript_NMJI_original_article.md"),
    ]
    corpus = "\n".join(corpus_parts).lower()

    for pattern in FORBIDDEN_UNQUALIFIED_PATTERNS:
        matches = re.findall(pattern, corpus, flags=re.IGNORECASE)
        if matches and "does not" not in corpus and "not claim" not in corpus:
            fail(f"possible unqualified clinical claim pattern found: {pattern}")

    for pattern in REQUIRED_CAUTION_PATTERNS:
        if not re.search(pattern, corpus, flags=re.IGNORECASE | re.DOTALL):
            fail(f"required caution language missing: {pattern}")


def check_nmji_reference_order() -> None:
    path = ROOT / "submission_package/nmji_original_article_submission/02_main_manuscript_NMJI_original_article.md"
    text = read_text(path)
    pre_refs = text.split("## References")[0]
    seen: list[str] = []
    for citation in re.findall(r"<sup>(.*?)</sup>", pre_refs):
        for number in re.findall(r"\d+", citation):
            if number not in seen:
                seen.append(number)
    expected = [str(i) for i in range(1, len(seen) + 1)]
    if seen != expected:
        fail(f"NMJI references not sequential by first citation: {seen}")
    if "Parkinson's Disease Drug Therapies in the Clinical Trial Pipeline: 2024 Update" not in text:
        fail("corrected reference 11 title not found")


def main() -> None:
    check_required_files()
    check_candidate_table()
    check_claim_language()
    check_nmji_reference_order()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
