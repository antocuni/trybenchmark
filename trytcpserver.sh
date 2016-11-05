tcpserver 127.0.0.1 5000 echo ciao &
nc 127.0.0.1 5000
kill %1
