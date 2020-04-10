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
from MainServerSocket import ServerSocket
from ChatWindow import ChatWindow

CWD = str(os.getcwd())
# print(CWD)

formMain = uic.loadUiType("ui/MainWindow.ui")[0]


class MainWindow(QMainWindow, formMain):

    SERVER = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonUi()
        self.initUI()

    # 미사용
    def connectWindow(self):
        Dig = DialogWindow(self)
        self.btn_connect.setEnabled(False)
        Dig.exec_()
        self.chatWrite('connect active...')
        self.btn_connect.setEnabled(True)

    def chatOpen(self):
        cw = ChatWindow(self)
        cw.exec_()

    def connectConsole(self):
        IP = self.txt_ip.text()
        PORT = self.txt_port.text()
        self.SERVER = ServerSocket(self)
        self.SERVER.setServerInfo(IP, PORT)
        self.SERVER.start()

    def connectStop(self):
        self.SERVER.serverStop()

    def chatWrite(self, text):
        self.chat_textedit.append(text)

    def chatWindow(self):
        self.chatWrite(self.chat_txt.text())
        self.chat_txt.setText('')

    def buttonUi(self):
        # self.btn_connect.clicked.connect(self.connectWindow)
        self.btn_connect.clicked.connect(self.connectConsole)
        self.btn_stop.clicked.connect(self.connectStop)
        self.chat_btn.clicked.connect(self.chatWindow)
        self.chat_btn_open.clicked.connect(self.chatOpen)
        self.chat_txt.returnPressed.connect(self.chatWindow)

    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setWindowTitle('Main System from Python')
        self.setWindowIcon(QIcon(CWD + '/image/web.png'))
        # self.setGeometry(300, 300, 300, 200)
        # self.move(300, 300)
        # self.resize(800, 600)
        self.moveCenter()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
