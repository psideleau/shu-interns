import pytest

@pytest.mark.parametrize("x, y,expected", [
    pytest.param(1, 3, 4),
    pytest.param(2, 2, 4),
])
def test_adding(x, y, expected):
    assert expected == x + y
