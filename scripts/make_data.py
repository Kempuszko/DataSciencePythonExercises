"""Generuje deterministyczne, syntetyczne zbiory danych do ćwiczeń (seed=42).

Uruchom:  python scripts/make_data.py
Wynik trafia do katalogu data/ (pliki są w repo, więc studenci NIE muszą tego uruchamiać).
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "data"
rng = np.random.default_rng(42)

COUNTRIES = ["PL", "DE", "CZ", "SK", "FR", "UK"]
PRODUCTS = {
    "laptop": ("electronics", 3200), "phone": ("electronics", 1800),
    "headset": ("electronics", 250), "desk": ("furniture", 900),
    "chair": ("furniture", 650), "lamp": ("furniture", 120),
    "notebook": ("office", 15), "pen": ("office", 5), "monitor": ("electronics", 1100),
}


def customers(n=300):
    df = pd.DataFrame({
        "customer_id": np.arange(1, n + 1),
        "country": rng.choice(COUNTRIES, n, p=[.35, .25, .12, .08, .12, .08]),
        "segment": rng.choice(["consumer", "business", "education"], n, p=[.6, .3, .1]),
        "signup_date": pd.to_datetime("2022-01-01") + pd.to_timedelta(rng.integers(0, 900, n), "D"),
    })
    return df


def sales(cust, n=3000):
    names = list(PRODUCTS)
    prod = rng.choice(names, n)
    qty = rng.integers(1, 6, n)
    base = np.array([PRODUCTS[p][1] for p in prod])
    price = base * rng.normal(1, .08, n)
    cid = rng.choice(cust.customer_id, n)
    df = pd.DataFrame({
        "order_id": np.arange(1, n + 1),
        "date": pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 640, n), "D"),
        "customer_id": cid,
        "product": prod,
        "category": [PRODUCTS[p][0] for p in prod],
        "quantity": qty,
        "amount": (price * qty).round(2),
    })
    df["country"] = df.customer_id.map(cust.set_index("customer_id").country)
    df = df.sort_values("date").reset_index(drop=True)
    df["order_id"] = np.arange(1, n + 1)
    return df[["order_id", "date", "customer_id", "product", "category", "quantity", "amount", "country"]]


def dirty(df):
    d = df.copy()
    d["date"] = d["date"].dt.strftime("%Y-%m-%d")
    idx = rng.choice(len(d), 150, replace=False)
    d.loc[idx[:50], "date"] = pd.to_datetime(d.loc[idx[:50], "date"]).dt.strftime("%d/%m/%Y")
    d.loc[idx[50:80], "country"] = d.loc[idx[50:80], "country"].str.lower()
    d.loc[idx[80:110], "country"] = " " + d.loc[idx[80:110], "country"] + " "
    d["amount"] = d["amount"].astype(object)
    d.loc[idx[110:130], "amount"] = d.loc[idx[110:130], "amount"].map(lambda v: f"{v:.2f} PLN")
    d.loc[idx[130:140], "amount"] = -abs(d.loc[idx[130:140], "amount"].astype(float))
    d.loc[idx[140:], "amount"] = np.nan
    d.loc[rng.choice(len(d), 80, replace=False), "quantity"] = np.nan
    d.loc[rng.choice(len(d), 6, replace=False), "amount"] = 99999.0  # outliery
    d = pd.concat([d, d.sample(40, random_state=1)], ignore_index=True)  # duplikaty
    return d.sample(frac=1, random_state=3).reset_index(drop=True)


def churn(n=2000):
    tenure = rng.integers(1, 72, n)
    monthly = rng.normal(70, 25, n).clip(20, 150).round(2)
    support = rng.poisson(2, n)
    contract = rng.choice(["monthly", "yearly", "two_year"], n, p=[.55, .25, .2])
    internet = rng.choice(["dsl", "fiber", "none"], n, p=[.3, .5, .2])
    z = (-0.04 * tenure + 0.02 * (monthly - 70) + 0.35 * support
         + np.where(contract == "monthly", 1.0, np.where(contract == "yearly", -0.3, -1.0)) - 0.2)
    p = 1 / (1 + np.exp(-z))
    y = (rng.random(n) < p).astype(int)
    df = pd.DataFrame({"customer_id": np.arange(1, n + 1), "tenure_months": tenure,
                       "monthly_charges": monthly, "support_calls": support,
                       "contract": contract, "internet": internet, "churned": y})
    # kolumna przeciekająca (wycieka target) – do ćwiczenia o data leakage
    df["cancellation_reason"] = np.where(y == 1, rng.choice(["price", "service", "moved"], n), "none")
    df.loc[rng.choice(n, 60, replace=False), "monthly_charges"] = np.nan
    return df


def housing(n=800):
    area = rng.normal(70, 25, n).clip(20, 200)
    rooms = np.clip((area / 25 + rng.normal(0, .6, n)).round(), 1, 8)
    dist = rng.exponential(6, n).clip(0.3, 30)
    age = rng.integers(0, 80, n)
    price = 6000 * area - 9000 * dist - 800 * age + 15000 * rooms + rng.normal(0, 40000, n) + 100000
    return pd.DataFrame({"area_m2": area.round(1), "rooms": rooms.astype(int),
                         "dist_center_km": dist.round(2), "age_years": age, "price_pln": price.round(-2)})


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    c = customers(); s = sales(c)
    c.to_csv(OUT / "customers.csv", index=False)
    s.to_csv(OUT / "sales.csv", index=False)
    dirty(s).to_csv(OUT / "sales_dirty.csv", index=False)
    churn().to_csv(OUT / "churn.csv", index=False)
    housing().to_csv(OUT / "housing.csv", index=False)
    print("OK:", sorted(p.name for p in OUT.glob("*.csv")))
