"""Lab 11 – Klasyfikacja: metryki i walidacja krzyżowa od zera (NumPy)."""
import numpy as np

def confusion_counts(y_true, y_pred):
    """Zwróć dict {'tp','fp','tn','fn'} dla klasyfikacji binarnej (klasa pozytywna = 1)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def precision_recall_f1(y_true, y_pred):
    """Zwróć (precision, recall, f1). Gdy mianownik == 0, dana miara = 0.0."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def roc_auc_manual(y_true, scores):
    """AUC-ROC przez statystykę rangową (Mann-Whitney), z obsługą remisów
    (rangi średnie). Bez sklearn."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def kfold_indices(n, k, seed=0):
    """Podział na k foldów: lista k krotek (train_idx, test_idx).

    Permutacja rng = np.random.default_rng(seed).permutation(n); foldy jak
    np.array_split (rozmiary różnią się co najwyżej o 1); każdy indeks trafia
    do test dokładnie raz.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
