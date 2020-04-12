# -*- coding: utf-8 -*-
import os
import sys
import socket

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import uic
from _thread import *
from MainClientSocket import ClientSocket

CWD = str(os.getcwd())
# print(CWD)

# formMain = uic.loadUiType("ui/ChatWindow.ui")[0]


class ChatWindow(QDialog):

    Client = None
    CLIENT_SOCKET = None

    def __init__(self, parent):
        super(ChatWindow, self).__init__(parent)
        self.PRT = parent
        ui = 'ui/ChatDialog.ui'
        uic.loadUi(ui, self)
        self.buttonUi()
        self.show()

    def textWrite(self, text):
        self.chat_textedit.append(text)

    def clientStart(self):
        HOST = self.txt_ip.text()
        PORT = self.txt_port.text()

        try:
            self.CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.CLIENT_SOCKET.connect((HOST, int(PORT)))
            self.textWrite('========= client start-' + HOST + ':' + PORT)

            self.Client = ClientSocket(self)
            self.Client.start()
        except:
            pass

    def clientStop(self):
        self.CLIENT_SOCKET.close()

    def sendMessage(self):
        if( self.CLIENT_SOCKET == None ):
            self.clientStart()

        MSG = self.chat_txt.text()
        try:
            self.CLIENT_SOCKET.send(MSG.encode())
        except:
            pass

        self.chat_txt.setText('')

    def buttonUi(self):
        self.btn_client_start.clicked.connect(self.clientStart)
        self.btn_client_stop.clicked.connect(self.clientStop)
        self.chat_btn.clicked.connect(self.sendMessage)
        self.chat_txt.returnPressed.connect(self.sendMessage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = ChatWindow()
    mainwindow.show()
    sys.exit(app.exec_())