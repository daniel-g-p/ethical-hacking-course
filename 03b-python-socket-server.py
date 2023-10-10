#!/bin/python3

import socket

HOST = "127.0.0.1"
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with s:
    s.bind((HOST, PORT))
    s.listen(1)
    connection, address = s.accept()
    with connection:
        print(f'Connection from "{address}"')
