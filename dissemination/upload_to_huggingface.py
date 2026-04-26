"""Upload a prepared dataset folder to the Hugging Face Hub.

Usage:
  python upload_to_huggingface.py --repo-id USER_OR_ORG/parkinsons-evidence-to-discovery-prioritisation --path hf_pd_evidence_dataset
"""

from __future__ import annotations

import argparse
from pathlib import Path

from huggingface_hub import HfApi


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", required=True, help="Hugging Face dataset repo id, e.g. username/repo-name")
    parser.add_argument("--path", default="hf_pd_evidence_dataset", help="Prepared dataset folder")
    parser.add_argument("--private", action="store_true", help="Create/upload as private")
    args = parser.parse_args()

    folder = Path(args.path).resolve()
    if not folder.exists():
        raise FileNotFoundError(folder)

    api = HfApi()
    api.create_repo(repo_id=args.repo_id, repo_type="dataset", private=args.private, exist_ok=True)
    api.upload_folder(
        repo_id=args.repo_id,
        repo_type="dataset",
        folder_path=str(folder),
        commit_message="Add Parkinson's disease evidence-to-discovery dataset package",
    )
    print(f"Uploaded {folder} to https://huggingface.co/datasets/{args.repo_id}")


if __name__ == "__main__":
    main()

