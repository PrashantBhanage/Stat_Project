# Group 8 project plan — official repository phase numbering

> **Numbering note:** The handout calls the enhanced visualisation/SDG interpretation assignment “Group Task Phase 5”. In this repository's official plan, the same work is **Phase 4**. Repository **Phase 5** is machine learning. Both labels are shown in the notebook and report.

## Phase 1 — Repository and data audit
- [x] Confirm workbook structure, Data sheet header row and Data Dictionary.
- [x] Record dimensions, duplicate keys and missingness from the original workbook.
- [x] Build reproducible notebook, requirements and local dataset instructions.
- [x] Preserve the original workbook in the group's private working copy.
- [x] Exclude the workbook from public GitHub because the workbook README says to keep it within the group.

## Phase 2 — Descriptive statistics and EDA
- [x] Mean, median, mode, variance, standard deviation, quartiles, IQR, skewness and kurtosis.
- [x] Compare descriptive results by continent.
- [x] Finance zero counts and distribution/skewness analysis.
- [x] Histograms, boxplots and continent-period chart.

## Phase 3 — Outlier analysis and interpretation
- [x] Calculate Z-score (|z| > 3) and IQR (1.5 × IQR) flags for total finance and renewable capacity.
- [x] Compare methods and export flagged country-year-variable rows.
- [x] Review flags and document retention decision; no capping or deletion because flags alone do not establish data errors.

## Phase 4 — Visualisation and SDG 7.a interpretation (Group Task Phase 5 in handout)
- [x] Retain and review existing histograms, boxplots, country finance summary and continent trend chart.
- [x] Add top-10 cumulative country/area finance chart and CSV with year coverage.
- [x] Add finance versus renewable-share scatter plot and Pearson/Spearman correlations.
- [x] Check SDG indicator mappings against the workbook Data Dictionary.
- [x] Write findings in `outputs/PHASE5_SDG_INTERPRETATION.md`.
- [ ] Commit the two generated PNG files to `outputs/figures/`; the files are generated and validated locally but binary upload to this repo is still pending.

## Phase 5 — Machine learning
- [x] Build complete-case modelling sample and country-grouped train/test split.
- [x] Split countries before calculating the renewable-share threshold; calculate median on training rows only and apply the same threshold to test rows.
- [x] Compare majority-class baseline with logistic regression.
- [x] Report accuracy, precision, recall and confusion matrix.
- [ ] Interpret held-out errors and assess practical value versus baseline in the final report.

## Phase 6 — Submission
- [x] Execute the notebook top-to-bottom locally against the supplied workbook with no cell errors.
- [ ] Perform a clean-environment rerun on another group member's machine.
- [ ] Prepare the 8–10 page report using the prescribed template.
- [ ] Complete contribution matrix, individual member pages and authorship/declaration appendices.
- [ ] Prepare the 10-minute presentation and Q&A.
