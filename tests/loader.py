"""Ładowanie rozwiązania studenta. Nie edytuj.

Lokalnie (bez zmiennej środowiskowej) testy działają na szablonach z labs/.
Autograder ustawia SUBMISSION_DIR=submissions/<login>.
"""
import importlib.util
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(lab):
    base = os.environ.get("SUBMISSION_DIR")
    path = (Path(base) / lab if base else ROOT / "labs" / lab) / "exercises.py"
    if not path.exists():
        raise FileNotFoundError(f"Brak pliku {path}")
    spec = importlib.util.spec_from_file_location(f"{lab}_exercises", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
