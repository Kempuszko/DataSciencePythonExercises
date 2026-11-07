import numpy as np
from loader import load

m = load("lab10")
rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = 4.0 + X @ np.array([1.5, -2.0, 0.5]) + rng.normal(0, 0.1, 200)


def test_split_sizes_and_disjoint():
    Xtr, Xte, ytr, yte = m.train_test_split_manual(X, y, 0.25, seed=1)
    assert len(Xte) == 50 and len(Xtr) == 150 and len(ytr) == 150 and len(yte) == 50
    rows = {tuple(r) for r in Xtr} & {tuple(r) for r in Xte}
    assert not rows
    a = m.train_test_split_manual(X, y, 0.25, seed=1)[1]
    assert np.array_equal(a, Xte)


def test_fit_linear_recovers_weights():
    w = m.fit_linear(X, y)
    assert np.allclose(w, [4.0, 1.5, -2.0, 0.5], atol=0.05)


def test_predict_and_r2():
    w = m.fit_linear(X, y)
    r2 = m.r2_score_manual(y, m.predict_linear(w, X))
    assert r2 > 0.99
    assert abs(m.r2_score_manual([1, 2, 3], [1, 2, 3]) - 1) < 1e-12
    assert abs(m.r2_score_manual([1, 2, 3], [2, 2, 2])) < 1e-12


def test_knn():
    Xtr = np.array([[0, 0], [0, 1], [1, 0], [10, 10], [10, 11], [11, 10]], float)
    ytr = np.array([0, 0, 0, 1, 1, 1])
    pred = m.knn_predict(Xtr, ytr, np.array([[0.2, 0.2], [10.5, 10.4]]), k=3)
    assert pred.tolist() == [0, 1]


def test_knn_tie_prefers_smaller_label():
    Xtr = np.array([[0.0], [2.0]]); ytr = np.array([1, 0])
    assert m.knn_predict(Xtr, ytr, np.array([[1.0]]), k=2).tolist() == [0]
