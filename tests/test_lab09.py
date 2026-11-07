import numpy as np
from loader import load

m = load("lab09")
rng = np.random.default_rng(1)
A = rng.normal(10, 2, 80)
B = rng.normal(11, 2, 90)


def test_bootstrap_ci_contains_mean_and_deterministic():
    lo, hi = m.bootstrap_ci(A, n_boot=1000, seed=3)
    assert lo < A.mean() < hi and 0 < hi - lo < 2
    assert m.bootstrap_ci(A, n_boot=1000, seed=3) == (lo, hi)


def test_bootstrap_ci_other_stat():
    lo, hi = m.bootstrap_ci(A, stat=np.median, n_boot=500, seed=0)
    assert lo < np.median(A) < hi


def test_welch_t():
    expected = (A.mean() - B.mean()) / np.sqrt(A.var(ddof=1) / 80 + B.var(ddof=1) / 90)
    assert abs(m.welch_t(A, B) - expected) < 1e-9
    assert m.welch_t(A, B) < 0


def test_cohens_d():
    d = m.cohens_d(B, A)
    assert 0.2 < d < 1.0
    assert abs(m.cohens_d(A, B) + d) < 1e-12


def test_permutation_test_detects_difference():
    assert m.permutation_test(A, B, n_perm=2000, seed=0) < 0.05
    same = rng.normal(0, 1, 60)
    assert m.permutation_test(same, same + rng.normal(0, 1e-3, 60), n_perm=500, seed=0) > 0.5


def test_permutation_p_in_range():
    p = m.permutation_test([1, 2, 3], [1, 2, 3], n_perm=200, seed=0)
    assert 0 < p <= 1
