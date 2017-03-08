import collections

_ = lambda: _

class DefaultDict(collections.defaultdict):
    def __init__(self, default_factor=None, *arg, **kwargs):
        collections.defaultdict.__init__(self, _, *arg, **kwargs)
        self.default_factor = default_factor

    def __missing__(self, key):

        if callable(self.default_factor):
            value = self.default_factor(key)
        else:
            value = self.default_factor
        self[key] = value
        return value

