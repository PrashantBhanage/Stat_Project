# Phase 2 — Statistical Analysis and EDA

**Dataset:** Group 08 instructor workbook, Data sheet (header row 12)  
**Coverage:** 2,295 country-year rows, 153 countries, 2010–2024  
**Validation:** 0 duplicate rows; 0 duplicate ISO3-year keys.

## Missing data
- Electricity access: 75 missing (75/2,295; 3.27%).
- Renewable share of total final energy consumption: 124 missing (5.40%).
- Renewable capacity per capita: 45 missing (1.96%).
- Finance variables and country/year identifiers: no missing values.

Missing values are left as missing; no blank is assumed to mean zero.

## Descriptive statistics

Variance and standard deviation use pandas' sample definitions (ddof=1). Quartiles use the default linear interpolation.

| Variable | n | Mean | Median | Mode | Variance | SD | Q1 | Q3 | IQR | Skewness | Excess kurtosis |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Total clean-energy finance (million US$) | 2,295 | 108.951 | 6.500 | 0 | 87,284.958 | 295.440 | 0.030 | 77.965 | 77.935 | 6.089 | 59.148 |
| Electricity access (%) | 2,220 | 77.712 | 94.300 | 100 | 824.953 | 28.722 | 56.500 | 99.900 | 43.400 | -1.074 | -0.214 |
| Renewable share (%) | 2,171 | 34.194 | 26.730 | 0 | 866.906 | 29.443 | 8.305 | 58.315 | 50.010 | 0.579 | -1.002 |
| Renewable capacity per capita (W) | 2,250 | 175.927 | 60.380 | 0 | 99,409.735 | 315.293 | 12.588 | 186.698 | 174.110 | 4.123 | 24.602 |
| Solar finance (million US$) | 2,295 | 27.764 | 0.010 | 0 | 12,542.862 | 111.995 | 0 | 4.135 | 4.135 | 8.151 | 87.607 |
| Wind finance (million US$) | 2,295 | 9.454 | 0 | 0 | 3,327.476 | 57.684 | 0 | 0 | 0 | 13.554 | 273.312 |
| Hydropower finance (million US$) | 2,295 | 30.870 | 0 | 0 | 30,584.256 | 174.884 | 0 | 0.030 | 0.030 | 13.002 | 242.724 |
| Bioenergy finance (million US$) | 2,295 | 1.702 | 0 | 0 | 145.642 | 12.068 | 0 | 0 | 0 | 10.495 | 133.916 |

## Zero values and distribution
- Total finance is zero in 478 records (20.83%).
- Solar finance is zero in 1,129 (49.19%).
- Wind finance is zero in 1,972 (85.93%).
- Hydropower finance is zero in 1,700 (74.07%).
- Bioenergy finance is zero in 1,925 (83.88%).

The finance series have large positive skew and high excess kurtosis. Median and IQR are more representative of a typical country-year than mean and SD alone. For visualisations, use log1p(finance) to retain zero values while compressing extreme right tails. Do not automatically delete outliers.

## Finance by continent (country-year observations)

| Continent | n | Total finance (million US$) | Mean | Median |
|---|---:|---:|---:|---:|
| Asia | 585 | 104,032.98 | 177.83 | 20.88 |
| Africa | 825 | 78,964.50 | 95.71 | 9.56 |
| South America | 180 | 39,912.57 | 221.74 | 53.65 |
| North America | 315 | 18,473.41 | 58.65 | 2.50 |
| Europe | 120 | 6,998.37 | 58.32 | 14.56 |
| Oceania | 270 | 1,660.40 | 6.15 | 0.05 |

Asia has the largest summed finance in this dataset. South America has the highest mean and median per country-year. These are descriptive comparisons of this workbook's recorded observations, not per-capita or needs-adjusted fairness measures.

## Top recorded finance country-years
| Country | Year | Finance (million US$) |
|---|---:|---:|
| Angola | 2016 | 5,145.90 |
| India | 2023 | 3,309.48 |
| India | 2016 | 2,661.82 |
| Argentina | 2014 | 2,573.94 |
| India | 2017 | 2,312.10 |
| Lao People's Democratic Republic | 2017 | 2,299.54 |
| India | 2011 | 2,195.33 |
| Ecuador | 2010 | 2,192.04 |
| Egypt | 2017 | 2,185.62 |
| India | 2018 | 1,913.71 |

## Interpretation
1. Total finance and installed renewable capacity are strongly right-skewed: a few large values drive the means.
2. The finance component variables contain many zeros; wind and bioenergy finance are zero in most country-years.
3. Electricity access is concentrated near the upper end, but some observations remain much lower.
4. The renewable-share variable is moderately positively skewed; its median (26.73%) is below its mean (34.19%).
5. Country/continent comparisons should use both totals and typical values, and must not be described as proof of equitable allocation or causal impact.

## Phase 2 completion
Completed in the notebook: descriptive statistics, continent grouping, zero-value analysis, distribution charts and output tables. Review the notebook outputs and figures before using these interpretations in the final report.
