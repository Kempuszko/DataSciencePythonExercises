"""Lab 08 – EDA: funkcje pomocnicze do mini-projektu."""
import numpy as np
import pandas as pd

def eda_summary(df):
    """Zwróć dict z podsumowaniem DataFrame:

    n_rows, n_cols,
    missing – dict {kolumna: liczba braków} tylko dla kolumn z brakami,
    numeric_cols – lista nazw kolumn liczbowych (kolejność jak w df),
    categorical_cols – lista kolumn tekstowych/kategorii,
    duplicates – liczba zduplikowanych wierszy.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def correlation_pairs(df, threshold=0.5):
    """Pary kolumn liczbowych o |korelacji Pearsona| >= threshold.

    Zwróć listę krotek (kol_a, kol_b, r) z a < b alfabetycznie, każda para raz,
    posortowaną malejąco po |r|; r zaokrąglone do 3 miejsc.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def top_categories(df, col, n=3):
    """Zwróć Series z udziałem (0-1) n najczęstszych wartości kolumny `col`
    (value_counts(normalize=True)), malejąco; NaN ignoruj."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def group_profile(df, by, target):
    """Profil grup: DataFrame z indeksem = wartości `by` i kolumnami
    count, mean, median dla kolumny `target`, posortowany malejąco po mean."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
