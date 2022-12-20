#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
import sysconfig
from PyQt5 import QtCore, QtGui, QtWidgets
from mhyt import yt_download

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 364)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_logo = QtWidgets.QLabel(self.centralwidget)
        self.img_logo.setGeometry(QtCore.QRect(120, 0, 161, 151))
        self.img_logo.setStyleSheet("image: url(:/youtube/youtube.png);")
        self.img_logo.setText("")
        self.img_logo.setObjectName("img_logo")
        self.lab_Download = QtWidgets.QLabel(self.centralwidget)
        self.lab_Download.setGeometry(QtCore.QRect(270, 40, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lab_Download.setFont(font)
        self.lab_Download.setObjectName("lab_Download")
        self.lab_link = QtWidgets.QLabel(self.centralwidget)
        self.lab_link.setGeometry(QtCore.QRect(10, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lab_link.setFont(font)
        self.lab_link.setObjectName("lab_link")
        self.lab_n_arquivo = QtWidgets.QLabel(self.centralwidget)
        self.lab_n_arquivo.setGeometry(QtCore.QRect(10, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lab_n_arquivo.setFont(font)
        self.lab_n_arquivo.setObjectName("lab_n_arquivo")
        self.le_link = QtWidgets.QLineEdit(self.centralwidget)
        self.le_link.setGeometry(QtCore.QRect(80, 141, 491, 31))
        self.le_link.setObjectName("le_link")
        self.le_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.le_titulo.setGeometry(QtCore.QRect(230, 191, 341, 31))
        self.le_titulo.setObjectName("le_titulo")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(250, 270, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(216, 37, 50);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_download.setObjectName("btn_download")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 240, 73, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_mp3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_mp3.setFont(font)
        self.rb_mp3.setChecked(True)
        self.rb_mp3.setObjectName("rb_mp3")
        self.verticalLayout.addWidget(self.rb_mp3)
        self.rb_mp4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_mp4.setFont(font)
        self.rb_mp4.setObjectName("rb_mp4")
        self.verticalLayout.addWidget(self.rb_mp4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        ### Botao Download
        self.btn_download.clicked.connect(self.download)

    def download(self):
        if self.rb_mp4.isChecked() == True:
            url = self.le_link.text()
            titulo = self.le_titulo.text()
            titulo_mp3 = titulo +'.mp4'
            yt_download(url, titulo_mp3)
            
        elif self.rb_mp3.isChecked() == True:
            try:
                url = self.le_link.text()
                titulo = self.le_titulo.text()
                titulo_mp3 = titulo +'.mp3'
                yt_download(url, titulo_mp3, ismusic = True, codec = 'mp3')
            except:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_Download.setText(_translate("MainWindow", "Download"))
        self.lab_link.setText(_translate("MainWindow", "Link: "))
        self.lab_n_arquivo.setText(_translate("MainWindow", "Nome do Arquivo:"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.rb_mp3.setText(_translate("MainWindow", "Mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "Mp4"))
#Imagem
import youtube

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# In[ ]:




