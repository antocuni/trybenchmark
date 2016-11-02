from test import pystone

def test_pystone(benchmark):
    benchmark(pystone.main)


def test_sum(benchmark):
    def fn():
        x = 0
        for i in range(1200000):
            x += i
        return i
    benchmark(fn)
