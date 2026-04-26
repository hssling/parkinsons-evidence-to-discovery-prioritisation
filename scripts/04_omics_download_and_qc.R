#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(GEOquery)
  library(Biobase)
  library(ggplot2)
})

args_file <- grep("^--file=", commandArgs(FALSE), value = TRUE)
script_path <- if (length(args_file)) sub("^--file=", "", args_file[[1]]) else "scripts/04_omics_download_and_qc.R"
root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)
omics_dir <- file.path(root, "data", "omics")
fig_dir <- file.path(root, "figures")
dir.create(omics_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(fig_dir, recursive = TRUE, showWarnings = FALSE)

message("Downloading GSE72267 from GEO...")
gse <- getGEO("GSE72267", GSEMatrix = TRUE, AnnotGPL = TRUE)
eset <- gse[[1]]

expr <- exprs(eset)
pheno <- pData(eset)
feature <- fData(eset)

group <- ifelse(grepl("PD patient", pheno$source_name_ch1, ignore.case = TRUE), "PD",
  ifelse(grepl("healthy control", pheno$source_name_ch1, ignore.case = TRUE), "Control", NA)
)
pheno$analysis_group <- factor(group, levels = c("Control", "PD"))

keep <- !is.na(pheno$analysis_group)
expr <- expr[, keep]
pheno <- pheno[keep, ]

if (max(expr, na.rm = TRUE) > 100) {
  expr <- log2(expr + 1)
}

saveRDS(
  list(expr = expr, pheno = pheno, feature = feature),
  file = file.path(omics_dir, "GSE72267_expression_pheno_feature.rds")
)
write.csv(pheno, file.path(omics_dir, "GSE72267_sample_metadata.csv"), row.names = TRUE)

qc <- data.frame(
  sample = colnames(expr),
  group = pheno$analysis_group,
  median_expression = apply(expr, 2, median, na.rm = TRUE),
  iqr_expression = apply(expr, 2, IQR, na.rm = TRUE)
)
write.csv(qc, file.path(omics_dir, "GSE72267_qc_metrics.csv"), row.names = FALSE)

png(file.path(fig_dir, "fig4a_GSE72267_qc_boxplot.png"), width = 2200, height = 1400, res = 220)
boxplot(expr, las = 2, outline = FALSE, col = ifelse(pheno$analysis_group == "PD", "#C55A11", "#2E75B6"),
  main = "GSE72267 expression distribution after log-scale check", ylab = "Expression")
legend("topright", fill = c("#2E75B6", "#C55A11"), legend = c("Control", "PD"), bty = "n")
dev.off()

pca <- prcomp(t(expr), scale. = TRUE)
pca_df <- data.frame(
  sample = rownames(pheno),
  group = pheno$analysis_group,
  PC1 = pca$x[, 1],
  PC2 = pca$x[, 2]
)
write.csv(pca_df, file.path(omics_dir, "GSE72267_pca.csv"), row.names = FALSE)

png(file.path(fig_dir, "fig4b_GSE72267_pca.png"), width = 1800, height = 1400, res = 220)
print(
  ggplot(pca_df, aes(PC1, PC2, color = group)) +
    geom_point(size = 2.4, alpha = 0.9) +
    scale_color_manual(values = c(Control = "#2E75B6", PD = "#C55A11")) +
    theme_minimal(base_size = 12) +
    labs(title = "GSE72267 PCA", color = "Group")
)
dev.off()

writeLines(capture.output(sessionInfo()), file.path(root, "reproducibility", "R_sessionInfo.txt"))
message("Saved GSE72267 expression object, metadata, QC metrics, and QC figures.")
