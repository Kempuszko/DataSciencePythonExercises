import matplotlib
matplotlib.use("Agg")
import numpy as np
import pandas as pd
from loader import load

m = load("lab07")


def _labels_ok(ax):
    return bool(ax.get_title()) and bool(ax.get_xlabel()) and bool(ax.get_ylabel())


def test_monthly_revenue():
    s = pd.Series([10, 20, 15, 30], index=["2024-01", "2024-02", "2024-03", "2024-04"])
    ax = m.plot_monthly_revenue(s)
    assert _labels_ok(ax)
    assert len(ax.lines) == 1 and len(ax.lines[0].get_xdata()) == 4
    assert all(abs(l.get_rotation() - 45) < 1e-6 for l in ax.get_xticklabels())


def test_hist():
    ax = m.plot_hist(np.random.default_rng(0).normal(size=500), bins=15)
    assert _labels_ok(ax) and len(ax.patches) == 15


def test_bar_by_category():
    s = pd.Series({"a": 5, "b": 9, "c": 1, "d": 7, "e": 3, "f": 8})
    ax = m.plot_bar_by_category(s, top=4)
    assert _labels_ok(ax) and len(ax.patches) == 4
    heights = [p.get_height() for p in ax.patches]
    assert heights[0] == max(heights) == 9


def test_scatter_with_trend():
    rng = np.random.default_rng(0)
    x = rng.normal(size=60); y = 2 * x + rng.normal(size=60)
    ax = m.plot_scatter_with_trend(x, y)
    assert _labels_ok(ax)
    assert len(ax.collections) == 1 and len(ax.collections[0].get_offsets()) == 60
    assert len(ax.lines) == 1
