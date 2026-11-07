"""Lab 14 – Wydajność i pamięć w pandas."""
import numpy as np
import pandas as pd

def memory_mb(df):
    """Całkowite zużycie pamięci DataFrame (deep=True) w MB (1 MB = 1024**2 B)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def optimize_dtypes(df, cat_threshold=0.5):
    """Zwróć KOPIĘ df ze zmniejszonymi typami:
    - liczby całkowite -> najmniejszy możliwy int (pd.to_numeric downcast='integer'),
    - liczby zmiennoprzecinkowe -> float32,
    - kolumny tekstowe, w których unikalnych wartości jest < cat_threshold * len(df)
      -> 'category'.
    Wartości (po rzutowaniu) muszą pozostać równe oryginałowi (float32: z tolerancją).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def chunked_group_sum(path, by, col, chunksize=500):
    """Suma `col` w grupach `by` z pliku CSV czytanego fragmentami (chunksize wierszy),
    bez wczytywania całości. Zwróć Series posortowaną po indeksie."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def haversine_vectorized(lat1, lon1, lat2, lon2):
    """Odległość wielkiego koła w km (R=6371) – wektoryzowana wersja na tablicach NumPy
    (bez pętli). Wejście w stopniach."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
