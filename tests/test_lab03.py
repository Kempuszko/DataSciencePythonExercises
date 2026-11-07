import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab03")


def _df():
    return m.load_sales(DATA / "sales.csv")


def test_a_standardize():
    a = np.array([[1., 5.], [2., 5.], [3., 5.]])
    z = m.standardize(a)
    assert np.allclose(z[:, 0].mean(), 0) and np.allclose(z[:, 0].std(), 1)
    assert np.allclose(z[:, 1], 0)


def test_a_load_sales_dates():
    df = _df()
    assert str(df["date"].dtype).startswith("datetime64")
    assert len(df) == 3000


def test_b_top_countries():
    df = _df()
    r = m.top_countries(df, 3)
    assert len(r) == 3 and r.is_monotonic_decreasing
    expected = df.groupby("country")["amount"].sum().nlargest(3)
    assert list(r.index) == list(expected.index)
    assert abs(r.iloc[0] - expected.iloc[0]) < 1e-6


def test_b_revenue_by_month():
    df = _df()
    r = m.revenue_by_month(df)
    assert r.index[0] == "2024-01" and r.index.is_monotonic_increasing
    assert abs(r.sum() - df["amount"].sum()) < 1e-6
