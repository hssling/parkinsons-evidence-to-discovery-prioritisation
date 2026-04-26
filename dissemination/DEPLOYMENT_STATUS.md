# Deployment Status

Deployment date: 2026-04-24

## Hugging Face

Status: uploaded successfully.

Repository:

https://huggingface.co/datasets/hssling/parkinsons-evidence-to-discovery-prioritisation

Type: dataset repository.

Notes:

- Uploaded with `huggingface_hub`.
- Dataset card is in `README.md`.
- This is a research dataset, not a trained model.
- README updated after GitHub repository creation to include the version-controlled repository and CI validation link.

## Kaggle

Status: public dataset created, full package uploaded, and file listing verified through Kaggle CLI.

Dataset:

https://www.kaggle.com/datasets/jkhospital/parkinsons-evidence-to-discovery-prioritisation

Notes:

- Initial Kaggle creation required title and subtitle shortening to satisfy Kaggle metadata limits.
- A second version was uploaded with `--dir-mode zip`; Kaggle file listing now shows nested dataset assets including processed data, omics outputs, figures, scripts, manuscript files, and tables.
- Kaggle rejected several custom tags as invalid; the dataset content and README still include the relevant biomedical keywords.
- README and dataset metadata updated after GitHub repository creation to include the version-controlled repository and CI validation link.

## GitHub Evidence Repository

Status: created and pushed successfully.

Repository:

https://github.com/hssling/parkinsons-evidence-to-discovery-prioritisation

Notes:

- Includes evidence tables, omics outputs, figures, scripts, manuscript assets, NMJI submission files, reproducibility logs, README, citation metadata, licence, and GitHub Actions CI.
- CI workflow: `.github/workflows/validate.yml`.
- Validator: `scripts/12_validate_repository.py`.

## Clinical/Scientific Caution

The dataset is for evidence synthesis, reproducibility, validation, teaching, and hypothesis generation. It is not a diagnostic tool, clinical decision-support model, or proof that any intervention prevents or cures Parkinson's disease.

## Linked Benchmark Release

The extended target-to-intervention benchmark and dashboard have been released separately as:

- GitHub release: https://github.com/hssling/pd-discovery-benchmark-dashboard/releases/tag/v1.0.0
- GitHub Zenodo-trigger release: https://github.com/hssling/pd-discovery-benchmark-dashboard/releases/tag/v1.0.1
- GitHub repository: https://github.com/hssling/pd-discovery-benchmark-dashboard
- Hugging Face Datasets: https://huggingface.co/datasets/hssling/pd-discovery-benchmark-dashboard
- Kaggle Datasets: https://www.kaggle.com/datasets/jkhospital/pd-discovery-benchmark

These linked outputs provide the target benchmark, compound triage matrix, validation-model table, knowledge graph, dashboard, and resource manuscript draft used for downstream validation planning.

## Springer Nature Submission Assets

Generated local DOCX submission package:

- Folder: `submission_package/springer_nature_jnt_subscription_submission/`
- ZIP: `submission_package/springer_nature_jnt_subscription_submission.zip`
- Target: Journal of Neural Transmission, Springer Nature.
- Route: subscription publishing model / non-open-access route to avoid APC.
- Included: manuscript DOCX, cover letter, title page, declarations, data availability statement, submission checklist, Zenodo DOI checklist, supplementary DOCX, and STROBE/PRISMA checklist.

Human items still required before upload: author list, affiliations, ORCID IDs, corresponding author email, funding statement, author contribution statement, final author approval, and Zenodo DOI insertion if the GitHub release is archived before submission.

## Zenodo DOI Status

Zenodo account context provided by user: `hssling@yahoo.com`.

GitHub release `v1.0.1` was created after the user indicated Zenodo was connected to GitHub. If Zenodo repository archiving is enabled for `hssling/pd-discovery-benchmark-dashboard`, Zenodo should mint a DOI for that release. Insert the Zenodo version DOI into the Data Availability Statement after Zenodo processing completes.
