# Hugging Face Upload Instructions

This package is a Hugging Face **dataset repository**, not a model repository. No trained predictive model was created.

## Create A Dataset Repository

Replace `YOUR_HF_USERNAME` with your Hugging Face username or organisation:

```powershell
huggingface-cli login
huggingface-cli repo create parkinsons-evidence-to-discovery-prioritisation --type dataset
```

Then upload from this folder:

```powershell
python ..\upload_to_huggingface.py --repo-id YOUR_HF_USERNAME/parkinsons-evidence-to-discovery-prioritisation --path .
```

## Recommended Repository Name

`parkinsons-evidence-to-discovery-prioritisation`

## Recommended Visibility

Start private, inspect the dataset card, then switch public after author approval.

## Important

Do not describe this as a clinical model or a validated clinical decision-support system. It is a research dataset for evidence synthesis, pathway analysis, reproducibility, and hypothesis generation.

