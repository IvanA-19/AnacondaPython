# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameSettings(object):
    def setupUi(self, GameSettings):
        GameSettings.setObjectName("GameSettings")
        GameSettings.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(GameSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 731, 101))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 160, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 220, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 270, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 330, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 390, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 440, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 500, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        GameSettings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GameSettings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        GameSettings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GameSettings)
        self.statusbar.setObjectName("statusbar")
        GameSettings.setStatusBar(self.statusbar)

        self.retranslateUi(GameSettings)
        QtCore.QMetaObject.connectSlotsByName(GameSettings)

    def retranslateUi(self, GameSettings):
        _translate = QtCore.QCoreApplication.translate
        GameSettings.setWindowTitle(_translate("GameSettings", "MainWindow"))
        self.label.setText(_translate("GameSettings", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffff00;\">Game settings</span></p></body></html>"))
        self.pushButton.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_2.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_3.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_4.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_5.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_6.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_7.setText(_translate("GameSettings", "PushButton"))
        self.pushButton_8.setText(_translate("GameSettings", "PushButton"))