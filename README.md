# Data Science wspomagane programowanie w Pythonie

Materiały do kursu dla studentów informatyki: **15 laboratoriów** z analizy danych i data science,
z naciskiem na dobre praktyki inżynierskie (testy, Git, reprodukowalność) i **odpowiedzialną pracę z asystentem AI** (Copilot).

## Zanim zaczniesz: konto GitHub

- Nie masz konta? → [`docs/01_zakladanie_konta_github.pdf`](docs/01_zakladanie_konta_github.pdf)
- Masz konto, chcesz przygotować fork, Git i środowisko → [`docs/02_przygotowanie_konta_i_srodowiska.pdf`](docs/02_przygotowanie_konta_i_srodowiska.pdf)

## Szybki start

```bash
# 1. Zrób fork tego repo na GitHubie (przycisk "Fork"), potem:
git clone https://github.com/<TWÓJ_LOGIN>/DataSciencePythonExercises.git
cd DataSciencePythonExercises

# 2. Środowisko (jednorazowo)
conda env create -f environment.yml
conda activate ds-exercises

# 3. Pracuj
git checkout -b lab01-<TWÓJ_LOGIN>
mkdir -p submissions/<TWÓJ_LOGIN> && cp -r labs/lab01 submissions/<TWÓJ_LOGIN>/lab01
jupyter lab submissions/<TWÓJ_LOGIN>/lab01/lab.ipynb
```

Bez condy: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.

Oddawanie prac przez Pull Request – opis w [CONTRIBUTING.md](CONTRIBUTING.md).

## Zawartość

| Tydzień | Temat | Lab (`labs/`) |
|---|---|---|
| 1 | Wprowadzenie, narzędzia, **zasady pracy z AI** | Git/GitHub, Copilot: prompting |
| 2 | Python dla DS, **weryfikacja kodu od AI** | moving_average, flatten, parsowanie logów |
| 3 | NumPy | wektoryzacja, broadcasting |
| 4 | Pandas I | wczytywanie, selekcja, agregacje |
| 5 | Pandas II | merge, pivot, czas, RFM |
| 6 | Czyszczenie danych | brudne dane sprzedażowe |
| 7 | Wizualizacja | matplotlib, uczciwe wykresy |
| 8 | EDA | mini-projekt: odejścia klientów |
| 9 | Statystyka | bootstrap, testy, rozmiar efektu |
| 10 | ML: podstawy | OLS, k-NN, train/test od zera |
| 11 | Klasyfikacja i metryki | precision/recall, AUC, CV |
| 12 | Pipeline'y i data leakage | wykrywanie przecieków, Pipeline |
| 13 | Drzewa, ensemble, interpretacja | Gini, podział, permutation importance |
| 14 | Wydajność i pamięć | dtypes, chunking, DuckDB |
| 15 | Projekt końcowy, etyka | projekt + prezentacja |

Pełny sylabus, ocenianie i zasady: [SYLLABUS.md](SYLLABUS.md).

## Struktura repo

```
labs/labNN/   lab.ipynb (instrukcja) + exercises.py (szablon funkcji do uzupełnienia)
tests/        testy autogradingu (pytest)
data/         zbiory danych (syntetyczne, w repo)
submissions/  tu trafiają Twoje prace: submissions/<login>/labNN/
scripts/      make_data.py (generator danych), grade.py (autograder)
```

## Dane
Wszystkie zbiory są **syntetyczne** (generowane deterministycznie przez `scripts/make_data.py`), więc nie ma problemów z licencją ani prywatnością.
