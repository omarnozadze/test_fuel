from fuel import convert, gauge


def test_valid_fraction():
    assert convert("2/4") ==50
    assert convert("1/4") == 25


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(99) == "F"


