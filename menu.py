import gameCharacteristics
from PyQt5 import QtWidgets, QtGui, QtCore
from label import Ui_window
from pause import Ui_Game_pause
import sys
from time import sleep
from game import Game
from game_over import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.ui.label.setFont(QtGui.QFont("Times", 15))

        self.setStyleSheet("background-color: black;")

        self.ui.label.adjustSize()
        self.ui.label.setGeometry(165, 30, 470, 90)
        self.ui.pushButton.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")
        self.ui.pushButton_3.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")
        self.ui.pushButton_4.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")

        self.ui.pushButton.setText("Start new game")
        self.ui.pushButton.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton.setGeometry(150, 170, 500, 90)

        self.ui.pushButton_2.setText("Level")
        self.ui.pushButton_2.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton_2.setGeometry(150, 280, 500, 90)

        self.ui.pushButton_3.setText("Settings")
        self.ui.pushButton_3.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton_3.setGeometry(150, 390, 500, 90)

        self.ui.pushButton_4.setText("Quit")
        self.ui.pushButton_4.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton_4.setGeometry(150, 500, 500, 90)

        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_4.clicked.connect(self.btn4Clicked)

    def btn4Clicked(self):
        sys.exit(0)


    def btnClicked(self):
        gameCharacteristics.score = 0
        #gameCharacteristics.exitGame = False
        gameCharacteristics.gameStarted = True
        gameCharacteristics.gameOver = False
        gameCharacteristics.newGame = True
        self.close()


class Pause(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pause, self).__init__()
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.ui = Ui_Game_pause()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.ui.label.setGeometry(250, 5, 300, 100)

        self.ui.label_2.setText(f"Score: {gameCharacteristics.score}")
        self.ui.label_2.setGeometry(300, 110, 400, 50)

        self.ui.label_2.setStyleSheet("color: rgb(0, 255, 0)")
        self.ui.label_2.setFont(QtGui.QFont('BigOldBoldy-dEjR', 30))


        self.setWindowTitle("Pause")

        self.ui.pushButton_2.setGeometry(150, 220, 500, 90)
        self.ui.pushButton.setGeometry(150, 330, 500, 90)

        self.ui.pushButton.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255); color: rgb(0, 0, 0);")
        self.ui.pushButton_2.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))

        self.ui.pushButton.clicked.connect(self._button_1_clicked)
        self.ui.pushButton_2.clicked.connect(self._button_2_clicked)

    def _button_1_clicked(self):
        gameCharacteristics.exitGame = True
        gameCharacteristics.gameRestarted = False
        self.close()

    def _button_2_clicked(self):
        gameCharacteristics.gamePaused = False
        self.close()





class GameOver(QtWidgets.QMainWindow):
    def __init__(self):
        super(GameOver, self).__init__()

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Game over")

        self.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.ui.pushButton.setStyleSheet("background-color: rgb(10, 255, 60); color: rgb(0, 0, 0);")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(10, 255, 60); color: rgb(0, 0, 0);")

        self.ui.pushButton.setText("Restart")
        self.ui.pushButton_2.setText("Back to main menu")

        self.ui.pushButton.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton_2.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))

        self.ui.pushButton.setGeometry(100, 140, 500, 90)
        self.ui.pushButton_2.setGeometry(100, 250, 500, 90)

        self.ui.label.setGeometry(115, 10, 470, 90)

        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btn2Clicked)

    def btnClicked(self):
        gameCharacteristics.gameRestarted = True
        gameCharacteristics.score = 0
        gameCharacteristics.gameStarted = True
        self.close()

    def btn2Clicked(self):
        gameCharacteristics.gameRestarted = False
        self.close()


app = QtWidgets.QApplication([])

def openMainMenu():
    gameCharacteristics.gameStarted = False
    application = mywindow()
    application.setFixedSize(800, 640)
    application.show()

    app.exec()


def openPauseMenu():
    application = Pause()
    application.setFixedSize(800, 500)
    application.show()

    app.exec()

def openGameOverMenu():
    application = GameOver()
    application.setFixedSize(700, 400)
    application.show()

    app.exec()