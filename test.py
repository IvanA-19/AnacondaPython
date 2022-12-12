from PyQt5 import QtWidgets, QtGui, QtCore
from settings import Ui_GameSettings
import sys


class GameSettingsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GameSettingsWindow, self).__init__()

        self.ui = Ui_GameSettings()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.setStyleSheet("background-color: black;")

        self.ui.label.setGeometry(50, 10, 700, 100)

        self.ui.pushButton.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_5.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_6.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_7.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_8.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")

        self.ui.pushButton.setGeometry(105, 130, 590, 70)
        self.ui.pushButton_2.setGeometry(105, 210, 590, 70)
        self.ui.pushButton_3.setGeometry(105, 290, 590, 70)
        self.ui.pushButton_4.setGeometry(105, 370, 590, 70)
        self.ui.pushButton_5.setGeometry(105, 450, 590, 70)
        self.ui.pushButton_6.setGeometry(105, 530, 590, 70)
        self.ui.pushButton_7.setGeometry(105, 610, 590, 70)
        self.ui.pushButton_8.setGeometry(105, 690, 590, 70)

        self.ui.pushButton.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_2.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_3.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_4.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_5.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_6.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_7.setFont(QtGui.QFont("BigOldBoldy", 20))
        self.ui.pushButton_8.setFont(QtGui.QFont("BigOldBoldy", 20))

        self.ui.pushButton.setText("Graphics")
        self.ui.pushButton_2.setText("Type of control")
        self.ui.pushButton_3.setText("Anaconda skin")
        self.ui.pushButton_4.setText("Walls")
        self.ui.pushButton_5.setText("Field color")
        self.ui.pushButton_6.setText("Difficulty level")
        self.ui.pushButton_7.setText("Volume")
        self.ui.pushButton_8.setText("Back to main menu")

        self.ui.pushButton_8.clicked.connect(self.close)


def openSettingsMenu():
    app = QtWidgets.QApplication([])
    application = GameSettingsWindow()
    application.setFixedSize(800, 800)
    application.show()

    sys.exit(app.exec())