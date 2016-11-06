import pytest
import socket
import random
import subprocess
from cStringIO import StringIO

@pytest.mark.usefixtures('initargs')
class TestBuffered(object):

    # apparently, the slowdown of makefile is not completely linear. E.g. by
    # using 20 MB I got a 20x slowdown compared to BufferedSocket, on PyPy.
    # Anyway, 1 MB should be enough to show that BufferedSocket is much faster
    SIZE = 1 * (1024*1024) # MB
    PORT = 5000

    @pytest.fixture
    def initargs(self, request, tmpdir):
        self.tmpdir = tmpdir
        # create the file to serve
        mystream = tmpdir.join('mystream')
        with mystream.open('wb') as f:
            buf = StringIO()
            for i in xrange(self.SIZE):
                ch = chr(random.randrange(255))
                f.write(ch)
        #
        # start tcpserver
        cmd = ['tcpserver', '127.0.0.1', str(self.PORT),
               'cat', str(mystream)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #
        # stop tcpserver
        def finalize():
            try:
                print 'killing...'
                p.kill()
                print 'done'
            except OSError, e:
                print 'OSError', e
                pass
            if p.returncode is None:
                print 'communicate'
                stdout, stderr = p.communicate()
                print p.returncode
                print stdout
                print stderr
                print 'done'
        request.addfinalizer(finalize)

    def do_benchmark(self, benchmark, open_connection):
        def count_bytes():
            f = open_connection()
            tot = 0
            while True:
                s = f.read(1)
                if s == '':
                    break
                tot += len(s)
            return tot

        res = benchmark(count_bytes)
        assert res == self.SIZE

    @pytest.mark.benchmark(group="buffered")
    def test_makefile(self, benchmark):
        def open_connection():
            sock = socket.create_connection(('127.0.0.1', self.PORT))
            return sock.makefile()
        self.do_benchmark(benchmark, open_connection)

    @pytest.mark.benchmark(group="buffered")
    def test_makefile_2(self, benchmark):
        def open_connection():
            sock = socket.create_connection(('127.0.0.1', self.PORT))
            return sock.makefile()
        self.do_benchmark(benchmark, open_connection)

    @pytest.mark.benchmark(group="buffered")
    def test_makefile_3(self, benchmark):
        def open_connection():
            sock = socket.create_connection(('127.0.0.1', self.PORT))
            return sock.makefile()
        self.do_benchmark(benchmark, open_connection)
