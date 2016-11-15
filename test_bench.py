import os
import commands
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
    p = psutil.Process()
    print
    print 'cpu affinity:', p.cpu_affinity()
    for i in range(10):
        mycpu = commands.getoutput('ps -o psr= -p %d' % os.getpid())
        mycpu = int(mycpu)
        usage = psutil.cpu_percent(0.1, percpu=True)
        print 'CPU', mycpu, usage[mycpu:mycpu+1]

def test_cgroup():
    import py
    d = py.path.local('/sys/fs/cgroup/')
    for f in d.visit():
        if f.check(file=False):
            continue
        try:
            s = f.read().strip()
        except py.error.Error, e:
            s = str(e)
        if '\n' in s:
            s = s.splitlines()[0] + '...'
        print f, s
