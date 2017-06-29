# https://docs.python.org/3/library/collections.html#collections.ChainMap
from UserDict import DictMixin


class ChainMap(DictMixin):
    def __init__(self, *maps):
        self._maps = maps

    def __getitem__(self, key):
        for mapping in self._maps:
            if key in mapping:
                return mapping[key]
        raise KeyError(key)
