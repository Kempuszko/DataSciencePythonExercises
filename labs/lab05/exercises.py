"""Lab 05 – Pandas II: groupby, merge, pivot, szeregi czasowe."""
import pandas as pd

def revenue_pivot(df):
    """Tabela przestawna: wiersze = category, kolumny = country, wartości = suma amount.

    Brakujące kombinacje wypełnij 0.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def add_customer_info(orders, customers):
    """LEFT JOIN zamówień z klientami po customer_id; dodaj kolumnę `segment`.

    Zachowaj wszystkie wiersze `orders` i ich kolejność. Nie duplikuj kolumny
    `country` (zostaw tę z `orders`).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def monthly_growth(df):
    """Zmiana procentowa (0.1 = +10%) przychodu miesiąc do miesiąca.

    Zwróć Series z indeksem 'YYYY-MM'; pierwszy miesiąc pomiń (brak poprzedniego).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def customer_rfm(df, today):
    """RFM per klient. Zwróć DataFrame z indeksem customer_id i kolumnami:

    recency   – dni od ostatniego zamówienia do `today` (datetime/str),
    frequency – liczba zamówień,
    monetary  – suma amount.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
