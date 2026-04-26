#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(limma)
  library(ggplot2)
})

args_file <- grep("^--file=", commandArgs(FALSE), value = TRUE)
script_path <- if (length(args_file)) sub("^--file=", "", args_file[[1]]) else "scripts/05_differential_expression_meta_analysis.R"
root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)
omics_dir <- file.path(root, "data", "omics")
fig_dir <- file.path(root, "figures")
obj_path <- file.path(omics_dir, "GSE72267_expression_pheno_feature.rds")
if (!file.exists(obj_path)) {
  stop("Run scripts/04_omics_download_and_qc.R before differential expression.")
}

obj <- readRDS(obj_path)
expr <- obj$expr
pheno <- obj$pheno
feature <- obj$feature

design <- model.matrix(~ 0 + pheno$analysis_group)
colnames(design) <- levels(pheno$analysis_group)
fit <- lmFit(expr, design)
contrast <- makeContrasts(PD_vs_Control = PD - Control, levels = design)
fit2 <- eBayes(contrasts.fit(fit, contrast))
res <- topTable(fit2, coef = "PD_vs_Control", number = Inf, sort.by = "P")

feature$probe_id <- rownames(feature)
anno <- feature[, intersect(c("probe_id", "Gene symbol", "Gene ID", "Gene title"), colnames(feature)), drop = FALSE]
res$probe_id <- rownames(res)
res <- merge(res, anno, by = "probe_id", all.x = TRUE)
res$gene_symbol_primary <- sub("///.*", "", res$`Gene symbol`)
res <- res[order(res$adj.P.Val, res$P.Value), ]
write.csv(res, file.path(omics_dir, "GSE72267_limma_DEG_all.csv"), row.names = FALSE)

sig <- subset(res, adj.P.Val < 0.05 & abs(logFC) >= 0.25)
write.csv(sig, file.path(omics_dir, "GSE72267_limma_DEG_FDR05_logFC025.csv"), row.names = FALSE)

volcano <- res
volcano$neglog10FDR <- -log10(pmax(volcano$adj.P.Val, .Machine$double.xmin))
volcano$status <- ifelse(volcano$adj.P.Val < 0.05 & volcano$logFC > 0.25, "Higher in PD",
  ifelse(volcano$adj.P.Val < 0.05 & volcano$logFC < -0.25, "Lower in PD", "Not significant")
)
label_df <- head(volcano[order(volcano$adj.P.Val), ], 12)

png(file.path(fig_dir, "fig4_omics_DEG_volcano.png"), width = 1900, height = 1500, res = 240)
print(
  ggplot(volcano, aes(logFC, neglog10FDR, color = status)) +
    geom_point(alpha = 0.55, size = 1.2) +
    geom_vline(xintercept = c(-0.25, 0.25), linetype = "dashed", color = "grey45") +
    geom_hline(yintercept = -log10(0.05), linetype = "dashed", color = "grey45") +
    geom_text(data = label_df, aes(label = gene_symbol_primary), size = 2.6, vjust = -0.5, check_overlap = TRUE) +
    scale_color_manual(values = c("Higher in PD" = "#C55A11", "Lower in PD" = "#2E75B6", "Not significant" = "#BFBFBF")) +
    theme_minimal(base_size = 12) +
    labs(
      title = "Figure 4. GSE72267 PD vs control differential-expression volcano plot",
      x = "log2 fold-change, PD vs control",
      y = "-log10(FDR)",
      color = ""
    )
)
dev.off()

summary <- data.frame(
  dataset = "GSE72267",
  samples = ncol(expr),
  control_n = sum(pheno$analysis_group == "Control"),
  pd_n = sum(pheno$analysis_group == "PD"),
  probes_tested = nrow(res),
  significant_FDR05_logFC025 = nrow(sig),
  method = "limma empirical Bayes; PD-Control contrast"
)
write.csv(summary, file.path(omics_dir, "GSE72267_DEG_summary.csv"), row.names = FALSE)
message("Saved limma DEG outputs and updated fig4_omics_DEG_volcano.png.")
