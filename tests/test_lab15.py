import tempfile
from pathlib import Path
from loader import load

m = load("lab15")


def _make(tmp, readme_len=400, notebook=True, req=True, figs=2, big=False):
    p = Path(tmp)
    (p / "README.md").write_text("x" * readme_len, encoding="utf-8")
    if notebook:
        (p / "analysis.ipynb").write_text("{}", encoding="utf-8")
    if req:
        (p / "requirements.txt").write_text("pandas\n", encoding="utf-8")
    (p / "figures").mkdir()
    for i in range(figs):
        (p / "figures" / f"f{i}.png").write_bytes(b"\x89PNG")
    if big:
        (p / "big.bin").write_bytes(b"0" * (5 * 1024 ** 2 + 1))
    return p


def test_all_ok():
    with tempfile.TemporaryDirectory() as d:
        assert all(m.check_project(_make(d)).values())


def test_each_failure_detected():
    cases = {"has_readme": dict(readme_len=10), "has_notebook": dict(notebook=False),
             "has_requirements": dict(req=False), "has_results": dict(figs=1),
             "has_data_policy": dict(big=True)}
    for key, kw in cases.items():
        with tempfile.TemporaryDirectory() as d:
            r = m.check_project(_make(d, **kw))
            assert r[key] is False, key
            assert sum(not v for v in r.values()) == 1, key
