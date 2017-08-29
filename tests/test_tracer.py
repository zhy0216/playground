import random
from method_tracer import tracer


class A:
    def __init__(self):
        self.a = 1
        self.random_int = random.randint(1, 50)

    def b(self, x):
        self.a += x
        return 2*x

    def c(self):
        self.b(self.random_int)


def test_tracer():
    im_a = A()
    with tracer(im_a.b) as r:
        im_a.c()
        assert len(r) == 1
        args, return_value = r[0]
        assert len(args) == 1
        assert args[0] == im_a.random_int
        assert return_value == 2*im_a.random_int