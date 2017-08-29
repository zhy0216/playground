from functools import partial
from types import FunctionType
from inspect import signature
from itertools import starmap


def _raise(msg: str, error=ValueError):
    raise error(msg)


class Overloader:
    def __init__(self):
        self.env = {}

    def load(self, func: FunctionType):
        # TODO: cannot deal with any and generic type
        # read https://github.com/python/mypy, see if can solve this
        # print(f"dispatcher: {func.__name__}")
        sig = signature(func)
        self.env[tuple(para.annotation for para in sig.parameters.values())] = func
        return lambda *arg: _raise("you need to use overloader")

    def __call__(self, *args):
        for arg_types, func in self.env.items():
            if all(starmap(isinstance, zip(args, arg_types))):
                return func(*args)


