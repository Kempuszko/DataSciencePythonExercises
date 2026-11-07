import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab05")
raw = pd.read_csv(DATA / "sales_dirty.csv")


def test_a_parse_mixed_dates():
    s = pd.Series(["2024-05-23", "23/05/2024", "01/02/2024"])
    r = m.parse_mixed_dates(s)
    assert r.tolist() == [pd.Timestamp("2024-05-23"), pd.Timestamp("2024-05-23"), pd.Timestamp("2024-02-01")]


def test_a_clean_does_not_mutate_input():
    before = raw.copy()
    m.clean_sales(raw)
    pd.testing.assert_frame_equal(raw, before)


def test_a_clean_sales_rules():
    c = m.clean_sales(raw)
    assert not c.duplicated().any()
    assert c["order_id"].is_unique and c["order_id"].is_monotonic_increasing
    assert set(c["country"]) <= {"PL", "DE", "CZ", "SK", "FR", "UK"}
    assert c["amount"].dtype.kind == "f" and (c["amount"] > 0).all() and c["amount"].notna().all()
    assert c["quantity"].dtype.kind == "i" and c["quantity"].notna().all()
    assert str(c["date"].dtype).startswith("datetime64") and c["date"].notna().all()
    assert list(c.index) == list(range(len(c)))


def test_a_clean_sales_keeps_good_rows():
    c = m.clean_sales(raw)
    assert 2800 <= len(c) <= 3000


def test_b_detect_outliers_iqr():
    s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 100])
    mask = m.detect_outliers_iqr(s)
    assert mask.tolist() == [False] * 8 + [True]


def test_b_missing_report():
    df = pd.DataFrame({"a": [1, None, None], "b": [1, 2, None], "c": [1, 2, 3]})
    r = m.missing_report(df)
    assert list(r.index) == ["a", "b", "c"]
    assert r.loc["a", "missing"] == 2 and r.loc["a", "pct"] == 66.67
