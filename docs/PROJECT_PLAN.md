# Group 8 project plan — official repository phase numbering

> **Numbering note:** The group handout calls the visualisation/SDG interpretation task “Group Task Phase 5”. In this repository it is **Phase 4**. Repository **Phase 5** is the separate machine-learning task.

## Phase 1 — Repository and data audit
- [x] Confirm workbook structure, Data sheet header row and Data Dictionary.
- [x] Record dimensions, duplicate keys and missingness from the original workbook.
- [x] Build reproducible notebook, requirements and local dataset instructions.
- [x] Preserve the original workbook in the group's private working copy.
- [x] Exclude the workbook from public GitHub because its README says to keep it within the group.

## Phase 2 — Descriptive statistics and EDA
- [x] Mean, median, mode, variance, standard deviation, quartiles, IQR, skewness and kurtosis.
- [x] Compare descriptive results by continent.
- [x] Finance zero counts and distribution/skewness analysis.
- [x] Histograms, boxplots and continent-period grouped chart.
- [x] Save statistical tables and Phase 2 interpretation.

## Phase 3 — Outlier analysis and interpretation
- [x] Calculate Z-score (|z| > 3) and IQR (1.5 × IQR) flags for total finance and renewable capacity.
- [x] Compare methods and generate flagged country-year-variable rows from notebook code.
- [x] Review flags and justify retaining raw observations; no capping/deletion without evidence of error.
- [x] Save method comparison and interpretation in `outputs/outlier_method_comparison.csv` and `outputs/OUTLIER_REVIEW.md`.

## Phase 4 — Visualisation and SDG 7.a interpretation (Group Task Phase 5 in handout)
- [x] Review existing histograms, boxplots, country finance summary and continent-period chart.
- [x] Create top-10 cumulative country/area finance chart and CSV with observed-year coverage.
- [x] Create finance versus renewable-share scatter plot and calculate Pearson (raw/log1p) and Spearman correlations.
- [x] Check official indicator mappings against the workbook Data Dictionary.
- [x] Write chart findings and SDG 7.a interpretation in `outputs/PHASE5_SDG_INTERPRETATION.md`.
- [x] Commit and verify both requested PNG figures under `outputs/figures/`.

## Phase 5 — Machine learning
- [x] Create complete-case modelling sample and country-grouped train/test split.
- [x] Split countries before calculating the renewable-share threshold; calculate median on training rows only and apply it unchanged to test rows.
- [x] Compare majority-class baseline with logistic regression.
- [x] Report accuracy, precision, recall and confusion matrix.
- [x] Interpret held-out errors and assess results against baseline in `outputs/ML_EVALUATION_REVIEW.md`.
- [x] Export held-out predictions, error summary, metrics and training-only threshold from the notebook.

## Phase 6 — Submission and repeated testing

**Deliberately left open at the user's request.** No Phase 6 item is marked complete. The group will start this phase after the current implementation handoff and use it for repeated testing before formal submission.
- [ ] Repeat notebook tests on several runs/seeds and compare stability of metrics.
- [ ] Run in a clean environment on another group member's machine.
- [ ] Prepare the 8–10 page report using the prescribed template.
- [ ] Complete the contribution matrix, individual member pages and authorship/declaration appendices.
- [ ] Prepare the 10-minute presentation and Q&A.
