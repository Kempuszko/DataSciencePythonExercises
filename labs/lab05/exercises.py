"""Lab 05 – Czyszczenie danych i jakość danych."""
import numpy as np
import pandas as pd

# --- część A ---
def parse_mixed_dates(s):
    """Sparsuj Series tekstów w formatach 'YYYY-MM-DD' lub 'DD/MM/YYYY' do datetime64."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def clean_sales(df):
    """Wyczyść brudne dane sprzedaży i zwróć NOWY DataFrame (nie modyfikuj wejścia).

    Kroki:
      1. usuń duplikaty wierszy (pełne duplikaty),
      2. `country`: strip + upper,
      3. `amount`: usuń sufiks ' PLN', zamień na liczby (błędy -> NaN),
      4. usuń wiersze z amount NaN lub amount <= 0,
      5. `quantity`: uzupełnij braki medianą kolumny i rzutuj na int,
      6. `date`: sparsuj mieszane formaty 'YYYY-MM-DD' i 'DD/MM/YYYY' do datetime64,
      7. posortuj po order_id i zresetuj indeks.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def detect_outliers_iqr(s, k=1.5):
    """Maska bool (Series): True dla wartości poza [Q1 - k*IQR, Q3 + k*IQR]."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def missing_report(df):
    """DataFrame z kolumnami `missing` (liczba) i `pct` (0-100, zaokrąglone do 2 miejsc).

    Indeks = nazwy kolumn, posortowany malejąco po `missing`.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
