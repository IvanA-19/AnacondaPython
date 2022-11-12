import pygame
from random import choice
import sys
import time
import gameCharacteristics
from field import Field
from Snake import Snake
from apple import Apple


class Game(Apple, Snake):
    def __init__(self):
        self.icon = pygame.image.load("icon.png")

        super(Game, self).__init__()

        pygame.init()

        self.mainWindow = pygame.display.set_mode((gameCharacteristics.windowWidth, gameCharacteristics.windowHeigth))
        pygame.display.set_caption("Snake")
        pygame.display.set_icon(self.icon)
        self.setGameSettings()

        self.gameOverSound = pygame.mixer.Sound("sounds/game_over.wav")

        self.gameField = Field()
        self.snake = Snake()


        self.rotatedHead = pygame.transform.rotate(self.snake.snakeHeadImage, -90)

        self.snakeDirectionLast = self.snake.snakeDirection

    def setGameSettings(self):
        self.mainWindow.fill(gameCharacteristics.windowColor)


    def clearField(self):
        for i in range(gameCharacteristics.cellCountX):
            for j in range(gameCharacteristics.cellCountY):
                self.gameField.field[j][i] = self.gameField.cellTypeNone
        match gameCharacteristics.gameLevel:
            case 1:
                for i in range(7):
                    self.gameField.field[0][i] = self.gameField.cellTypeWall
                    self.gameField.field[gameCharacteristics.cellCountY - 1][i] = self.gameField.cellTypeWall
                    self.gameField.field[0][gameCharacteristics.cellCountX - 1 - i] = self.gameField.cellTypeWall
                    self.gameField.field[gameCharacteristics.cellCountY - 1][gameCharacteristics.cellCountX - 1 - i] = \
                        self.gameField.cellTypeWall

                for j in range(1, 6):
                    self.gameField.field[j][0] = self.gameField.cellTypeWall
                    self.gameField.field[j][gameCharacteristics.cellCountX - 1] = self.gameField.cellTypeWall
                    self.gameField.field[gameCharacteristics.cellCountY - 1 - j][0] = self.gameField.cellTypeWall
                    self.gameField.field[gameCharacteristics.cellCountY - 1 - j][gameCharacteristics.cellCountX - 1] = \
                        self.gameField.cellTypeWall

        for i in range(self.snake.snakeLength):
            self.gameField.field[self.snake.snakePositionY][self.snake.snakePositionX - i] = self.snake.snakeLength - i

        self.addApple()

    def drawGame(self, mainWindow):
        for i in range(gameCharacteristics.cellCountX):
            for j in range(gameCharacteristics.cellCountY):

                match self.gameField.field[j][i]:
                    case self.gameField.cellTypeNone:
                        self.gameField.noneRect.x = i * gameCharacteristics.cellSize
                        self.gameField.noneRect.y = j * gameCharacteristics.cellSize
                        mainWindow.blit(self.gameField.cellImage, self.gameField.noneRect)
                    case self.gameField.cellTypeWall:
                        self.gameField.wallRect.x = i * gameCharacteristics.cellSize
                        self.gameField.wallRect.y = j * gameCharacteristics.cellSize
                        mainWindow.blit(self.gameField.wallImage, self.gameField.wallRect)
                    case self.gameField.cellTypeApple:
                        self.appleRect.x = i * gameCharacteristics.cellSize
                        self.appleRect.y = j * gameCharacteristics.cellSize
                        mainWindow.blit(self.appleImsge, self.appleRect)
                    case _ :
                        if self.gameField.field[j][i] == self.snake.snakeLength:
                            self.snake.headRect.x = i * gameCharacteristics.cellSize
                            self.snake.headRect.y = j * gameCharacteristics.cellSize
                            mainWindow.blit(self.rotatedHead, self.snake.headRect)
                        else:
                            self.snake.headRect.x = i * gameCharacteristics.cellSize
                            self.snake.headRect.y = j * gameCharacteristics.cellSize
                            mainWindow.blit(self.snake.snakeImage, self.snake.headRect)

    def makeMove(self):
        match self.snake.snakeDirection:
            case self.snake.directionDown:
                self.snake.snakePositionY += 1
                self.rotatedHead = pygame.transform.rotate(self.snake.snakeHeadImage, 180)
                for j in range(gameCharacteristics.cellCountY):
                    for i in range(gameCharacteristics.cellCountX):
                        if (self.gameField.field[j][i] > self.gameField.cellTypeNone):
                                self.gameField.field[j][i] -= 1

                if (self.snake.snakePositionY > gameCharacteristics.cellCountY - 1):
                    self.snake.snakePositionY = 0

            case self.snake.directionUp:
                self.snake.snakePositionY -= 1
                self.rotatedHead = pygame.transform.rotate(self.snake.snakeHeadImage, 0)
                for j in range(gameCharacteristics.cellCountY):
                    for i in range(gameCharacteristics.cellCountX):
                        if(self.gameField.field[j][i] > self.gameField.cellTypeNone):
                            self.gameField.field[j][i] -= 1

                if (self.snake.snakePositionY < 0):
                    self.snake.snakePositionY = gameCharacteristics.cellCountY - 1

            case self.snake.directionLeft:
                self.snake.snakePositionX -= 1
                self.rotatedHead = pygame.transform.rotate(self.snake.snakeHeadImage, -270)
                for j in range(gameCharacteristics.cellCountY):
                    for i in range(gameCharacteristics.cellCountX):
                        if (self.gameField.field[j][i] > self.gameField.cellTypeNone):
                            self.gameField.field[j][i] -= 1

                if (self.snake.snakePositionX < 0):
                    self.snake.snakePositionX = gameCharacteristics.cellCountX - 1

            case self.snake.directionRight:
                self.rotatedHead = pygame.transform.rotate(self.snake.snakeHeadImage, -90)
                self.snake.snakePositionX += 1
                for j in range(gameCharacteristics.cellCountY):
                    for i in range(gameCharacteristics.cellCountX):
                        if (self.gameField.field[j][i] > self.gameField.cellTypeNone):
                            self.gameField.field[j][i] -= 1
                if (self.snake.snakePositionX > gameCharacteristics.cellCountX - 1):
                    self.snake.snakePositionX = 0

        if self.gameField.field[self.snake.snakePositionY][self.snake.snakePositionX] != self.gameField.cellTypeNone:
            match self.gameField.field[self.snake.snakePositionY][self.snake.snakePositionX]:
                case self.gameField.cellTypeApple:
                    self.snake.snakeLength += 1
                    self.appleSound.play()
                    gameCharacteristics.score += 1
                    self.growSnake()
                    self.addApple()
                case self.gameField.cellTypeWall:
                    self.gameOverSound.play()
                    time.sleep(1)
                    gameCharacteristics.gameOver = True
                case _:
                    self.gameOverSound.play()
                    time.sleep(1)
                    gameCharacteristics.gameOver = True
        self.gameField.field[self.snake.snakePositionY][self.snake.snakePositionX] = self.snake.snakeLength

    def gameControl(self, event):
        match event.key:
            case pygame.K_UP:
                if self.snakeDirectionLast != self.snake.directionDown and self.snakeDirectionLast != self.snake.directionUp:
                    if len(self.snake.snakeDirectionQueue) < 2:
                        self.snake.snakeDirectionQueue.insert(0, self.snake.directionUp)
            case pygame.K_DOWN:
                if self.snakeDirectionLast != self.snake.directionDown and self.snakeDirectionLast != self.snake.directionUp:
                    if len(self.snake.snakeDirectionQueue) < 2:
                        self.snake.snakeDirectionQueue.insert(0, self.snake.directionDown)
            case pygame.K_LEFT:
                if self.snakeDirectionLast != self.snake.directionLeft and self.snakeDirectionLast != self.snake.directionRight:
                    if len(self.snake.snakeDirectionQueue) < 2:
                        self.snake.snakeDirectionQueue.insert(0, self.snake.directionLeft)
            case pygame.K_RIGHT:
                if self.snakeDirectionLast != self.snake.directionLeft and self.snakeDirectionLast != self.snake.directionRight:
                    if len(self.snake.snakeDirectionQueue) < 2:
                        self.snake.snakeDirectionQueue.insert(0, self.snake.directionRight)
            case pygame.K_SPACE:
                gameCharacteristics.gamePaused = True
            case pygame.K_ESCAPE:
                sys.exit()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.gameControl(event)
                if not self.snake.snakeDirectionQueue:
                    self.snakeDirectionLast = self.snake.snakeDirection
                else:
                    self.snakeDirectionLast = self.snake.snakeDirectionQueue[0]



    def gameCicle(self):
        self.clearField()

        while True:
            self.checkEvents()
            if self.snake.snakeDirectionQueue:
                self.snake.snakeDirection = self.snake.snakeDirectionQueue[len(self.snake.snakeDirectionQueue) - 1]
                self.snake.snakeDirectionQueue.pop()
            if not gameCharacteristics.gamePaused:
                self.makeMove()
            else:
                from menu import openPauseMenu
                openPauseMenu()

            self.mainWindow.fill(tuple(gameCharacteristics.windowColor))


            if gameCharacteristics.gameOver:
                gameCharacteristics.newGame = False
                from menu import openGameOverMenu
                openGameOverMenu()
                pygame.quit()
                break

            elif gameCharacteristics.exitGame:
                gameCharacteristics.newGame = False
                gameCharacteristics.exitGame = False
                gameCharacteristics.gamePaused = False
                pygame.quit()
                break

            self.drawGame(self.mainWindow)

            pygame.display.flip()
            time.sleep(0.08)






