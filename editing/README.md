# Chapter IV (Results and Discussion) — editorial revision

`Thesis_Aromatic_Rice_West_Bengal_REVISED.docx` is the thesis with Chapter IV
("Results and Discussion", §4.0–4.43) rewritten for scholarly register.
`Thesis_Aromatic_Rice_West_Bengal_ORIGINAL.docx` is the unedited source.

## Scope

516 body paragraphs (~42,700 words) at 12 pt were rewritten. Deliberately left
untouched: all 284 tables, table captions (11 pt), statistical legends (10 pt,
"Means followed by a common letter…", "Significance of main effects…"), headings,
figures, and every chapter outside IV.

## Method

Paragraph text was replaced in place in `word/document.xml` by byte-level
surgery, preserving each paragraph's `pPr` and the run properties of its first
run, so pagination, styles and numbering are unchanged. Run formatting within
these paragraphs was already uniform (verified before editing).

## Verification

`check.py` compares, per paragraph, the multiset of numeric tokens and of
`Author (year)` citations between original and revision. Post-build checks over
the whole document:

- 2,845 body blocks before and after; only the 516 intended paragraphs differ
- 0 tables altered
- doc-wide numeric multiset identical
- doc-wide citation multiset identical
- OOXML schema validation passes

`b00.json`–`b19.json` hold the revised text keyed by body-block index.
