#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import sys
from _thread import *
from PyQt5 import QtCore


class ServerSocket(QtCore.QThread):

    SERVER_IP = ''
    SERVER_PORT = ''
    PRT = None
    SERVER_SOCKET = None
    SERVER_FLAG = True
    SOCKETS = []

    def __init__(self, parent=None):
        super(ServerSocket, self).__init__(parent)
        self.PRT = parent

    def run(self):
        self.serverStart()

    def setServerInfo(self,IP,PORT):
        self.SERVER_IP = IP         # self.PRT.txt_ip.text()
        self.SERVER_PORT = PORT     # self.PRT.txt_port.text()
        self.textWrite(self.SERVER_IP + ":" + self.SERVER_PORT)

    def textWrite(self, text):
        # self.textedit.appendPlainText(text)
        self.PRT.chatWrite(text)
        print(text)

    def conn_thread(self, client_socket, addr):
        self.textWrite('Connected by : ' + str(addr[0]) + ', ' + str(addr[1]))

        while self.SERVER_FLAG:
            try:
                data = client_socket.recv(1024)
                self.textWrite('Received from ' + str(addr[0]) + ', ' + str(addr[1]) + ', ' + data.decode())
                print(self.SOCKETS)
                for csocket in self.SOCKETS:
                    csocket.send(data)

                if data == '' or data == 'QuitAll':
                    self.SERVER_FLAG = False
                    self.textWrite('Disconnected by ' + str(addr[0]) + ', ' + str(addr[1]))
                    break

            except ConnectionResetError as e:
                self.textWrite('Disconnected by ' + str(addr[0]) + ', ' + str(addr[1]))
                self.SERVER_FLAG = False
                break

        client_socket.close()
        self.textWrite('######### Client Disconnected')

    def serverStart(self):
        # self.setServerInfo()
        self.textWrite('######### server info-' + self.SERVER_IP + ':' + self.SERVER_PORT)

        self.SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.SERVER_SOCKET.bind((self.SERVER_IP, int(self.SERVER_PORT)))
        self.SERVER_SOCKET.listen()

        self.textWrite('######### server start...')

        while self.SERVER_FLAG:
            self.textWrite('######### client waiting...')
            client_socket, addr = self.SERVER_SOCKET.accept()
            self.SOCKETS.append(client_socket)
            start_new_thread(self.conn_thread, (client_socket, addr))

        self.SERVER_SOCKET.close()
        self.textWrite('######### server stop...')

    def serverStop(self):
        self.SERVER_FLAG = False
        self.textWrite('######### stopping...')
