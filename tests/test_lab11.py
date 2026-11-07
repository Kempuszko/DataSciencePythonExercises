import numpy as np
from loader import load

m = load("lab11")
YT = [1, 1, 1, 0, 0, 0, 0, 1]
YP = [1, 0, 1, 0, 1, 0, 0, 1]


def test_confusion_counts():
    assert m.confusion_counts(YT, YP) == {"tp": 3, "fp": 1, "tn": 3, "fn": 1}


def test_prf():
    p, r, f = m.precision_recall_f1(YT, YP)
    assert abs(p - 0.75) < 1e-9 and abs(r - 0.75) < 1e-9 and abs(f - 0.75) < 1e-9


def test_prf_zero_division():
    assert m.precision_recall_f1([0, 0], [0, 0]) == (0.0, 0.0, 0.0)


def test_auc():
    assert abs(m.roc_auc_manual([0, 0, 1, 1], [0.1, 0.4, 0.35, 0.8]) - 0.75) < 1e-9
    assert abs(m.roc_auc_manual([0, 1], [0.5, 0.5]) - 0.5) < 1e-9  # remis
    rng = np.random.default_rng(0)
    y = rng.integers(0, 2, 300); s = y + rng.normal(0, 1, 300)
    assert 0.7 < m.roc_auc_manual(y, s) < 0.95


def test_kfold():
    folds = m.kfold_indices(23, 5, seed=1)
    assert len(folds) == 5
    all_test = np.concatenate([te for _, te in folds])
    assert sorted(all_test.tolist()) == list(range(23))
    for tr, te in folds:
        assert not set(tr) & set(te) and len(tr) + len(te) == 23
    sizes = sorted(len(te) for _, te in folds)
    assert sizes[-1] - sizes[0] <= 1
