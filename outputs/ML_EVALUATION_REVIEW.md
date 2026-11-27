# Repository Phase 5 — Machine-learning evaluation review

## Evaluation design

The complete-case sample is split by ISO3 country using a deterministic 75/25 `GroupShuffleSplit` (random state 42). Countries are assigned to train/test **before** the renewable-share cutoff is calculated. The training-only median is **25.01%** and is applied unchanged to both sets.

| Split | Rows | Countries |
|---|---:|---:|
| Training | 1,578 | 110 |
| Test | 533 | 37 |
| Country overlap | — | **0** |

## Held-out evaluation

| Metric | Majority-class baseline | Logistic regression |
|---|---:|---:|
| Accuracy | 39.02% | 75.98% |
| Precision (high class) | 0.00% | 87.45% |
| Recall (high class) | 0.00% | 70.77% |

The logistic-regression confusion matrix is:

| Actual / predicted | Low | High |
|---|---:|---:|
| Low | 175 | 33 |
| High | 95 | 230 |

The model classifies **405 of 533** observations correctly and misclassifies **128 (24.02%)**. It makes 33 false-positive high predictions and 95 false-negative high predictions. At least one observation is misclassified in **19 of 37** held-out countries.

## Interpretation

The model's accuracy is 36.96 percentage points above the baseline on this fixed split. Precision of 87.45% indicates that most positive/high predictions are correct, while recall of 70.77% means that about seven in ten high observations are detected.

The majority baseline predicts the most common training class (low). The test set contains 208 low and 325 high observations, so class proportions differ between training and test; the baseline's 39.02% accuracy reflects this distribution shift. It is a deliberately simple reference, not a strong universal benchmark.

## Limitations and next tests

- Only one deterministic group split has been evaluated.
- Country-level grouping prevents the same country from entering both samples, but does not eliminate distribution differences between country groups.
- Predictors and outcome are measured at the same country-year; time-lagged prediction is not assessed.
- The target is a training-median-derived binary label, not a continuous renewable share.
- Finance, policy, resource potential, domestic investment, country size and time effects are not fully controlled.
- Correlation and classification performance do not establish causation.

**Conclusion:** Logistic regression performs better than the majority baseline on this split. The result is promising for this introductory exercise but not yet stable evidence of generalisation. Repeated country-grouped splits or grouped cross-validation are the next testing phase. This is intentionally left for the group's repeated tests, not repository Phase 6 submission work.
