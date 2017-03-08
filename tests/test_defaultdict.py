from defaultdict import DefaultDict

EMPTY = object()

def test_empty_default():
    d = DefaultDict()
    assert d[EMPTY] == None
    assert len(d) == 1

def test_non_function_default():
    d = DefaultDict(89)
    assert d[EMPTY] == 89
    assert len(d) == 1

def test_function_default():
    d = DefaultDict(lambda x: 0)
    assert d[EMPTY] == 0
    assert len(d) == 1

def test_function_default_with_key_parameter():
    d = DefaultDict(lambda x: x+1)
    assert d[41] == 42
    assert len(d) == 1

def test_check_donot_add_value():
    d = DefaultDict()
    assert EMPTY not in d
    assert len(d) == 0





