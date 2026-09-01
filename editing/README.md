# Results and Discussion editorial revision

Four documents, each paired with its unedited source:

| Revised | Source | Paragraphs | Words |
|---|---|---|---|
| `Thesis_Aromatic_Rice_West_Bengal_REVISED.docx` (Chapter IV) | `..._ORIGINAL.docx` | 516 | ~42,700 |
| `Experiment1_Results_and_Discussion_REVISED.docx` | `..._ORIGINAL.docx` | 231 | ~19,100 |
| `Experiment2_Results_and_Discussion_REVISED.docx` | `..._ORIGINAL.docx` | 239 | ~18,600 |
| `Experiment3_Results_and_Discussion_REVISED.docx` | `..._ORIGINAL.docx` | 160 | ~15,100 |

## Scope

Body prose only. Deliberately untouched: all tables, table captions, statistical
legends, headings, figure captions, and the Experiment 3 reference list
(102 bibliography entries, blocks 591 onward).

## House style applied

- Results: objective and empirical; short declarative sentences merged;
  duplicated statements of the same letter-grouping consolidated; precise
  reporting verbs (recorded, ranged, declined, attained, constituted).
- Discussion: interpretive, with hedging (suggests, indicates, may) and precise
  verbs for engaging the literature (corroborated, determined, demonstrated).
- No em dashes anywhere in the revised text, and no AI-tell vocabulary
  introduced (moreover, furthermore, crucial, robust, underscore, leverage,
  landscape, testament, and the rest of the list in `check.py`).
- Each document keeps its own conventions: `2022-23` vs `2022–23`, `%` vs
  `per cent`, spelling of cultivar names, `Results.`/`Discussion.` labels.

## Method

Paragraph text replaced in place in `word/document.xml` by byte-level surgery,
preserving each paragraph's `pPr` and the run properties of its first run, so
pagination, styles and numbering are unchanged.

## Verification

`check.py` compares, per paragraph, the multiset of numeric tokens and of
`Author (year)` citations between source and revision, and flags em dashes and
newly introduced AI-tell vocabulary. Document-wide, after rebuild:

- block counts unchanged in all four files; only the intended paragraphs differ
- 0 tables altered
- numeric multiset identical (all four files, subject to `exceptions.json`)
- citation multiset identical (all four files)
- 0 em dashes in output
- OOXML schema validation passes on all four

`exceptions.json` records the only two intentional numeric-token differences:
in Experiment 2 paragraphs 174 and 379 the source named 2-acetyl-1-pyrroline
twice in consecutive sentences and the redundant mention was merged. No data
point, percentage or citation was removed.

`b*.json` hold the revised text keyed by body-block index (Chapter IV in
`editing/`, the three experiments in `editing/experiments/`).
