#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import sys
from _thread import *
from PyQt5 import QtCore


class ClientSocket(QtCore.QThread):

    PRT = None

    def __init__(self, parent=None):
        super(ClientSocket, self).__init__(parent)
        self.PRT = parent

    def run(self):
        self.recvStart()

    def textWrite(self, text):
        self.PRT.textWrite(text)

    def recvStart(self):

        while True:
            try:
                data = self.PRT.CLIENT_SOCKET.recv(1024)

                self.textWrite('Received '+ repr(data.decode()))

                if data == 'Quit':
                    break
            except ConnectionResetError as e:
                self.textWrite('Disconnected by ConnectionResetError')
                break
            except ConnectionAbortedError as e:
                self.textWrite('Disconnected by ConnectionAbortedError')
                break

        self.PRT.CLIENT_SOCKET.close()
        self.textWrite('######### client disconnected')