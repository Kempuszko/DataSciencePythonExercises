from loader import load

m = load("lab01")


def test_slugify_basic():
    assert m.slugify("Hello, World!") == "hello-world"


def test_slugify_polish_and_spaces():
    assert m.slugify("Cześć, Świat!  2024") == "czesc-swiat-2024"
    assert m.slugify("  --Łódź--  ") == "lodz"


def test_slugify_empty():
    assert m.slugify("!!!") == ""


def test_word_freq_top():
    text = "to be or not to be, that is the question. To be!"
    assert m.word_freq(text, 2) == [("be", 3), ("to", 3)]


def test_word_freq_ties_alphabetical_and_n():
    assert m.word_freq("b a c a b", 3) == [("a", 2), ("b", 2), ("c", 1)]
    assert m.word_freq("", 3) == []
