import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab13")


class _Thresh:
    def predict(self, X):
        return (np.asarray(X)[:, 0] > 0).astype(int)


def test_a_gini():
    assert m.gini([]) == 0.0 and m.gini([1, 1, 1]) == 0.0
    assert abs(m.gini([0, 1]) - 0.5) < 1e-12
    assert abs(m.gini([0, 0, 1, 2]) - (1 - (0.25 + 0.0625 + 0.0625))) < 1e-12


def test_a_best_split():
    t, g = m.best_split([1, 2, 3, 10, 11, 12], [0, 0, 0, 1, 1, 1])
    assert abs(t - 6.5) < 1e-9 and abs(g) < 1e-12


def test_a_best_split_noisy_and_constant():
    t, g = m.best_split([1, 2, 3, 4, 5, 6], [0, 0, 1, 0, 1, 1])
    assert 0 <= g < 0.5 and t is not None
    assert m.best_split([5, 5, 5], [0, 1, 0])[0] is None


def test_b_bagging_predict():
    P = [[0, 1, 1], [0, 0, 1], [1, 0, 1]]
    assert m.bagging_predict(P).tolist() == [0, 0, 1]
    assert m.bagging_predict([[0, 1], [1, 0]]).tolist() == [0, 0]


def test_b_permutation_importance():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(300, 3)); y = (X[:, 0] > 0).astype(int)
    acc = lambda t, p: float((np.asarray(t) == np.asarray(p)).mean())
    imp = m.permutation_importance(_Thresh(), X, y, acc, n_repeats=10, seed=1)
    assert imp.shape == (3,) and imp[0] > 0.3
    assert abs(imp[1]) < 1e-12 and abs(imp[2]) < 1e-12
