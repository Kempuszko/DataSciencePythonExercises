"""Lab 07 – Wizualizacja (matplotlib). Funkcje zwracają obiekt Axes."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_monthly_revenue(series):
    """Wykres liniowy przychodu miesięcznego (indeks = miesiące, wartości = przychód).

    Wymagania: tytuł, opisy osi x i y (niepuste), dokładnie jedna linia
    z len(series) punktami, etykiety osi x obrócone o 45 stopni.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def plot_hist(values, bins=20):
    """Histogram z liczbą słupków == bins, tytułem i opisami osi (niepuste)."""
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def plot_bar_by_category(series, top=5):
    """Wykres słupkowy `top` największych kategorii (indeks = kategoria), malejąco.

    Wymagania: tytuł, opisy osi, liczba słupków == min(top, len(series)),
    pierwszy słupek jest największy.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def plot_scatter_with_trend(x, y):
    """Scatter + prosta trendu (OLS, np.polyfit stopnia 1).

    Wymagania: tytuł, opisy osi, jedna kolekcja punktów (scatter) o len(x)
    punktach oraz dokładnie jedna linia (trend).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
