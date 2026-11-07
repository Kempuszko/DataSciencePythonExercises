import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab10")
churn = pd.read_csv(DATA / "churn.csv")


def test_a_find_leaky_columns():
    assert m.find_leaky_columns(churn, "churned") == ["cancellation_reason"]


def test_a_find_leaky_numeric():
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [0, 0, 1, 1], "z": [5, 1, 4, 2]})
    df["leak"] = df["y"] * 10
    assert m.find_leaky_columns(df, "y", 0.95) == ["leak"]


def test_a_add_features_copy():
    before = churn.copy()
    r = m.add_features(churn)
    pd.testing.assert_frame_equal(churn, before)
    assert {"charges_per_month_tenure", "is_new", "many_calls"} <= set(r.columns)
    assert r["is_new"].dtype == bool


def test_b_target_encode_no_leak():
    tr = pd.DataFrame({"c": ["a", "a", "b"], "t": [1, 0, 1]})
    te = pd.DataFrame({"c": ["a", "z"], "t": [0, 0]})
    etr, ete = m.target_encode(tr, te, "c", "t", smoothing=2)
    gm = 2 / 3
    assert abs(etr.iloc[0] - (2 * 0.5 + 2 * gm) / 4) < 1e-9
    assert abs(ete.iloc[1] - gm) < 1e-9          # nieznana kategoria
    assert abs(ete.iloc[0] - etr.iloc[0]) < 1e-9


def test_b_build_pipeline_fits():
    try:
        import sklearn  # noqa: F401
    except ImportError:
        return  # lokalnie bez sklearn; w CI jest zainstalowany
    num = ["tenure_months", "monthly_charges", "support_calls"]
    cat = ["contract", "internet"]
    pipe = m.build_pipeline(num, cat)
    assert [n for n, _ in pipe.steps] == ["prep", "model"]
    X = churn[num + cat]; y = churn["churned"]
    pipe.fit(X.iloc[:1500], y.iloc[:1500])  # NaN w monthly_charges musi przejść
    assert pipe.score(X.iloc[1500:], y.iloc[1500:]) > 0.6
