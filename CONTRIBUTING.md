# Jak oddawać ćwiczenia (workflow PR)

## Zasady
1. Pracujesz na **własnym forku**; PR otwierasz do `main` repozytorium prowadzącego.
2. Jeden PR = jedno laboratorium. Nazwa gałęzi: `labNN-<login>`.
3. Zmieniasz pliki **wyłącznie** w `submissions/<twój_login>/` (autograder odrzuci PR z innymi zmianami).
4. Folder `submissions/<login>/labNN/` zawiera: `exercises.py` oraz `lab.ipynb` (z odpowiedziami na pytania).
5. **Deklarujesz użycie AI** w opisie PR (jest checklista w szablonie).

## Krok po kroku
```bash
git checkout -b lab03-<login>
mkdir -p submissions/<login> && cp -r labs/lab03 submissions/<login>/lab03
# ... pracujesz w submissions/<login>/lab03/ ...

# testy lokalnie (macOS/Linux):
SUBMISSION_DIR=submissions/<login> pytest tests/test_lab03.py -v
# Windows PowerShell:
$env:SUBMISSION_DIR="submissions/<login>"; pytest tests/test_lab03.py -v

git add submissions/<login>/lab03
git commit -m "Lab 03: NumPy"
git push -u origin lab03-<login>
# GitHub → "Compare & pull request" → wypełnij szablon
```

## Co się dzieje po otwarciu PR
1. GitHub Actions (`autograde`) uruchamia testy dla zmienionych labów i pokazuje tabelę wyników w zakładce *Checks*.
   *(Pierwszy PR z forka może wymagać zatwierdzenia przez prowadzącego – to normalne.)*
2. Prowadzący robi **review jakościowe** (czytelność kodu, odpowiedzi na pytania, użycie AI) – komentarze w PR.
3. Poprawki: dopisujesz kolejne commity do tej samej gałęzi – PR aktualizuje się sam.

## Autograding – co oznacza zielony ✅
Funkcje zwracają poprawne wyniki na testowych przypadkach. **Nie oznacza** to pełnej oceny: oceniamy też zrozumienie
(odpowiedzi, review, możliwa krótka rozmowa o Twoim kodzie).

## Uczciwość akademicka
Testy są jawne, więc łatwo je "obejść". Nie rób tego: kod, którego nie rozumiesz, wyjdzie na review.
Wolno dyskutować podejścia ze współstudentami; kod piszesz sam/a. AI wolno używać według zasad z Lab 01–02.
