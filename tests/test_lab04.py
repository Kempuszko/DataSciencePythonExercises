import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab04")
sales = pd.read_csv(DATA / "sales.csv", parse_dates=["date"])
cust = pd.read_csv(DATA / "customers.csv", parse_dates=["signup_date"])


def test_a_revenue_pivot():
    p = m.revenue_pivot(sales)
    assert set(p.index) == {"electronics", "furniture", "office"}
    assert abs(p.to_numpy().sum() - sales["amount"].sum()) < 1e-4
    assert not p.isna().any().any()


def test_a_add_customer_info():
    r = m.add_customer_info(sales, cust)
    assert len(r) == len(sales)
    assert list(r["order_id"]) == list(sales["order_id"])
    assert "segment" in r.columns and "country_x" not in r.columns and "country_y" not in r.columns
    assert r["segment"].notna().all()


def test_a_add_customer_info_keeps_unmatched():
    o = sales.head(3).copy()
    o.loc[o.index[0], "customer_id"] = -1
    r = m.add_customer_info(o, cust)
    assert len(r) == 3 and pd.isna(r["segment"].iloc[0])


def test_b_monthly_growth():
    g = m.monthly_growth(sales)
    monthly = sales.groupby(sales["date"].dt.strftime("%Y-%m"))["amount"].sum().sort_index()
    assert len(g) == len(monthly) - 1 and g.index[0] == monthly.index[1]
    assert abs(g.iloc[0] - (monthly.iloc[1] / monthly.iloc[0] - 1)) < 1e-9


def test_b_customer_rfm():
    r = m.customer_rfm(sales, "2025-12-31")
    assert list(r.columns) == ["recency", "frequency", "monetary"]
    assert r["frequency"].sum() == len(sales)
    cid = sales["customer_id"].iloc[0]
    last = sales[sales.customer_id == cid]["date"].max()
    assert r.loc[cid, "recency"] == (pd.Timestamp("2025-12-31") - last).days
