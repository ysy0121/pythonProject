#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import sys

HOST = '192.168.0.6'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print('client start')

while True:

    message = input('Enter Message: ')

    client_socket.send(message.encode())
    data = client_socket.recv(1024)

    print('Received', repr(data.decode()))

    if message == 'Quit':
        break

client_socket.close()
