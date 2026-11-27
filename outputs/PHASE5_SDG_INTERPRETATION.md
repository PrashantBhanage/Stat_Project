# Group Task Phase 5 (Repository Phase 4) — Visualisations and SDG Interpretation

**Project:** Group 8 — International Finance for Clean Energy  
**Course:** AS5004 Foundational Statistics for AI  
**SDG focus:** SDG 7, Target 7.a  
**Dataset:** 2,295 country/area-year observations, 153 countries/areas, 2010–2024  
**Units:** Million constant 2023 US dollars for finance.

**Numbering note:** The handout labels this work Group Task Phase 5. The repository project plan labels it Phase 4 — Visualisation and SDG interpretation; repository Phase 5 is machine learning.\n\n## 1. Introduction
This analysis examines the distribution of recorded international clean-energy finance, differences across countries and continents, and its pooled relationship with renewable energy share. The workbook Data Dictionary defines clean_energy_finance_all_usd_m as international financial flows supporting clean-energy R&D and renewable-energy production, including hybrid systems, and maps it to SDG indicator 7.a.1.

## 2. Objectives
- Review existing histograms, boxplots, continent-period chart and country finance summary.
- Rank the top 10 countries/areas by cumulative finance and show observed-year coverage.
- Visualise finance against renewable energy share and calculate Pearson and Spearman correlations.
- Interpret results against SDG 7.a using the Data Dictionary's indicator definitions.

## 3. Visualisation methodology
Finance distributions use log1p where needed to display the long right tail while retaining zeros. The scatter plot uses pairwise complete finance/share observations (n=2,171); missing values are excluded only from calculations requiring those variables. The raw workbook is not changed. Country totals are sums over observed years, and all country/areas have 15 finance observations (2010–2024) in this dataset. Potential IQR extremes are retained, not automatically deleted.

## 4. Important findings
Total finance is strongly right-skewed: mean **$108.95 million**, median **$6.50 million**, skewness **6.09**. There are **478 zero records (20.83%)**. The mean substantially exceeds the median, showing that a small number of large flows raise the average; median and IQR better describe a typical country-year.

The existing distributions, boxplots and continent-period comparison are retained. Finance and renewable-capacity distributions have long upper tails. IQR flags indicate unusual values relative to the observed distribution, not necessarily errors.

## 5. Country-wise comparison
Top cumulative finance, 2010–2024:

| Rank | Country/area | Total (million constant 2023 US$) | Observed years |
|---:|---|---:|---:|
| 1 | India | 24,962.39 | 15 |
| 2 | Pakistan | 11,875.51 | 15 |
| 3 | Türkiye | 11,483.67 | 15 |
| 4 | South Africa | 9,352.12 | 15 |
| 5 | Brazil | 8,823.85 | 15 |
| 6 | Argentina | 7,853.93 | 15 |
| 7 | Indonesia | 7,661.79 | 15 |
| 8 | Egypt | 7,547.60 | 15 |
| 9 | Lao People's Democratic Republic | 7,355.67 | 15 |
| 10 | Morocco | 6,608.58 | 15 |

India has the largest cumulative recorded total, more than twice Pakistan's. Equal year coverage makes period length comparable, but totals are not adjusted for population, GDP, energy demand, financing needs or project costs.

## 6. Finance and renewable energy relationship
The scatter plot compares total finance on the x-axis (log1p scale) with renewable share of total final energy consumption (%) on the y-axis. For the 2,171 pairwise complete country-years:
- Pearson, raw finance: **r = 0.018** (near-zero pooled linear relationship).
- Pearson, log1p finance: **r = 0.169** (weak positive linear association on transformed finance).
- Spearman, raw finance: **ρ = 0.258** (weak positive monotonic association).

The relationship is scale-sensitive and observations vary widely at similar finance levels. Correlation does not establish causation. Repeated country-years are not independent, and the pooled coefficients do not control for country, time, domestic investment, policy, resource potential or reverse causation.

## 7. SDG 7.a interpretation
The finance variable and its technology breakdowns are mapped by the workbook Data Dictionary to **Target 7.a, indicator 7.a.1**. The distribution is concentrated and zero-heavy, and continent totals differ: Asia records the largest aggregate finance (**$104,032.98 million**), while South America has the highest median per country-year (**$53.65 million**); Oceania has the lowest (**$0.05 million**). These patterns are relevant to international financial support and allocation monitoring, but do not alone prove that allocations are unfair or insufficient.

The supporting variables have distinct official mappings in the Data Dictionary: electricity access is **7.1.1** (Target 7.1), renewable share is **7.2.1** (Target 7.2), and installed renewable electricity capacity per capita is **7.b.1** (Target 7.b). They are contextual energy indicators, not direct 7.a.1 measurements. A weak pooled finance/share association does not show whether finance has been effective; project-level, time-lagged and country-adjusted analysis would be needed.

## 8. Limitations
- The data are country/area-year aggregates, not project-level finance or a complete inventory of every support source.
- The workbook warns that some indicator values may be estimates.
- Missing values remain missing; no blank is treated as zero.
- Continent summaries are not adjusted for population, GDP, financing need, renewable potential or cost.
- Correlations are pooled and unadjusted; country-year observations may be dependent.
- 2020–2024 is a partial 2020s period, not a complete decade.

## 9. Conclusion
Recorded international clean-energy finance varies substantially across country-years and continents. India has the highest cumulative total in the dataset, and Asia has the largest regional aggregate. Finance is highly right-skewed and has many zero observations. Finance and renewable share show near-zero raw Pearson correlation but weak positive rank and transformed-scale associations; none supports a causal claim. The findings can inform descriptive monitoring of SDG 7.a.1, while the related 7.1.1, 7.2.1 and 7.b.1 variables provide context only.

## Data Dictionary and source notes
The workbook attributes 7.a.1 financial flows to OECD DAC Statistics (2025) and the IRENA Public Finance Database (2026); 7.1.1 electricity access to the World Bank; 7.2.1 renewable share to IEA World Energy Balances (2025) and UN Statistics Division Energy Balances (2025); and 7.b.1 capacity to IRENA electricity-capacity data with population from UN World Population Prospects. Cite the workbook and relevant custodian agencies in the final submission.


## Machine-learning threshold correction

The ML workflow now splits country groups before calculating the renewable-share threshold. The median is calculated from the training observations only (**25.01%** for the recorded split) and then applied unchanged to both training and test observations. This avoids using the held-out target distribution to define the classes.
