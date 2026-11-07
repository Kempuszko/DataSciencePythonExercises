"""Lab 04 – Pandas I: wczytywanie, selekcja, agregacje."""
import pandas as pd

def load_sales(path):
    """Wczytaj sales.csv; kolumna `date` ma mieć typ datetime64."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def top_countries(df, n=3):
    """Zwróć Series: n krajów o największym łącznym `amount` (malejąco).

    Indeks = kraj, wartości = suma amount.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def revenue_by_month(df):
    """Zwróć Series: suma `amount` per miesiąc; indeks jako tekst 'YYYY-MM', rosnąco."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def large_orders(df, threshold):
    """Zwróć DataFrame zamówień z amount > threshold, posortowany malejąco po amount.

    Indeks zresetuj (0..k-1).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
