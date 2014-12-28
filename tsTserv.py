import socket
from time import ctime
import os

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while 1:
    print 'waiting for connection'
    tcpCliSock, addr = tcpSerSock.accept()
    print '... connected from ', addr

    while 1:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        timestamp = ctime()
        os_info = os.name
        os_current_dir = os.curdir
        os_dir = os.listdir(os_current_dir)
        
        tcpCliSock.sendall('{}, {}: {}\n{}'.format(timestamp, os_info, os_dir, data))
        print data

    tcpCliSock.close()
tcpSerSock.close()

