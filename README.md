# Data Science wspomagane programowanie w Pythonie

Ćwiczenia do kursu dla studentów informatyki: **12 laboratoriów (każde 2 × 45 min) + 2 dodatkowe** z analizy danych i data science,
z naciskiem na dobre praktyki inżynierskie (testy, Git, SQL, reprodukowalność) i **odpowiedzialną pracę z asystentem AI**.

**Narzędzia: darmowe dla studenta.** Otwarte: Python, JupyterLab, pandas, NumPy, scikit-learn, SQLite, DuckDB, pytest, Git, Miniforge/conda-forge.
Asystent AI: **Microsoft 365 Copilot Chat** z kontem uczelnianym (w przeglądarce lub w Teams; darmowy w ramach licencji uczelni, ale nie open source).
Kod hostujemy na GitHubie (darmowym dla repozytoriów publicznych).

## Zanim zaczniesz: konto GitHub

- Nie masz konta? → [`docs/01_zakladanie_konta_github.pdf`](docs/01_zakladanie_konta_github.pdf)
- Masz konto, chcesz przygotować fork, Git i środowisko → [`docs/02_przygotowanie_konta_i_srodowiska.pdf`](docs/02_przygotowanie_konta_i_srodowiska.pdf)

## Szybki start

```bash
# 1. Zrób fork tego repo na GitHubie (przycisk "Fork"), potem:
git clone https://github.com/<TWÓJ_LOGIN>/DataSciencePythonExercises.git
cd DataSciencePythonExercises

# 2. Środowisko (jednorazowo) – Miniforge (conda-forge), albo venv + pip install -r requirements.txt
conda env create -f environment.yml
conda activate ds-exercises

# 3. Pracuj
git checkout -b lab01-<TWÓJ_LOGIN>
mkdir -p submissions/<TWÓJ_LOGIN> && cp -r labs/lab01 submissions/<TWÓJ_LOGIN>/lab01
jupyter lab submissions/<TWÓJ_LOGIN>/lab01/lab.ipynb
```

Oddawanie prac przez Pull Request – opis w [CONTRIBUTING.md](CONTRIBUTING.md).

## Zawartość

Każdy lab ma **część A (~45 min, wymagana – zalicza lab)** i **część B (~45 min, rozszerzenie)**.

| Lab | Temat | Narzędzia |
|---|---|---|
| 01 | Git/GitHub, środowisko, Copilot Chat | Git, Copilot Chat |
| 02 | Python dla DS, testy, weryfikacja kodu od AI | pytest |
| 03 | NumPy i pandas I | NumPy, pandas |
| 04 | pandas II: merge, pivot, czas, RFM (mały ETL) | pandas |
| 05 | Czyszczenie danych i jakość danych | pandas |
| 06 | Bazy danych: generowanie danych, schemat, import | SQLite |
| 07 | SQL analityczny (funkcje okna) i DuckDB | SQLite, DuckDB |
| 08 | Wizualizacja, EDA, wnioskowanie (bootstrap, test permutacyjny) | matplotlib |
| 09 | ML: regresja, klasyfikacja, metryki, walidacja | NumPy, scikit-learn |
| 10 | Potoki ML i wyciek danych | scikit-learn |
| 11 | Generatywna AI w praktyce: wyszukiwanie, RAG, ocena odpowiedzi | NumPy, Copilot Chat |
| 12 | Projekt końcowy | wszystko powyżej |
| 13 | *Dodatkowy:* drzewa, ensemble, interpretacja | NumPy |
| 14 | *Dodatkowy:* wydajność i pamięć | pandas |

Sylabus, ocenianie i zasady: [SYLLABUS.md](SYLLABUS.md).

## Struktura repo

```
labs/labNN/   lab.ipynb (instrukcja) + exercises.py (szablon funkcji do uzupełnienia)
tests/        testy autogradingu (pytest): test_a_* = część A, test_b_* = część B
data/         zbiory danych (syntetyczne, w repo)
docs/         instrukcje PDF (konto GitHub, przygotowanie środowiska)
submissions/  tu trafiają Twoje prace: submissions/<login>/labNN/
scripts/      make_data.py (generator danych), grade.py (autograder)
```

## Dane
Wszystkie zbiory są **syntetyczne** (generowane deterministycznie przez `scripts/make_data.py`), więc nie ma problemów z licencją ani prywatnością.
