#!/usr/bin/env Rscript

suppressPackageStartupMessages({
  library(clusterProfiler)
  library(ReactomePA)
  library(org.Hs.eg.db)
  library(ggplot2)
})

args_file <- grep("^--file=", commandArgs(FALSE), value = TRUE)
script_path <- if (length(args_file)) sub("^--file=", "", args_file[[1]]) else "scripts/06_pathway_enrichment.R"
root <- normalizePath(file.path(dirname(script_path), ".."), winslash = "/", mustWork = TRUE)
omics_dir <- file.path(root, "data", "omics")
fig_dir <- file.path(root, "figures")
deg_path <- file.path(omics_dir, "GSE72267_limma_DEG_all.csv")
if (!file.exists(deg_path)) {
  stop("Run scripts/05_differential_expression_meta_analysis.R before enrichment.")
}

deg <- read.csv(deg_path, check.names = FALSE)
deg$gene_symbol_primary <- sub("///.*", "", deg$gene_symbol_primary)
deg <- deg[!is.na(deg$gene_symbol_primary) & deg$gene_symbol_primary != "", ]

ranked <- deg[order(deg$P.Value), ]
candidate_symbols <- unique(head(ranked$gene_symbol_primary, 500))
map <- bitr(candidate_symbols, fromType = "SYMBOL", toType = "ENTREZID", OrgDb = org.Hs.eg.db)
entrez <- unique(map$ENTREZID)

ego <- enrichGO(
  gene = entrez,
  OrgDb = org.Hs.eg.db,
  keyType = "ENTREZID",
  ont = "BP",
  pAdjustMethod = "BH",
  qvalueCutoff = 0.20,
  readable = TRUE
)

ego_df <- as.data.frame(ego)
write.csv(ego_df, file.path(omics_dir, "GSE72267_GO_BP_enrichment_top500.csv"), row.names = FALSE)

react <- enrichPathway(
  gene = entrez,
  organism = "human",
  pAdjustMethod = "BH",
  qvalueCutoff = 0.20,
  readable = TRUE
)
react_df <- as.data.frame(react)
write.csv(react_df, file.path(omics_dir, "GSE72267_Reactome_enrichment_top500.csv"), row.names = FALSE)

if (nrow(ego_df) > 0) {
  plot_df <- head(ego_df[order(ego_df$p.adjust), ], 15)
  plot_df$Description <- factor(plot_df$Description, levels = rev(plot_df$Description))
  png(file.path(fig_dir, "fig5_pathway_enrichment_dotplot.png"), width = 2100, height = 1500, res = 240)
  print(
    ggplot(plot_df, aes(x = -log10(p.adjust), y = Description, size = Count, color = -log10(p.adjust))) +
      geom_point(alpha = 0.9) +
      scale_color_viridis_c() +
      theme_minimal(base_size = 11) +
      labs(
        title = "Figure 5. GSE72267 GO biological-process enrichment",
        x = "-log10(FDR)",
        y = "",
        size = "Gene count",
        color = "-log10(FDR)"
      )
  )
  dev.off()
} else {
  warning("No GO BP enrichment terms passed q-value threshold.")
}

if (nrow(react_df) > 0) {
  react_plot <- head(react_df[order(react_df$p.adjust), ], 15)
  react_plot$Description <- factor(react_plot$Description, levels = rev(react_plot$Description))
  png(file.path(fig_dir, "fig5b_reactome_enrichment_dotplot.png"), width = 2100, height = 1500, res = 240)
  print(
    ggplot(react_plot, aes(x = -log10(p.adjust), y = Description, size = Count, color = -log10(p.adjust))) +
      geom_point(alpha = 0.9) +
      scale_color_viridis_c() +
      theme_minimal(base_size = 11) +
      labs(
        title = "Supplementary Figure. GSE72267 Reactome enrichment",
        x = "-log10(FDR)",
        y = "",
        size = "Gene count",
        color = "-log10(FDR)"
      )
  )
  dev.off()
} else {
  warning("No Reactome enrichment terms passed q-value threshold.")
}

message("Saved GO BP and Reactome enrichment outputs and updated pathway enrichment figures.")
