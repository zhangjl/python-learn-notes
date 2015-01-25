#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFFER = 1024
ADDR = (HOST, PORT)
socks = []

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)

try:
    while True:
        print 'waiting for connection...'
        tcpCliSocket, addr = tcpSerSocket.accept()
        socks.append(tcpCliSocket)
        print 'connected from: ' , addr
        print 'connected count: ' , len(socks)

        while True:
            for sock in socks:
                data = sock.recv(BUFFER)
                if not data:
                    socks.remove(sock)
                    continue

                if 'close' == data.strip():
                    sock.close()
                    socks.remove(sock)
                    continue

                sock.send('[%s] %s' % (ctime(), data))
except KeyboardInterrupt:
    tcpSerSocket.close()
