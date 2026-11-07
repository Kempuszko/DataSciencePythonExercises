# Sylabus: Data Science wspomagane programowanie Python

**Dla:** studenci informatyki · **Forma:** 15 × wykład (90 min) + 15 × laboratorium (90 min) · **Język:** polski, kod i dokumentacja po angielsku

## Efekty uczenia się
Po kursie student:
1. przeprowadza pełny cykl analizy danych w Pythonie (czyszczenie → EDA → model → walidacja → wnioski),
2. stosuje pandas/NumPy/scikit-learn i rozumie, co dzieje się "pod spodem" (implementacje od zera),
3. rozpoznaje i unika typowych błędów (leakage, złe metryki, p-hacking, mylące wykresy),
4. pracuje zespołowo-inżyniersko: Git, PR, testy, reprodukowalne środowisko,
5. **krytycznie używa asystenta AI**: formułuje prompty, weryfikuje i testuje wynik, deklaruje użycie.

## Plan zajęć
Patrz tabela w [README.md](README.md). Bloki: *Fundamenty i praca z AI* (1–2) · *Dane w Pythonie* (3–8) · *Wnioskowanie i ML* (9–13) · *Praktyka produkcyjna* (14–15).

## Ocenianie (propozycja – do dostosowania)
| Składnik | Waga | Jak |
|---|---|---|
| Laboratoria 1–14 | 40% | autograding (50%) + review PR: jakość, odpowiedzi, deklaracja AI (50%) |
| Kolokwium / krótka rozmowa o własnym kodzie | 15% | pytania o kod z 2 losowych labów (sprawdza zrozumienie, nie tylko wynik) |
| Projekt końcowy (Lab 15) | 35% | kryteria w wykładzie 15; prezentacja 10 min |
| Aktywność, higiena PR (opis, commity) | 10% | |

Zaliczenie: ≥ 50% łącznie i oddane ≥ 10 z 14 labów.

## Zasady użycia AI
- Dozwolone narzędzia: GitHub Copilot (VS Code), Microsoft 365 Copilot Chat; inne – po uzgodnieniu.
- Każdy PR zawiera deklarację użycia AI i opis poprawek.
- Kod z AI musi przejść testy i być przez studenta zrozumiany (kryterium na review/rozmowie).
- Lab 01–02: moduł wprowadzający (prompting, checklista przeglądu). W kolejnych labach AI jest dozwolone wg tych zasad, a notebooki zawierają punktowe zadania "Copilot".

## Harmonogram tygodniowy (szablon)
Wykład: 60 min treści + 30 min demo/dyskusji. Lab: 15 min omówienia poprzedniego PR (typowe błędy z review) + 75 min pracy. Praca domowa: dokończenie labu i PR do następnego wykładu.

## Literatura (darmowa)
- VanderPlas, *Python Data Science Handbook* (online)
- McKinney, *Python for Data Analysis* (online, 3. wyd.)
- James et al., *Introduction to Statistical Learning* (PDF)
- Downey, *Think Stats* (online)
- Dokumentacja: pandas, scikit-learn, GitHub Copilot
