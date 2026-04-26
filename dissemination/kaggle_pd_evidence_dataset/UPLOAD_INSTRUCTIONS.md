# Kaggle Upload Instructions

1. Edit `dataset-metadata.json`.
2. Replace `YOUR_KAGGLE_USERNAME/parkinsons-evidence-to-discovery-prioritisation` with your Kaggle username slug.
3. Confirm the package does not include private or unpublished human-subject data. This package currently contains processed public/research outputs only.
4. Confirm the license choice. The default is `CC-BY-4.0`.
5. From this folder, run:

```powershell
kaggle datasets create -p . --public
```

For a private draft first:

```powershell
kaggle datasets create -p .
```

For later updates:

```powershell
kaggle datasets version -p . -m "Update evidence-to-discovery package"
```

## Recommended Title

Parkinson's Disease Evidence-to-Discovery Prioritisation Dataset

## Recommended Subtitle

Evidence map, pathway-intervention framework, GSE72267 omics outputs, Reactome/GO enrichment, and drug-repurposing rankings.

## Recommended Visibility

Start private, inspect rendering, then publish public after author approval.

