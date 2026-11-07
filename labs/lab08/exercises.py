"""Lab 08 – Wizualizacja, EDA i wnioskowanie statystyczne."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- część A ---
def plot_monthly_revenue(series):
    """Wykres liniowy przychodu miesięcznego (indeks = miesiące, wartości = przychód).

    Wymagania: tytuł, opisy osi x i y (niepuste), dokładnie jedna linia
    z len(series) punktami, etykiety osi x obrócone o 45 stopni.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def eda_summary(df):
    """Zwróć dict z podsumowaniem DataFrame:

    n_rows, n_cols,
    missing – dict {kolumna: liczba braków} tylko dla kolumn z brakami,
    numeric_cols – lista nazw kolumn liczbowych (kolejność jak w df),
    categorical_cols – lista kolumn tekstowych/kategorii (w pandas 3 tekst to dtype `str`,
                       nie `object` – użyj pd.api.types.is_string_dtype),
    duplicates – liczba zduplikowanych wierszy.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def bootstrap_ci(x, stat=np.mean, n_boot=2000, alpha=0.05, seed=0):
    """Percentylowy przedział ufności bootstrap dla statystyki `stat`.

    Losuj ze zwracaniem (rng = np.random.default_rng(seed)), n_boot powtórzeń.
    Zwróć krotkę (dolna, górna) = percentyle alpha/2 i 1-alpha/2.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def permutation_test(a, b, n_perm=5000, seed=0):
    """Dwustronny test permutacyjny różnicy średnich.

    p = (1 + #{|perm_diff| >= |obs_diff|}) / (1 + n_perm)
    (rng = np.random.default_rng(seed), mieszaj połączoną próbę).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
