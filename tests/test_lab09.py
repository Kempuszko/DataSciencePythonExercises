import numpy as np
import pandas as pd
from loader import DATA, load

m = load("lab09")
rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = 4.0 + X @ np.array([1.5, -2.0, 0.5]) + rng.normal(0, 0.1, 200)
YT = [1, 1, 1, 0, 0, 0, 0, 1]
YP = [1, 0, 1, 0, 1, 0, 0, 1]


def test_a_split_sizes_and_disjoint():
    Xtr, Xte, ytr, yte = m.train_test_split_manual(X, y, 0.25, seed=1)
    assert len(Xte) == 50 and len(Xtr) == 150 and len(ytr) == 150 and len(yte) == 50
    rows = {tuple(r) for r in Xtr} & {tuple(r) for r in Xte}
    assert not rows
    a = m.train_test_split_manual(X, y, 0.25, seed=1)[1]
    assert np.array_equal(a, Xte)


def test_a_fit_linear_recovers_weights():
    w = m.fit_linear(X, y)
    assert np.allclose(w, [4.0, 1.5, -2.0, 0.5], atol=0.05)


def test_a_predict_and_r2():
    w = m.fit_linear(X, y)
    r2 = m.r2_score_manual(y, m.predict_linear(w, X))
    assert r2 > 0.99
    assert abs(m.r2_score_manual([1, 2, 3], [1, 2, 3]) - 1) < 1e-12
    assert abs(m.r2_score_manual([1, 2, 3], [2, 2, 2])) < 1e-12


def test_b_confusion_counts():
    assert m.confusion_counts(YT, YP) == {"tp": 3, "fp": 1, "tn": 3, "fn": 1}


def test_b_prf():
    p, r, f = m.precision_recall_f1(YT, YP)
    assert abs(p - 0.75) < 1e-9 and abs(r - 0.75) < 1e-9 and abs(f - 0.75) < 1e-9


def test_b_prf_zero_division():
    assert m.precision_recall_f1([0, 0], [0, 0]) == (0.0, 0.0, 0.0)


def test_b_kfold():
    folds = m.kfold_indices(23, 5, seed=1)
    assert len(folds) == 5
    all_test = np.concatenate([te for _, te in folds])
    assert sorted(all_test.tolist()) == list(range(23))
    for tr, te in folds:
        assert not set(tr) & set(te) and len(tr) + len(te) == 23
    sizes = sorted(len(te) for _, te in folds)
    assert sizes[-1] - sizes[0] <= 1
