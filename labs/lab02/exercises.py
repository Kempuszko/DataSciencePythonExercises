"""Lab 02 – Python dla Data Science i weryfikacja kodu od AI."""

# --- część A ---
def moving_average(xs, k):
    """Średnia krocząca z oknem k. Zwraca listę długości len(xs)-k+1.

    Gdy k > len(xs) lub k < 1 -> ValueError.
    moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def flatten(nested):
    """Spłaszcz dowolnie zagnieżdżone listy/krotki do płaskiej listy.

    Łańcuchy znaków traktuj jako wartości atomowe.
    flatten([1, [2, (3, "ab")], []]) == [1, 2, 3, "ab"]
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def parse_log_line(line):
    """Sparsuj linię logu 'YYYY-MM-DD HH:MM:SS LEVEL [modul] wiadomość'.

    Zwróć dict z kluczami: date, time, level, module, message.
    Gdy format niepoprawny -> zwróć None.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

def group_by_key(rows, key):
    """Zgrupuj listę słowników po wartości klucza `key`.

    Zwróć dict {wartość: [wiersze...]} z zachowaniem kolejności wejścia.
    Wiersze bez klucza pomiń.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
