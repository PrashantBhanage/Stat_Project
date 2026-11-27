# Phase 3 — Outlier review and treatment decision

The Z-score rule uses |z| > 3 (sample standard deviation, ddof=1). The IQR rule uses Q1 − 1.5×IQR and Q3 + 1.5×IQR. Flags are based on non-missing observations. The source workbook is unchanged.

## Results

| Variable | n | Z-score flags | IQR flags | Both methods | IQR upper fence |
|---|---:|---:|---:|---:|---:|
| Total clean-energy finance | 2,295 | 60 (2.61%) | 334 (14.55%) | 60 | 194.868 million constant 2023 US$ |
| Renewable capacity per capita | 2,250 | 50 (2.22%) | 276 (12.27%) | 50 | 447.863 W/person |

## Interpretation

- Total finance is strongly right-skewed with a long upper tail. The stricter Z-score rule flags 60 observations; the IQR rule flags 334. All 60 Z-score flags are also IQR flags, so IQR identifies a further 274 moderately high observations.
- Renewable capacity per capita also has a long upper tail. Z-score flags 50 observations; IQR flags 276. All 50 Z-score flags are also IQR flags, so IQR identifies a further 226 observations.
- Both lower IQR fences are negative, while the variables are non-negative. All IQR flags are therefore upper-tail observations.
- The largest finance records include Angola (2016, 5,145.90 million constant 2023 US$), India (2023, 3,309.48 million) and India (2016, 2,661.82 million).
- The largest renewable-capacity observations include several Bhutan country-years. Extreme values may represent substantial real finance flows or installed capacity; the statistical flag alone does not identify a data error.

## Treatment decision

**Retain all observations; do not cap or delete based only on these rules.** The data are country-year aggregates, strongly right-skewed, and there is no independent evidence that flagged records are erroneous. Use medians/IQR and log1p displays for descriptive comparisons. Check questioned records against the custodian source before changing them.

The notebook exports `outlier_method_comparison.csv` and `outlier_flagged_country_years.csv` for row-level review.
