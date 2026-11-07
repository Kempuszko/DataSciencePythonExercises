"""Lab 11 – Generatywna AI w praktyce: wyszukiwanie fragmentów (TF-IDF), prompt RAG i ocena odpowiedzi modelu."""
import re
import numpy as np

# --- część A ---
def chunk_text(text, size=200, overlap=50):
    """Podziel tekst na fragmenty po `size` znaków z nakładaniem `overlap` znaków.

    Fragmenty zaczynają się w pozycjach 0, size-overlap, 2*(size-overlap), ...
    Kończysz, gdy fragment sięga końca tekstu (ostatni może być krótszy, bez
    dodatkowego fragmentu zawartego w całości w poprzednim). Pusty tekst -> [].
    overlap >= size -> ValueError.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def tfidf_search(query, docs, k=3):
    """Zwróć listę indeksów k dokumentów najbardziej podobnych do zapytania.

    Ręcznie w NumPy (bez scikit-learn): tokeny = re.findall(r"\\w+", tekst.lower());
    słownik z `docs` (tokeny zapytania spoza słownika ignoruj); tf = liczba wystąpień;
    idf = log((1 + N) / (1 + df)) + 1; wektor = tf * idf, znormalizowany L2;
    podobieństwo = iloczyn skalarny. Remisy: mniejszy indeks dokumentu.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def build_rag_prompt(question, passages):
    """Zbuduj prompt RAG jako tekst (do wklejenia do Copilot Chat):

      Odpowiedz wyłącznie na podstawie poniższych fragmentów. Jeśli odpowiedzi w nich nie ma, napisz "Nie wiem".

      [1] <fragment 1>
      [2] <fragment 2>
      ...

      Pytanie: <pytanie>
      Odpowiedź:

    (fragmenty numerowane od 1, każdy w osobnej linii; tekst kończy się słowem "Odpowiedź:")
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def extract_code_block(text):
    """Zwróć kod z PIERWSZEGO bloku kodu Pythona w odpowiedzi modelu (markdown).

    Blok zaczyna się linią ``` lub ```python (lub ```py, wielkość liter bez znaczenia)
    i kończy linią ```. Bloki w innych językach (np. ```bash) pomijaj. Zwróć treść
    bloku bez znaczników i bez końcowych znaków nowej linii; brak bloku -> None.
    Uwaga: zamykający ``` bloku w innym języku nie jest początkiem nowego bloku!
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def grounded_fraction(answer, passages):
    """Prosta miara „oparcia w źródłach”: odsetek słów odpowiedzi (tokeny
    re.findall(r"\\w+", ...) po zamianie na małe litery, tylko słowa o długości >= 4,
    liczone jako różne słowa) występujących w którymkolwiek z fragmentów.
    Brak słów o długości >= 4 w odpowiedzi -> 0.0.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
