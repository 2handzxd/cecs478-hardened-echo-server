def test_empty_string():
    assert "" == ""

def test_large_input():
    data = "a" * 1000
    assert len(data) == 1000