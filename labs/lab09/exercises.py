"""Lab 09 – Uczenie maszynowe: regresja, klasyfikacja, metryki, walidacja."""
import numpy as np

# --- część A ---
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

# --- część B ---
def confusion_counts(y_true, y_pred):
    """Zwróć dict {'tp','fp','tn','fn'} dla klasyfikacji binarnej (klasa pozytywna = 1)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def precision_recall_f1(y_true, y_pred):
    """Zwróć (precision, recall, f1). Gdy mianownik == 0, dana miara = 0.0."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def kfold_indices(n, k, seed=0):
    """Podział na k foldów: lista k krotek (train_idx, test_idx).

    Permutacja rng = np.random.default_rng(seed).permutation(n); foldy jak
    np.array_split (rozmiary różnią się co najwyżej o 1); każdy indeks trafia
    do test dokładnie raz.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
