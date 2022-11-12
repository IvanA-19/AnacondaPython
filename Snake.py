import gameCharacteristics
import pygame



class Snake:
    def __init__(self):
        super(Snake, self).__init__()

        self.snakeLength = 4

        self.directionRight = 0
        self.directionLeft = 1
        self.directionUp = 2
        self.directionDown = 3

        self.snakeDirection = self.directionRight

        self.snakePositionX = gameCharacteristics.cellCountX // 2
        self.snakePositionY = gameCharacteristics.cellCountY // 2

        self.snakeImage = pygame.image.load("images/snake.png")
        self.snakeHeadImage = pygame.image.load("images/head.png")

        self.rotatedHead = pygame.transform.rotate(self.snakeHeadImage, -90)

        self.headRect = self.snakeHeadImage.get_rect()
        self.snakeRect = self.snakeImage.get_rect()

        self.headRect.x = self.snakePositionX * gameCharacteristics.cellSize
        self.headRect.y = self.snakePositionY * gameCharacteristics.cellSize

        self.snakeDirectionQueue = []

    def growSnake(self):
        for j in range(gameCharacteristics.cellCountY):
            for i in range(gameCharacteristics.cellCountX):
                if self.gameField.field[j][i] > self.gameField.cellTypeNone:
                    self.gameField.field[j][i] += 1


