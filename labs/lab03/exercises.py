"""Lab 03 – NumPy: wektoryzacja, broadcasting."""
import numpy as np

def standardize(a):
    """Standaryzacja kolumnowa (z-score): (a - mean) / std (ddof=0).

    Kolumny o std == 0 zostaw jako zera (bez dzielenia przez 0).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def pairwise_distances(X):
    """Macierz odległości euklidesowych (n, n) między wierszami X – BEZ pętli.

    Wskazówka: broadcasting X[:, None, :] - X[None, :, :].
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def rolling_mean(x, k):
    """Średnia krocząca przez cumsum (bez pętli). Długość wyniku: len(x)-k+1."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def one_hot(labels, n_classes):
    """One-hot dla wektora etykiet 0..n_classes-1 -> macierz (len, n_classes) typu int."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
