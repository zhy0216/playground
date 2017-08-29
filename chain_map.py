# https://docs.python.org/3/library/collections.html#collections.ChainMap
from collections import UserDict


class ChainMap(UserDict):
    def __init__(self, *maps):
        self._maps = maps

    def __getitem__(self, key):
        for mapping in self._maps:
            if key in mapping:
                return mapping[key]
        raise KeyError(key)

    def __contains__(self, key):
        return any(key in m for m in self._maps)

