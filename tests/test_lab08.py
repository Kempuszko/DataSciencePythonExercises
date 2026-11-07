import numpy as np
import pandas as pd
from loader import DATA, load
import matplotlib
matplotlib.use('Agg')

m = load("lab08")
churn = pd.read_csv(DATA / "churn.csv")
rng = np.random.default_rng(1)
A = rng.normal(10, 2, 80)
B = rng.normal(11, 2, 90)


def _labels_ok(ax):
    return bool(ax.get_title()) and bool(ax.get_xlabel()) and bool(ax.get_ylabel())


def test_a_monthly_revenue():
    s = pd.Series([10, 20, 15, 30], index=["2024-01", "2024-02", "2024-03", "2024-04"])
    ax = m.plot_monthly_revenue(s)
    assert _labels_ok(ax)
    assert len(ax.lines) == 1 and len(ax.lines[0].get_xdata()) == 4
    assert all(abs(l.get_rotation() - 45) < 1e-6 for l in ax.get_xticklabels())


def test_a_eda_summary():
    r = m.eda_summary(churn)
    assert r["n_rows"] == 2000 and r["n_cols"] == 8
    assert r["missing"] == {"monthly_charges": 60}
    assert "tenure_months" in r["numeric_cols"] and "contract" in r["categorical_cols"]
    assert r["duplicates"] == 0


def test_b_bootstrap_ci_contains_mean_and_deterministic():
    lo, hi = m.bootstrap_ci(A, n_boot=1000, seed=3)
    assert lo < A.mean() < hi and 0 < hi - lo < 2
    assert m.bootstrap_ci(A, n_boot=1000, seed=3) == (lo, hi)


def test_b_bootstrap_ci_other_stat():
    lo, hi = m.bootstrap_ci(A, stat=np.median, n_boot=500, seed=0)
    assert lo < np.median(A) < hi


def test_b_permutation_test_detects_difference():
    assert m.permutation_test(A, B, n_perm=2000, seed=0) < 0.05
    same = rng.normal(0, 1, 60)
    assert m.permutation_test(same, same + rng.normal(0, 1e-3, 60), n_perm=500, seed=0) > 0.5


def test_b_permutation_p_in_range():
    p = m.permutation_test([1, 2, 3], [1, 2, 3], n_perm=200, seed=0)
    assert 0 < p <= 1
