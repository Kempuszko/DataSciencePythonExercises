"""Lab 12 – Projekt końcowy: checklista reprodukowalności."""
from pathlib import Path

# --- część A ---
def check_project(project_dir):
    """Sprawdź strukturę projektu i zwróć dict {nazwa_testu: bool}:

    has_readme        – istnieje README.md o długości >= 300 znaków,
    has_notebook      – istnieje co najmniej jeden plik *.ipynb,
    has_requirements  – istnieje requirements.txt lub environment.yml,
    has_data_policy   – brak plików większych niż 5 MB,
    has_results       – istnieje katalog `figures` z min. 2 plikami .png.
    """
    raise NotImplementedError('TODO: zaimplementuj tę funkcję')
