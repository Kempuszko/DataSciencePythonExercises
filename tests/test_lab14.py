import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab14")
sales = pd.read_csv(DATA / "sales.csv")


def test_a_memory_mb():
    df = pd.DataFrame({"a": np.arange(1024 * 128, dtype="int64")})
    assert abs(m.memory_mb(df) - 1.0) < 0.01


def test_a_optimize_dtypes_saves_memory_and_keeps_values():
    opt = m.optimize_dtypes(sales)
    assert m.memory_mb(opt) < 0.5 * m.memory_mb(sales)
    assert str(opt["country"].dtype) == "category" and str(opt["product"].dtype) == "category"
    assert opt["quantity"].dtype.itemsize == 1
    assert np.allclose(opt["amount"], sales["amount"], rtol=1e-5)
    assert (opt["order_id"].astype("int64") == sales["order_id"]).all()


def test_a_optimize_dtypes_does_not_mutate():
    before = sales.copy()
    m.optimize_dtypes(sales)
    pd.testing.assert_frame_equal(sales, before)


def test_b_chunked_group_sum():
    r = m.chunked_group_sum(DATA / "sales.csv", "country", "amount", chunksize=400)
    expected = sales.groupby("country")["amount"].sum().sort_index()
    assert list(r.index) == list(expected.index)
    assert np.allclose(r.to_numpy(), expected.to_numpy())


def test_b_haversine():
    d = m.haversine_vectorized(np.array([52.2297, 0.0]), np.array([21.0122, 0.0]),
                               np.array([50.0647, 0.0]), np.array([19.9450, 1.0]))
    assert abs(d[0] - 252) < 3     # Warszawa -> Kraków
    assert abs(d[1] - 111.19) < 0.5
