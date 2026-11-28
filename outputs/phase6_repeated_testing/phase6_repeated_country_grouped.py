#!/usr/bin/env python3
"""Phase 6 repeated and GroupKFold country-held-out tests for Group 8."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import GroupShuffleSplit, GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

TARGET = "renewable_share_tfec_pct"
FINANCE = "clean_energy_finance_all_usd_m"
ACCESS = "elec_access_total_pct"
CAPACITY = "re_capacity_all_w_per_capita"
FEATURES = ["log_finance", ACCESS, "log_capacity", "year"]


def load_data(workbook: Path) -> tuple[pd.DataFrame, int]:
    raw = pd.read_excel(workbook, sheet_name="Data", header=11)
    needed = ["country", "iso3", "continent", "year", TARGET, FINANCE, ACCESS, CAPACITY]
    missing = sorted(set(needed) - set(raw.columns))
    if missing:
        raise ValueError(f"Workbook is missing required columns: {missing}")
    data = raw[needed].copy()
    for col in ["year", TARGET, FINANCE, ACCESS, CAPACITY]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.dropna(subset=needed).copy()
    data = data[(data[FINANCE] >= 0) & (data[CAPACITY] >= 0)].copy()
    data["log_finance"] = np.log1p(data[FINANCE])
    data["log_capacity"] = np.log1p(data[CAPACITY])
    return data.reset_index(drop=True), len(raw)


def metric_dict(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
    }


def evaluate_partition(data: pd.DataFrame, train_idx: np.ndarray, test_idx: np.ndarray,
                       partition: int, label: str) -> tuple[dict, pd.DataFrame, dict]:
    train, test = data.iloc[train_idx], data.iloc[test_idx]
    train_countries, test_countries = set(train.iso3), set(test.iso3)
    overlap = train_countries & test_countries
    if overlap:
        raise AssertionError(f"Country leakage in {label} {partition}: {sorted(overlap)}")

    threshold = float(train[TARGET].median())
    y_train = (train[TARGET].to_numpy() > threshold).astype(int)
    y_test = (test[TARGET].to_numpy() > threshold).astype(int)

    model = make_pipeline(StandardScaler(), LogisticRegression(
        max_iter=2000, class_weight="balanced", random_state=42
    ))
    model.fit(train[FEATURES], y_train)
    prediction = model.predict(test[FEATURES]).astype(int)

    counts = np.bincount(y_train, minlength=2)
    baseline_class = 0 if counts[0] >= counts[1] else 1  # ties break to low
    baseline_prediction = np.full(len(test), baseline_class, dtype=int)
    model_metrics = metric_dict(y_test, prediction)
    baseline_metrics = metric_dict(y_test, baseline_prediction)

    row = {
        "partition": partition, "threshold_train_median_pct": threshold,
        "train_rows": len(train), "test_rows": len(test),
        "train_countries": len(train_countries), "test_countries": len(test_countries),
        "country_overlap": len(overlap), "train_low": int((y_train == 0).sum()),
        "train_high": int((y_train == 1).sum()), "test_low": int((y_test == 0).sum()),
        "test_high": int((y_test == 1).sum()), "baseline_tie": bool(counts[0] == counts[1]),
        "baseline_class": "low" if baseline_class == 0 else "high",
    }
    row.update({f"model_{k}": v for k, v in model_metrics.items()})
    row.update({f"baseline_{k}": v for k, v in baseline_metrics.items()})

    errors = test[["country", "iso3", "continent", "year"]].copy()
    errors["partition"] = partition
    errors["actual"] = y_test
    errors["predicted"] = prediction
    errors["correct"] = y_test == prediction
    audit = {
        "partition": partition, "train_rows": len(train), "test_rows": len(test),
        "train_countries": len(train_countries), "test_countries": len(test_countries),
        "country_overlap_count": len(overlap), "train_target_median_pct": threshold,
        "training_low_count": int(counts[0]), "training_high_count": int(counts[1]),
        "baseline_tie": bool(counts[0] == counts[1]),
        "baseline_tie_break": "low" if counts[0] == counts[1] else "",
    }
    return row, errors, audit


def error_summary(errors: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    rows = []
    for key, group in errors.groupby(group_cols, dropna=False, sort=False):
        if not isinstance(key, tuple):
            key = (key,)
        actual, predicted = group.actual.to_numpy(), group.predicted.to_numpy()
        fn = int(((actual == 1) & (predicted == 0)).sum())
        fp = int(((actual == 0) & (predicted == 1)).sum())
        tp = int(((actual == 1) & (predicted == 1)).sum())
        tn = int(((actual == 0) & (predicted == 0)).sum())
        row = dict(zip(group_cols, key))
        row.update({
            "test_exposures": len(group), "misclassified": int((actual != predicted).sum()),
            "error_rate": float((actual != predicted).mean()),
            "actual_high_pct": float((actual == 1).mean() * 100),
            "predicted_high_pct": float((predicted == 1).mean() * 100),
            "false_negatives": fn, "false_positives": fp,
            "true_positives": tp, "true_negatives": tn,
            "net_high_underprediction_fn_minus_fp": fn - fp,
        })
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["misclassified", "error_rate"] + group_cols,
                                           ascending=[False, False] + [True] * len(group_cols))


def summary_statistics(frame: pd.DataFrame) -> pd.DataFrame:
    records = []
    for model, prefix in [("Logistic regression", "model"), ("Majority baseline", "baseline")]:
        for metric in ["accuracy", "precision", "recall", "f1"]:
            values = frame[f"{prefix}_{metric}"].astype(float)
            records.append({"model": model, "metric": metric, "mean": values.mean(),
                            "sd_sample": values.std(ddof=1), "min": values.min(), "max": values.max()})
    return pd.DataFrame(records)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/phase6_repeated_testing"))
    parser.add_argument("--figure-dir", type=Path, default=Path("outputs/figures"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)

    data, source_rows = load_data(args.workbook)
    repeated_rows, repeated_errors, repeated_audits = [], [], []
    for seed in range(42, 52):
        splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=seed)
        train_idx, test_idx = next(splitter.split(data[FEATURES], groups=data.iso3))
        row, errors, audit = evaluate_partition(data, train_idx, test_idx, seed, "repeat")
        row["random_state"] = seed
        repeated_rows.append(row); repeated_errors.append(errors); repeated_audits.append(audit)

    repeated = pd.DataFrame(repeated_rows)
    repeated_event = pd.concat(repeated_errors, ignore_index=True)
    repeated_country = error_summary(repeated_event, ["country", "iso3"]).head(30)
    repeated_year = error_summary(repeated_event, ["year"])
    repeated_continent = error_summary(repeated_event, ["continent"])
    repeated.to_csv(args.output_dir / "phase6_repeated_split_metrics.csv", index=False)
    summary_statistics(repeated).to_csv(args.output_dir / "phase6_repeated_summary_statistics.csv", index=False)
    pd.DataFrame(repeated_audits).to_csv(args.output_dir / "phase6_repeated_split_audit.csv", index=False)
    repeated_country.to_csv(args.output_dir / "phase6_repeated_country_error_analysis.csv", index=False)
    repeated_year.to_csv(args.output_dir / "phase6_repeated_year_error_analysis.csv", index=False)
    repeated_continent.to_csv(args.output_dir / "phase6_repeated_continent_error_analysis.csv", index=False)

    fold_rows, fold_errors, fold_audits = [], [], []
    gkf = GroupKFold(n_splits=5)
    for fold, (train_idx, test_idx) in enumerate(gkf.split(data[FEATURES], groups=data.iso3), start=1):
        row, errors, audit = evaluate_partition(data, train_idx, test_idx, fold, "fold")
        fold_rows.append(row); fold_errors.append(errors); fold_audits.append(audit)
    heldout = pd.concat(fold_errors, ignore_index=True)
    if len(heldout) != len(data) or heldout.iso3.nunique() != data.iso3.nunique():
        raise AssertionError("GroupKFold did not hold out each country exactly once")
    folds = pd.DataFrame(fold_rows)
    fold_continent = error_summary(heldout, ["continent"])
    folds.to_csv(args.output_dir / "phase6_groupkfold_fold_metrics.csv", index=False)
    summary_statistics(folds).to_csv(args.output_dir / "phase6_groupkfold_summary_statistics.csv", index=False)
    pd.DataFrame(fold_audits).to_csv(args.output_dir / "phase6_groupkfold_fold_audit.csv", index=False)
    fold_continent.to_csv(args.output_dir / "phase6_groupkfold_continent_error_analysis.csv", index=False)

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    model_acc = repeated.model_accuracy.to_numpy() * 100
    base_acc = repeated.baseline_accuracy.to_numpy() * 100
    ax.boxplot([model_acc, base_acc], tick_labels=["Logistic regression", "Majority baseline"], showmeans=True)
    ax.scatter(np.repeat(1, len(model_acc)), model_acc, alpha=0.75, label="Individual repeats")
    ax.scatter(np.repeat(2, len(base_acc)), base_acc, alpha=0.75)
    ax.set_ylabel("Held-out accuracy (%)")
    ax.set_title("Accuracy across 10 country-grouped repeats (seeds 42–51)")
    ax.grid(axis="y", alpha=0.25); ax.legend(loc="best"); fig.tight_layout()
    fig.savefig(args.figure_dir / "phase6_accuracy_boxplot.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    print(f"Source observations: {source_rows}; complete modelling rows: {len(data)}; countries: {data.iso3.nunique()}")
    print("Repeated split country overlap maximum:", pd.DataFrame(repeated_audits).country_overlap_count.max())
    print("GroupKFold country overlap maximum:", pd.DataFrame(fold_audits).country_overlap_count.max())
    print("\nRepeated split metrics (percentages):")
    print(repeated[["random_state", "threshold_train_median_pct", "model_accuracy", "model_precision", "model_recall", "model_f1", "baseline_accuracy"]].to_string(index=False))
    print("\nRepeated summary (mean, sample SD, min, max; percentages):")
    print((summary_statistics(repeated).assign(**{c: lambda x: x[c] * 100 for c in ["mean", "sd_sample", "min", "max"]})).to_string(index=False))
    print("\nGroupKFold fold metrics (percentages):")
    print(folds[["partition", "threshold_train_median_pct", "model_accuracy", "model_precision", "model_recall", "model_f1", "baseline_accuracy", "country_overlap"]].to_string(index=False))
    print("\nGroupKFold summary (mean, sample SD, min, max; percentages):")
    print((summary_statistics(folds).assign(**{c: lambda x: x[c] * 100 for c in ["mean", "sd_sample", "min", "max"]})).to_string(index=False))
    print("\nContinent FN/FP across repeated splits:")
    print(repeated_continent[["continent", "test_exposures", "false_negatives", "false_positives", "error_rate"]].to_string(index=False))
    print("\nContinent FN/FP across GroupKFold:")
    print(fold_continent[["continent", "test_exposures", "false_negatives", "false_positives", "error_rate"]].to_string(index=False))

if __name__ == "__main__":
    main()
