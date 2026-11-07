import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab08")
churn = pd.read_csv(DATA / "churn.csv")


def test_eda_summary():
    r = m.eda_summary(churn)
    assert r["n_rows"] == 2000 and r["n_cols"] == 8
    assert r["missing"] == {"monthly_charges": 60}
    assert "tenure_months" in r["numeric_cols"] and "contract" in r["categorical_cols"]
    assert r["duplicates"] == 0


def test_correlation_pairs():
    df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 4, 6, 8.5], "c": [4, 1, 3, 2], "t": ["x"] * 4})
    r = m.correlation_pairs(df, 0.9)
    assert len(r) == 1 and r[0][:2] == ("a", "b") and r[0][2] > 0.99


def test_correlation_pairs_sorted_unique():
    r = m.correlation_pairs(churn, 0.0)
    pairs = [(a, b) for a, b, _ in r]
    assert len(pairs) == len(set(pairs)) and all(a < b for a, b in pairs)
    assert [abs(x[2]) for x in r] == sorted([abs(x[2]) for x in r], reverse=True)


def test_top_categories():
    s = m.top_categories(churn, "contract", 2)
    assert len(s) == 2 and s.iloc[0] >= s.iloc[1] and s.index[0] == "monthly"
    assert 0 < s.sum() <= 1


def test_group_profile():
    p = m.group_profile(churn, "contract", "tenure_months")
    assert list(p.columns) == ["count", "mean", "median"]
    assert p["mean"].is_monotonic_decreasing and p["count"].sum() == 2000
