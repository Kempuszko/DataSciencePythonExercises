"""Lab 06 – Bazy danych: generowanie danych, schemat i import do SQLite."""
import sqlite3
import numpy as np
import pandas as pd

# --- część A ---
def generate_orders(n, seed=0):
    """Wygeneruj syntetyczny zbiór zamówień jako DataFrame (n wierszy, deterministyczny dla seed).

    Użyj rng = np.random.default_rng(seed). Kolumny (w tej kolejności):
      order_id    – 1..n,
      date        – tekst 'YYYY-MM-DD', losowa data z roku 2024,
      customer_id – losowa liczba całkowita 1..50,
      product     – jeden z: laptop, phone, desk, chair, pen,
      quantity    – losowa liczba całkowita 1..5,
      amount      – kwota > 0 zaokrąglona do 2 miejsc
                    (cena bazowa produktu * quantity * losowy szum około 1.0).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def create_schema(conn):
    """Utwórz w otwartym połączeniu SQLite schemat:

      customers(customer_id INTEGER PRIMARY KEY, country TEXT NOT NULL,
                segment TEXT NOT NULL, signup_date TEXT)
      orders(order_id INTEGER PRIMARY KEY, date TEXT NOT NULL,
             customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
             product TEXT NOT NULL, quantity INTEGER NOT NULL CHECK (quantity > 0),
             amount REAL NOT NULL CHECK (amount > 0))

    Dodatkowo: indeks `idx_orders_customer` na orders(customer_id) oraz
    włączone klucze obce w tym połączeniu (PRAGMA foreign_keys = ON).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def load_into_db(conn, customers, orders):
    """Załaduj DataFrame'y do istniejących tabel (schemat już utworzony – dopisuj
    wiersze, nie zastępuj tabel). Zwróć krotkę (liczba_klientów, liczba_zamówień)
    wczytanych wierszy."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def revenue_by_country_sql(conn):
    """Zapytanie SQL (JOIN orders i customers): DataFrame z kolumnami
    country, revenue (SUM(amount) zaokrąglone do 2 miejsc), n_orders (COUNT),
    posortowany malejąco po revenue."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def top_customers_sql(conn, n=5):
    """DataFrame z kolumnami customer_id, revenue (SUM(amount), 2 miejsca): n klientów
    o największym przychodzie, malejąco. Parametr n przekaż jako parametr zapytania (?)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
