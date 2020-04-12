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
from SystemUtil import WindowOS
from DBmysql import Mysql

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
        self.osUtil = WindowOS()
        self.mntView()
        self.tableView()

    """
    def connectWindow(self):
        Dig = DialogWindow(self)
        self.btn_connect.setEnabled(False)
        Dig.exec_()
        self.chatWrite('connect active...')
        self.btn_connect.setEnabled(True)
    """

    def chatOpen(self):
        #cw = ChatWindow(self)
        #cw.exec_()
        ChatWindow(self)

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

    def mntView(self):
        str1 = self.osUtil.os_uname()
        str2 = self.osUtil.os_system() + ' ' + self.osUtil.os_release()
        str3 = self.osUtil.os_platform()
        str4 = str(self.osUtil.os_cpucount()) + '개'
        self.mnt_label1.setText(str1)
        self.mnt_label2.setText(str2)
        self.mnt_label3.setText(str3)
        self.mnt_label4.setText(str4)

    def timerTimeout(self):
        self.lcd_cpu.display( self.osUtil.os_cpupercent() )
        self.lcd_ram.display(self.osUtil.os_vmemory())
        self.lcd_disk.display(self.osUtil.os_disk())
        self.lcd_network.display(self.osUtil.os_network())

    def timerStart(self):
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timerTimeout)
        self.timer.start()
        self.mnt_btn_start.setEnabled(False)
        self.mnt_btn_stop.setEnabled(True)

    def timerStop(self):
        self.timer.stop()
        self.mnt_btn_start.setEnabled(True)
        self.mnt_btn_stop.setEnabled(False)

    def tableView(self):
        mysql = Mysql();
        arr = mysql.select()
        txt = '\n'.join(arr)
        self.db_label.setText(txt)

    def buttonUi(self):
        # self.btn_connect.clicked.connect(self.connectWindow)
        self.btn_connect.clicked.connect(self.connectConsole)
        self.btn_stop.clicked.connect(self.connectStop)
        self.chat_btn.clicked.connect(self.chatWindow)
        self.chat_btn_open.clicked.connect(self.chatOpen)
        self.chat_txt.returnPressed.connect(self.chatWindow)

        self.mnt_btn_start.clicked.connect(self.timerStart)
        self.mnt_btn_stop.clicked.connect(self.timerStop)

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
