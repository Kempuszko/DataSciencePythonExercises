"""Lab 12 – Feature engineering, pipeline'y i data leakage."""
import numpy as np
import pandas as pd

def find_leaky_columns(df, target, threshold=0.95):
    """Znajdź kolumny 'przeciekające' target.

    Dla kolumn liczbowych: |korelacja z target| >= threshold.
    Dla kolumn tekstowych: jeśli ZNAJOMOŚĆ kolumny niemal jednoznacznie wyznacza
    target, tzn. średnia (po wartościach kolumny) z max(p, 1-p) >= threshold,
    gdzie p to odsetek target==1 w danej wartości (ważona liczebnością).
    Zwróć posortowaną listę nazw (bez samego target).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def target_encode(train, test, col, target, smoothing=10):
    """Bezpieczne (bez przecieku) target encoding.

    Dla każdej kategorii: (n*mean_cat + smoothing*global_mean) / (n + smoothing),
    gdzie statystyki liczone są WYŁĄCZNIE na `train`. Nieznane kategorie w `test`
    dostają global_mean z train. Zwróć (train_encoded, test_encoded) jako Series.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def add_features(df):
    """Dodaj do KOPII churn df kolumny:
    charges_per_month_tenure = monthly_charges * tenure_months,
    is_new = tenure_months < 12 (bool),
    many_calls = support_calls >= 4 (bool).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def build_pipeline(num_cols, cat_cols):
    """Zwróć sklearn Pipeline: ColumnTransformer (liczbowe: SimpleImputer(median)
    + StandardScaler; kategoryczne: OneHotEncoder(handle_unknown='ignore'))
    -> LogisticRegression(max_iter=1000). Pipeline ma mieć kroki o nazwach
    'prep' i 'model'."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
