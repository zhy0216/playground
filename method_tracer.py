import contextlib
from types import MethodType
from typing import Tuple, List, Any

@contextlib.contextmanager
def tracer(method: MethodType) -> List[Tuple[List, Any]]:
    instance = method.__self__
    method_name = method.__name__
    trace_data = []

    def wrap_method(*args):
        r = method(*args)
        trace_data.append((args, r))
        return r

    original_method = method
    setattr(instance, method_name, wrap_method)
    yield trace_data
    setattr(instance, method_name, original_method)

