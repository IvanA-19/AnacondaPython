from PyQt5 import QtGui, QtWidgets
app = QtWidgets.QApplication([])
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()
from pygame import mixer


mixer.init()
enterSound = mixer.Sound("sounds/enter.wav")

cellSize = 32

cellCountX = 40
cellCountY = 25

windowWidth = cellCountX * cellSize
windowHeigth = cellCountY * cellSize

windowColor = [152, 251, 152]

gameLevel = 4

graphics = ['low', 'high']
gameGraphics = graphics[1]

gameStarted = False
gamePaused = False

exitGame = False

newGame = False

gameRestarted = False

score = 0

gameOver = False

openedSettingsMenu = False