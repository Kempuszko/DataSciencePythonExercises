"""Minimalny runner bez pytest (do szybkiej weryfikacji): python tests/run_plain.py lab01 [lab02 ...]"""
import importlib, sys, traceback
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
ok = bad = 0
for lab in sys.argv[1:]:
    m = importlib.import_module(f"test_{lab}")
    for name in sorted(dir(m)):
        if name.startswith("test_"):
            try:
                getattr(m, name)(); ok += 1
            except Exception:
                bad += 1; print(f"FAIL {lab}.{name}"); traceback.print_exc(limit=3)
print(f"passed={ok} failed={bad}")
sys.exit(1 if bad else 0)
