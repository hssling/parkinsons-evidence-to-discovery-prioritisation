# Methods Log

Generated on 2026-04-24.

- ClinicalTrials.gov queried via v2 API when network was available.
- R 4.5.3 was found at `C:\Program Files\R\R-4.5.3\bin\x64\Rscript.exe`; Rtools45 was also found.
- GSE72267 was downloaded with GEOquery and analysed with limma. The run included 59 samples, 22,277 probes, and 0 probes meeting FDR < 0.05 with absolute log2 fold-change >= 0.25.
- GO biological-process enrichment was run with clusterProfiler on the top-ranked 500 genes.
- ReactomePA and reactome.db were installed through BiocManager. Exploratory Reactome enrichment of the top-ranked 500 genes returned 964 ranked terms; the leading adjusted P values were approximately 0.14, so the result is labelled exploratory rather than confirmatory.
- Priority scores are transparent synthesis metrics, not clinical recommendations.
