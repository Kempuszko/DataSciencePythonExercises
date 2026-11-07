import sqlite3

import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab06")
cust = pd.read_csv(DATA / "customers.csv").head(50)


def _db():
    conn = sqlite3.connect(":memory:")
    m.create_schema(conn)
    return conn


def _raises(exc, f):
    try:
        f()
    except exc:
        return True
    return False


def test_a_generate_orders_shape_and_determinism():
    a = m.generate_orders(300, seed=7)
    b = m.generate_orders(300, seed=7)
    assert list(a.columns) == ["order_id", "date", "customer_id", "product", "quantity", "amount"]
    assert len(a) == 300 and a.equals(b) and not a.equals(m.generate_orders(300, seed=8))
    assert a["order_id"].tolist() == list(range(1, 301))


def test_a_generate_orders_ranges():
    a = m.generate_orders(500, seed=1)
    assert a["customer_id"].between(1, 50).all() and a["quantity"].between(1, 5).all()
    assert (a["amount"] > 0).all() and set(a["product"]) <= {"laptop", "phone", "desk", "chair", "pen"}
    d = pd.to_datetime(a["date"], format="%Y-%m-%d")
    assert d.min() >= pd.Timestamp("2024-01-01") and d.max() <= pd.Timestamp("2024-12-31")
    assert (a["amount"] * 100 % 1 < 1e-6).all() or np.allclose(a["amount"], a["amount"].round(2))


def test_a_create_schema_tables_and_index():
    conn = _db()
    names = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type IN ('table','index')")}
    assert {"customers", "orders", "idx_orders_customer"} <= names
    cols = {r[1]: r for r in conn.execute("PRAGMA table_info(orders)")}
    assert cols["order_id"][5] == 1                       # klucz główny
    assert cols["amount"][3] == 1 and cols["product"][3] == 1  # NOT NULL


def test_a_create_schema_constraints_enforced():
    conn = _db()
    conn.execute("INSERT INTO customers VALUES (1, 'PL', 'consumer', '2022-01-01')")
    conn.execute("INSERT INTO orders VALUES (1, '2024-01-01', 1, 'pen', 1, 5.0)")
    assert _raises(sqlite3.IntegrityError, lambda: conn.execute("INSERT INTO orders VALUES (2, '2024-01-01', 99, 'pen', 1, 5.0)"))  # FK
    assert _raises(sqlite3.IntegrityError, lambda: conn.execute("INSERT INTO orders VALUES (3, '2024-01-01', 1, 'pen', 0, 5.0)"))   # CHECK
    assert _raises(sqlite3.IntegrityError, lambda: conn.execute("INSERT INTO orders VALUES (1, '2024-01-01', 1, 'pen', 1, 5.0)"))   # PK


def test_b_load_into_db_counts():
    conn = _db()
    orders = m.generate_orders(200, seed=3)
    assert m.load_into_db(conn, cust, orders) == (50, 200)
    assert conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0] == 200
    assert conn.execute("SELECT COUNT(*) FROM customers").fetchone()[0] == 50


def _loaded():
    conn = _db()
    orders = m.generate_orders(400, seed=5)
    m.load_into_db(conn, cust, orders)
    return conn, orders


def test_b_revenue_by_country_sql():
    conn, orders = _loaded()
    r = m.revenue_by_country_sql(conn)
    assert list(r.columns) == ["country", "revenue", "n_orders"]
    exp = (orders.merge(cust[["customer_id", "country"]], on="customer_id")
           .groupby("country")["amount"].agg(["sum", "count"]).sort_values("sum", ascending=False))
    assert list(r["country"]) == list(exp.index)
    assert np.allclose(r["revenue"], exp["sum"].round(2)) and list(r["n_orders"]) == list(exp["count"])


def test_b_top_customers_sql():
    conn, orders = _loaded()
    r = m.top_customers_sql(conn, 4)
    assert list(r.columns) == ["customer_id", "revenue"] and len(r) == 4
    assert r["revenue"].is_monotonic_decreasing
    exp = orders.groupby("customer_id")["amount"].sum().nlargest(4)
    assert np.allclose(sorted(r["revenue"]), sorted(exp.round(2)))
