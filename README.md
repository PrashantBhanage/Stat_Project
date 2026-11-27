# Group 8 — International Finance for Clean Energy

**Course:** AS5004 Foundational Statistics for AI · MCA Semester 1 · Unit 2  
**SDG focus:** SDG 7 — Affordable and Clean Energy · Target 7.a

## Repository and group-task phase numbering

The group handout labels the enhanced visualisation and SDG interpretation assignment as **Group Task Phase 5**. In this repository's official plan, the same work is **Phase 4 — Visualisation and SDG interpretation**. Repository **Phase 5** is the separate machine-learning classification task. Both labels are made explicit in the notebook and report.

## Objectives

1. Describe international clean-energy finance across country-years and identify unusual observations.
2. Compare country and continent finance patterns and examine the descriptive relationship with renewable share.
3. Interpret findings against SDG target 7.a using the supplied workbook Data Dictionary.
4. Classify country-years as high/low renewable share using a country-held-out machine-learning evaluation.

## Dataset privacy and local setup

The instructor workbook's own README explicitly says **“Please keep this dataset within your group.”** Therefore the original Excel workbook is intentionally **not committed to this public repository**. Obtain it from the course-provided group file and place it locally at `data/Group_08_Dataset.xlsx`. Keep it unchanged and do not upload it to a public repository or public file host.

The notebook reads the `Data` sheet using `header=11` and refers to the `Data Dictionary` sheet for official indicator definitions. A `.gitignore` rule excludes the workbook from accidental commits.

## Repository structure

- `data/README.md` — private dataset placement instructions.
- `notebooks/Group_08_Notebook.ipynb` — end-to-end analysis, including top-10 finance visualisation, finance/share correlations and corrected ML threshold workflow.
- `outputs/` — statistical tables, interpretations and generated figure files.
- `docs/PROJECT_PLAN.md` — official project phase checklist.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
jupyter notebook notebooks/Group_08_Notebook.ipynb
```

Run every cell from top to bottom. The notebook expects the original workbook at `data/Group_08_Dataset.xlsx`. It preserves missing values and the source workbook. The ML workflow splits country groups before calculating the renewable-share median threshold; the training-derived threshold is then applied unchanged to test observations.

The notebook writes charts to `outputs/figures/`, including `top_10_countries_finance.png` and `finance_vs_renewable_share.png`. These binary figures are available in the Phase 5 handoff package; their GitHub binary-file sync remains pending.

## Data citation

United Nations, Department of Economic and Social Affairs (UN DESA), SDG Global Database, Goal 7 data supplied by the instructor. Also cite the custodian agencies and source dates listed in the workbook's Data Dictionary (OECD DAC Statistics, IRENA, World Bank, IEA and UN Statistics Division, as appropriate).

## Academic integrity

The group must review numerical outputs, interpret the methods in its own words, acknowledge AI assistance as required by the handout, and ensure every member can explain the work.
