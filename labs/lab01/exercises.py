"""Lab 01 – Git, GitHub, środowisko i pierwszy kontakt z Copilot Chat."""
import re
from collections import Counter

# --- część A ---
def slugify(title):
    """Zamień tytuł na slug: małe litery, tylko [a-z0-9], słowa łączone '-'.

    Polskie znaki zamień na odpowiedniki ASCII (ł->l, ą->a ...).
    slugify("Cześć, Świat!  2024") == "czesc-swiat-2024"
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')

# --- część B ---
def word_freq(text, n=3):
    """Zwróć listę n najczęstszych słów jako [(słowo, liczba), ...].

    Ignoruj wielkość liter i znaki interpunkcyjne. Remisy rozstrzygaj
    alfabetycznie (rosnąco po słowie).
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
