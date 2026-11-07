"""Lab 13 (dodatkowy) – Drzewa decyzyjne, ensemble, interpretacja."""
import numpy as np

# --- część A ---
def gini(y):
    """Nieczystość Gini'ego zbioru etykiet: 1 - sum(p_k^2). Pusty zbiór -> 0.0."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def best_split(x, y):
    """Najlepszy próg podziału jednej cechy `x` dla etykiet `y` (minimalizacja
    ważonego Gini). Kandydaci: środki między kolejnymi różnymi posortowanymi
    wartościami. Zwróć (próg, ważony_gini). Brak kandydatów -> (None, gini(y))."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def bagging_predict(models_preds):
    """Agregacja klasyfikatorów przez głosowanie większościowe.

    `models_preds` – tablica (n_models, n_samples) z etykietami; zwróć wektor
    n_samples (remis -> mniejsza etykieta)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def permutation_importance(model, X, y, metric, n_repeats=5, seed=0):
    """Ważność cech przez permutację (model-agnostyczna).

    model.predict(X) -> predykcje; metric(y, pred) -> wynik (wyższy = lepszy).
    Dla każdej kolumny j: średni spadek metric po przetasowaniu kolumny j
    (n_repeats razy; rng = np.random.default_rng(seed)). Zwróć wektor (n_features,).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
