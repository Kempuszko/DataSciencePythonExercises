"""Lab 09 – Statystyka od podstaw (tylko NumPy)."""
import numpy as np

def bootstrap_ci(x, stat=np.mean, n_boot=2000, alpha=0.05, seed=0):
    """Percentylowy przedział ufności bootstrap dla statystyki `stat`.

    Losuj ze zwracaniem (rng = np.random.default_rng(seed)), n_boot powtórzeń.
    Zwróć krotkę (dolna, górna) = percentyle alpha/2 i 1-alpha/2.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def welch_t(a, b):
    """Statystyka t Welcha: (mean_a - mean_b) / sqrt(var_a/n_a + var_b/n_b), ddof=1."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def cohens_d(a, b):
    """Rozmiar efektu d Cohena z połączonym odchyleniem standardowym (ddof=1):
    sp = sqrt(((na-1)va + (nb-1)vb) / (na+nb-2)); d = (mean_a - mean_b)/sp."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def permutation_test(a, b, n_perm=5000, seed=0):
    """Dwustronny test permutacyjny różnicy średnich.

    p = (1 + #{|perm_diff| >= |obs_diff|}) / (1 + n_perm)
    (rng = np.random.default_rng(seed), mieszaj połączoną próbę).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
