import socket

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host = raw_input('enter host: ')
# port = raw_input('enter port:' )
# if host and port:
#     ADDR = (host, int(port))
tcpCliSock.connect(ADDR)
    
while 1:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()