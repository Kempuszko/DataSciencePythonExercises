"""Autograder PR-ów. Uruchamiany w GitHub Actions (patrz .github/workflows/autograde.yml).

Zasady:
  * PR może zmieniać pliki WYŁĄCZNIE w submissions/<login>/ (login == autor PR, bez rozróżniania wielkości liter),
  * dla każdego zmienionego labNN uruchamiane są testy tests/test_labNN.py na kodzie studenta,
  * wynik (tabela) trafia na stdout i do $GITHUB_STEP_SUMMARY; kod wyjścia != 0 gdy coś nie przeszło.

Lokalnie:
  python scripts/grade.py --author jan-kowalski --files submissions/jan-kowalski/lab01/exercises.py
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def changed_files(base):
    out = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return [l for l in out.splitlines() if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--author", required=True)
    ap.add_argument("--files", nargs="*", help="zamiast git diff (do testów lokalnych)")
    a = ap.parse_args()

    files = a.files if a.files is not None else changed_files(a.base)
    problems, labs = [], set()
    for f in files:
        if not re.match(rf"submissions/{re.escape(a.author)}/", f, re.I):
            problems.append(f"Plik poza submissions/{a.author}/: {f}")
            continue
        m = re.match(r"submissions/([^/]+)/(lab\d\d)/", f, re.I)
        if m:
            labs.add((m.group(1), m.group(2)))
    if not files:
        problems.append("PR nie zmienia żadnych plików.")
    if not labs and not problems:
        print("Brak zmian w folderach labNN – nic do oceny (np. tylko project/).")

    rows = []
    for login, lab in sorted(labs, key=lambda t: t[1]):
        if not (ROOT / "tests" / f"test_{lab}.py").exists():
            rows.append((f"{lab}", "pominięty", "brak testów dla tego labu")); continue
        env = dict(os.environ, SUBMISSION_DIR=str(ROOT / "submissions" / login))
        for part, label in (("a", "część A (wymagana)"), ("b", "część B (rozszerzenie)")):
            p = subprocess.run([sys.executable, "-m", "pytest", f"tests/test_{lab}.py", "-q", "--tb=short",
                                "-k", f"test_{part}_"], cwd=ROOT, env=env, capture_output=True, text=True)
            if p.returncode == 5:      # brak testów w tej części
                continue
            tail = [l for l in p.stdout.strip().splitlines() if l.strip()][-1:] or [""]
            if p.returncode == 0:
                status = "✅ zaliczona"
            elif part == "a":
                status = "❌ błędy"
            else:
                status = "⚠️ niezaliczona (nieobowiązkowa)"
            rows.append((f"{lab} – {label}", status, tail[0]))
            if p.returncode != 0:
                print(p.stdout[-3000:])

    project = ROOT / "submissions" / a.author / "project"
    if project.is_dir() and any(f.startswith(f"submissions/{a.author}/project") for f in files):
        sys.path.insert(0, str(ROOT / "tests"))
        from loader import load  # noqa: E402
        os.environ["SUBMISSION_DIR"] = str(ROOT / "submissions" / a.author)
        try:
            res = load("lab12").check_project(project)
            ok = all(res.values())
            rows.append(("project", "✅ struktura OK" if ok else "❌ braki",
                         ", ".join(k for k, v in res.items() if not v) or "komplet"))
        except Exception as e:  # lab12/exercises.py jeszcze nie gotowy
            rows.append(("project", "❌ błąd", repr(e)[:120]))

    md = ["### Wynik autogradingu", "", "| Element | Status | Szczegóły |", "|---|---|---|"]
    md += [f"| {l} | {s} | {d} |" for l, s, d in rows]
    md += [""] + [f"- ⚠️ {p}" for p in problems]
    md += ["", "_Autograder sprawdza poprawność funkcji. Jakość kodu i refleksje oceniane są na review._"]
    text = "\n".join(md)
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        Path(os.environ["GITHUB_STEP_SUMMARY"]).write_text(text, encoding="utf-8")
    failed = problems or any("❌" in st for _, st, _ in rows)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
