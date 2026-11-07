import pandas as pd
from loader import DATA, load

m = load("lab04")


def _df():
    return m.load_sales(DATA / "sales.csv")


def test_load_sales_dates():
    df = _df()
    assert str(df["date"].dtype).startswith("datetime64")
    assert len(df) == 3000


def test_top_countries():
    df = _df()
    r = m.top_countries(df, 3)
    assert len(r) == 3 and r.is_monotonic_decreasing
    expected = df.groupby("country")["amount"].sum().nlargest(3)
    assert list(r.index) == list(expected.index)
    assert abs(r.iloc[0] - expected.iloc[0]) < 1e-6


def test_revenue_by_month():
    df = _df()
    r = m.revenue_by_month(df)
    assert r.index[0] == "2024-01" and r.index.is_monotonic_increasing
    assert abs(r.sum() - df["amount"].sum()) < 1e-6


def test_large_orders():
    df = _df()
    r = m.large_orders(df, 5000)
    assert (r["amount"] > 5000).all() and r["amount"].is_monotonic_decreasing
    assert list(r.index) == list(range(len(r)))
    assert len(r) == (df["amount"] > 5000).sum()
