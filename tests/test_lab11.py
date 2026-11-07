import numpy as np
from loader import load

m = load("lab11")

DOCS = [
    "Python to język programowania używany w analizie danych.",
    "Pandas udostępnia DataFrame do pracy z danymi tabelarycznymi.",
    "Kot siedzi na dywanie i pije mleko.",
    "SQLite to lekka baza danych zapisana w jednym pliku.",
]


def test_a_chunk_text_basic():
    t = "abcdefghij" * 5  # 50 znaków
    ch = m.chunk_text(t, size=20, overlap=5)
    assert ch[0] == t[:20] and ch[1] == t[15:35] and ch[2] == t[30:50]
    assert len(ch) == 3


def test_a_chunk_text_edge_cases():
    assert m.chunk_text("") == []
    assert m.chunk_text("abc", size=10, overlap=2) == ["abc"]
    assert m.chunk_text("a" * 20, size=20, overlap=5) == ["a" * 20]   # bez zbędnego ogona
    try:
        m.chunk_text("abc", size=5, overlap=5)
        raise AssertionError("brak ValueError")
    except ValueError:
        pass


def test_a_tfidf_search_finds_relevant():
    assert m.tfidf_search("baza danych w pliku", DOCS, k=1) == [3]
    assert m.tfidf_search("DataFrame pandas", DOCS, k=1) == [1]
    assert m.tfidf_search("kot mleko", DOCS, k=1) == [2]


def test_a_tfidf_search_k_and_ties():
    r = m.tfidf_search("python", DOCS, k=3)
    assert len(r) == 3 and r[0] == 0
    assert m.tfidf_search("zzzz", DOCS, k=2) == [0, 1]   # brak trafień -> kolejność indeksów


def test_b_build_rag_prompt():
    p = m.build_rag_prompt("Czym jest SQLite?", ["Pierwszy fragment.", "Drugi fragment."])
    assert "[1] Pierwszy fragment." in p and "[2] Drugi fragment." in p
    assert p.index("[1]") < p.index("[2]") < p.index("Czym jest SQLite?")
    assert "Nie wiem" in p and p.rstrip().endswith("Odpowiedź:") and "Pytanie: Czym jest SQLite?" in p


def test_b_extract_code_block_basic():
    t = "Oto kod:\n```python\ndef f(x):\n    return x + 1\n```\nGotowe."
    assert m.extract_code_block(t) == "def f(x):\n    return x + 1"


def test_b_extract_code_block_variants():
    assert m.extract_code_block("```\nprint(1)\n```") == "print(1)"
    assert m.extract_code_block("```PY\nx = 2\n```") == "x = 2"
    assert m.extract_code_block("brak kodu") is None
    assert m.extract_code_block("```python\nniezamknięty") is None


def test_b_extract_code_block_skips_other_languages():
    t = "```bash\npip install pandas\n```\nTekst pomiędzy.\n```python\nimport pandas\n```"
    assert m.extract_code_block(t) == "import pandas"
    assert m.extract_code_block("```javascript\nlet a = 1;\n```\nTylko tekst.") is None


def test_b_grounded_fraction():
    ps = ["SQLite to lekka baza danych zapisana w jednym pliku."]
    assert abs(m.grounded_fraction("Baza SQLite jest zapisana w jednym pliku", ps) - 5 / 6) < 1e-9
    assert m.grounded_fraction("Warszawa stolica Polski", ps) == 0.0
    assert m.grounded_fraction("to w i", ps) == 0.0   # same krótkie słowa
    assert m.grounded_fraction("lekka baza", ps) == 1.0
