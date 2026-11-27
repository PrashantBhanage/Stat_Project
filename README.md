# Group 8 — International Finance for Clean Energy

AS5004 Foundational Statistics for AI · MCA Semester 1 · Unit 2  
SDG 7: Affordable and Clean Energy · Target 7.a

## Objectives
1. Describe the distribution of international clean-energy finance across developing countries and identify extreme country-years.
2. Classify country-years as having high or low renewable energy share using finance, electricity access, installed renewable capacity and year.

## Repository structure
- `data/Group_08_Dataset.xlsx`: original instructor-provided workbook.
- `notebooks/Group_08_Notebook.ipynb`: reproducible analysis.
- `reports/`: final report files.
- `outputs/`: generated tables and figures.
- `docs/PROJECT_PLAN.md`: phase checklist.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/Group_08_Notebook.ipynb
```
Run all cells from top to bottom. The notebook uses the Data worksheet with `header=11`, preserves missing values, and uses a country-grouped train/test split.

## Data source
United Nations, Department of Economic and Social Affairs (UN DESA), SDG Global Database, Goal 7 data downloaded by the instructor in November 2026: https://unstats.un.org/sdgs/dataportal. Also cite the custodian agencies listed in the workbook's Data Dictionary.

## Academic integrity
Review all generated outputs, understand the methods, acknowledge AI assistance as required by the handout, and ensure every group member can explain the work.
