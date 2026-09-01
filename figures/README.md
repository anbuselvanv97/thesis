# Figures extracted from the experiment documents

Every figure already embedded in `Experiment2_Results_and_Discussion_REVISED.docx`
and `Experiment3_Results_and_Discussion_REVISED.docx`, exported as separate PNGs
for reuse in slides, posters and manuscripts. These are the original images from
the documents, copied byte for byte; nothing was regenerated or restyled.

## Experiment 2 (51 figures)

- `E2_01_PartA_*` to `E2_26_PartA_*` — bar charts, four cooked products
  (table rice, kichidi, pulao, payash) across ten cultivars
- `E2_27_dendrogram_PartA_cooked_products.png` — Ward dendrogram, 40 cultivar
  and product combinations
- `E2_28_PartB_*` to `E2_50_PartB_*` — bar charts, three processed products
  (popped, puffed, flattened rice)
- `E2_51_dendrogram_PartB_processed_products.png` — Ward dendrogram, 30
  cultivar and product combinations

In the source document these charts sit inside the data table blocks rather than
as separately captioned figures; only the two dendrograms carry a "Fig. N."
caption. Filenames here follow the document's own figure numbering.

## Experiment 3 (46 figures)

- `E3_Fig4-01_*` to `E3_Fig4-42_*` — bar charts, twelve treatment combinations
  (four varieties x plain, carrot fortified, beet fortified)
- `E3_Fig4-43_Correlation_heat_map.png`
- `E3_Fig4-44_Scree_plot.png`
- `E3_Fig4-45_PCA_biplot.png`
- `E3_Fig4-46_Dendrogram.png`

## Regenerating an archive

    zip -r Experiment2_figures.zip Experiment2
    zip -r Experiment3_figures.zip Experiment3
