"""Lab 10 – Podstawy ML od zera (NumPy), potem porównanie ze scikit-learn."""
import numpy as np

def train_test_split_manual(X, y, test_size=0.25, seed=0):
    """Losowy podział: zwróć X_train, X_test, y_train, y_test.

    rng = np.random.default_rng(seed); permutacja indeksów; n_test = round(n*test_size);
    pierwsze n_test indeksów -> test, reszta -> train.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def fit_linear(X, y):
    """Regresja liniowa OLS z wyrazem wolnym. Zwróć wektor wag [b0, b1, ..., bp]
    (b0 = intercept). Użyj np.linalg.lstsq."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def predict_linear(w, X):
    """Predykcje modelu liniowego z wag zwróconych przez fit_linear."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def r2_score_manual(y_true, y_pred):
    """Współczynnik determinacji R^2 = 1 - SS_res / SS_tot."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def knn_predict(X_train, y_train, X_test, k=3):
    """Klasyfikator k-NN (odległość euklidesowa, głosowanie większościowe).

    Remis głosów rozstrzygaj wybierając mniejszą etykietę. Bez sklearn.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
