# Notebook execution verification

- GitHub source notebook: `notebooks/Group_08_Notebook.ipynb` — 19 cells, 9 code cells, with the current outlier export, group/repository phase mapping, top-10 and correlation logic, corrected train-only ML cutoff, and final validation code.
- Local executed notebook: `notebooks/Group_08_Notebook_executed.ipynb` — 19 cells, 9 code cells executed, zero cell errors.
- Verification result from the top-to-bottom local run: 10 top-10 rows; 2,171 pairwise-complete finance/share observations; 610 flagged country-year-variable records across the two outlier variables; 110 training countries and 37 held-out countries with zero overlap; training-derived threshold 25.01%; 8/8 requested output files found.

The **executed notebook with saved outputs is included in the downloadable corrected project package**. The notebook currently stored in GitHub is the reproducible source version; it does not embed the local run's execution outputs. The source workbook remains private to Group 8 as required by its README and is not committed to this public repository.

A second clean-environment run by another group member remains recommended.
