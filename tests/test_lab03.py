import numpy as np
from loader import load

m = load("lab03")


def test_standardize():
    a = np.array([[1., 5.], [2., 5.], [3., 5.]])
    z = m.standardize(a)
    assert np.allclose(z[:, 0].mean(), 0) and np.allclose(z[:, 0].std(), 1)
    assert np.allclose(z[:, 1], 0)  # stała kolumna -> zera, bez NaN


def test_pairwise_distances():
    X = np.array([[0., 0.], [3., 4.], [6., 8.]])
    D = m.pairwise_distances(X)
    assert D.shape == (3, 3)
    assert np.allclose(D, [[0, 5, 10], [5, 0, 5], [10, 5, 0]])


def test_pairwise_random_symmetry():
    X = np.random.default_rng(0).normal(size=(20, 4))
    D = m.pairwise_distances(X)
    assert np.allclose(D, D.T) and np.allclose(np.diag(D), 0)


def test_rolling_mean():
    r = m.rolling_mean([1, 2, 3, 4, 5], 3)
    assert np.allclose(r, [2, 3, 4])


def test_one_hot():
    o = m.one_hot([0, 2, 1], 3)
    assert o.tolist() == [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
    assert o.dtype.kind == "i"
