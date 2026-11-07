import sqlite3

import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab07")
sales = pd.read_csv(DATA / "sales.csv")
cust = pd.read_csv(DATA / "customers.csv")


def _q(sql):
    conn = sqlite3.connect(":memory:")
    sales.to_sql("orders", conn, index=False)
    cust.to_sql("customers", conn, index=False)
    return pd.read_sql_query(sql, conn)


def _monthly():
    return sales.groupby(sales["date"].str[:7])["amount"].sum()


def test_a_sql_monthly_revenue():
    r = _q(m.sql_monthly_revenue())
    assert list(r.columns) == ["month", "revenue"]
    exp = _monthly()
    assert list(r["month"]) == list(exp.index) and np.allclose(r["revenue"], exp.round(2))


def test_a_sql_top_products():
    r = _q(m.sql_top_products(3))
    assert list(r.columns) == ["product", "units", "revenue"] and len(r) == 3
    g = sales.groupby("product").agg(units=("quantity", "sum"), revenue=("amount", "sum")).sort_values("revenue", ascending=False).head(3)
    assert list(r["product"]) == list(g.index) and list(r["units"]) == list(g["units"])
    assert np.allclose(r["revenue"], g["revenue"].round(2))


def test_a_sql_top_products_n():
    assert len(_q(m.sql_top_products(1))) == 1 and len(_q(m.sql_top_products(5))) == 5


def test_b_sql_running_total():
    r = _q(m.sql_running_total())
    assert list(r.columns) == ["month", "revenue", "running_revenue"]
    exp = _monthly()
    assert np.allclose(r["running_revenue"], exp.cumsum().round(2), atol=0.011)
    assert abs(r["running_revenue"].iloc[-1] - sales["amount"].sum()) < 0.5


def test_b_sql_top3_customers_per_country():
    r = _q(m.sql_top3_customers_per_country())
    assert list(r.columns) == ["country", "customer_id", "revenue", "rank_in_country"]
    assert r["rank_in_country"].between(1, 3).all()
    j = sales.drop(columns="country").merge(cust[["customer_id", "country"]], on="customer_id")
    g = j.groupby(["country", "customer_id"])["amount"].sum().reset_index()
    g["rk"] = g.groupby("country")["amount"].rank(method="min", ascending=False)
    exp = g[g["rk"] <= 3].sort_values(["country", "rk", "customer_id"])
    assert list(r["customer_id"]) == list(exp["customer_id"])
    assert list(r["rank_in_country"]) == list(exp["rk"].astype(int))
