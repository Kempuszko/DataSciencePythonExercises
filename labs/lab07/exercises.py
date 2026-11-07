"""Lab 07 – SQL analityczny (działa w SQLite i DuckDB).

Funkcje zwracają TEKST zapytania SQL. W testach dostępne są tabele:
  orders(order_id, date, customer_id, product, category, quantity, amount, country)
  customers(customer_id, country, segment, signup_date)
`date` to tekst 'YYYY-MM-DD'; miesiąc wyciągniesz przez strftime('%Y-%m', date) (SQLite).
"""

# --- część A ---
def sql_monthly_revenue():
    """Kolumny: month ('YYYY-MM'), revenue (SUM(amount) zaokrąglone do 2 miejsc);
    jeden wiersz na miesiąc, rosnąco po month."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def sql_top_products(n):
    """Kolumny: product, units (SUM(quantity)), revenue (SUM(amount), 2 miejsca);
    n produktów o największym revenue, malejąco (remis: alfabetycznie po product)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def sql_running_total():
    """Kolumny: month, revenue, running_revenue – narastająca suma przychodu po miesiącach
    (funkcja okna SUM() OVER (ORDER BY month)); wartości zaokrąglone do 2 miejsc;
    rosnąco po month. Wskazówka: najpierw CTE z przychodem miesięcznym."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def sql_top3_customers_per_country():
    """Kolumny: country, customer_id, revenue (SUM(amount), 2 miejsca), rank_in_country
    (RANK() OVER (PARTITION BY country ORDER BY revenue DESC)); tylko klienci z rank <= 3;
    country to kraj KLIENTA (tabela customers); sortuj po country, rank_in_country, customer_id."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
