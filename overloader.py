from functools import partial
from types import FunctionType
from typing import Dict
from inspect import signature, _empty
from itertools import zip_longest, starmap

# https://github.com/python/cpython/blob/3.6/Lib/typing.py#L1610


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
        return partial(_raise, "you need to use overloader")

    def __call__(self, *args):
        for arg_types, func in self.env.items():
            if all(starmap(isinstance, zip(args, arg_types))):
                return func(*args)





