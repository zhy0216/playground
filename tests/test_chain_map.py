from chain_map import ChainMap


def test_chain_map():
    local_env = {"a": 1, "b": 2}
    global_env = {"a": 3, "c": 4}

    chain_map = ChainMap(local_env, global_env)

    assert 'a' in chain_map
    assert 'c' in chain_map
    assert chain_map['a'] == 1
    assert chain_map['b'] == 2
    assert chain_map['c'] == 4
