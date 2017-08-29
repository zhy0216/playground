import pytest
from overloader import Overloader


over = Overloader()

@over.load
def _double_me(a: int):
    return 2*a

@over.load
def _double_me(a: str):
    return a + a

@over.load
def _double_me(a: type(None)):
    return None

double_me = over


def test_overload():
    assert double_me(1) == 2
    assert double_me("1") == "11"
    assert double_me(None) is None
    with pytest.raises(ValueError):
        _double_me(1)

