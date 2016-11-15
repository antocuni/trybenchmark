import time
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

def test_cpu():
    import psutil
    for i in range(10):
        print 'CPU:', psutil.cpu_percent(0.1, percpu=True)

def test_cgroup():
    import os
    os.system('cat /proc/%d/cgroup' % os.getpid())
