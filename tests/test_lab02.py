from loader import load

m = load("lab02")


def _raises(exc, f, *a):
    try:
        f(*a)
    except exc:
        return True
    return False


def test_moving_average():
    assert m.moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    assert m.moving_average([5], 1) == [5.0]


def test_moving_average_errors():
    assert _raises(ValueError, m.moving_average, [1, 2], 3)
    assert _raises(ValueError, m.moving_average, [1, 2], 0)


def test_flatten():
    assert m.flatten([1, [2, (3, "ab")], []]) == [1, 2, 3, "ab"]
    assert m.flatten([]) == []
    assert m.flatten([[[[1]]]]) == [1]


def test_parse_log_line():
    r = m.parse_log_line("2024-05-01 12:30:00 ERROR [db] connection lost: timeout")
    assert r == {"date": "2024-05-01", "time": "12:30:00", "level": "ERROR",
                 "module": "db", "message": "connection lost: timeout"}


def test_parse_log_line_invalid():
    assert m.parse_log_line("garbage") is None
    assert m.parse_log_line("2024-05-01 12:30:00 ERROR db no brackets") is None


def test_group_by_key_order_and_missing():
    rows = [{"k": "a", "v": 1}, {"v": 2}, {"k": "b", "v": 3}, {"k": "a", "v": 4}]
    g = m.group_by_key(rows, "k")
    assert list(g) == ["a", "b"]
    assert [r["v"] for r in g["a"]] == [1, 4]
