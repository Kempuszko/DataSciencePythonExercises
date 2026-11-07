"""Lab 03 – NumPy i pandas I: wczytywanie, selekcja, agregacje."""
import numpy as np
import pandas as pd

# --- część A ---
def standardize(a):
    """Standaryzacja kolumnowa (z-score): (a - mean) / std (ddof=0).

    Kolumny o std == 0 zostaw jako zera (bez dzielenia przez 0).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def load_sales(path):
    """Wczytaj sales.csv; kolumna `date` ma mieć typ datetime64."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def top_countries(df, n=3):
    """Zwróć Series: n krajów o największym łącznym `amount` (malejąco).

    Indeks = kraj, wartości = suma amount.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def revenue_by_month(df):
    """Zwróć Series: suma `amount` per miesiąc; indeks jako tekst 'YYYY-MM', rosnąco."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
