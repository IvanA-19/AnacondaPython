import pygame
import gameCharacteristics
from Snake import Snake
from apple import Apple


class Field():
    def __init__(self):

        self.apple = Apple()
        self.cellTypeNone = 0
        self.cellTypeApple = -1
        self.cellTypeWall = -2

        self.field = [[self.cellTypeNone for _ in range(gameCharacteristics.cellCountX)] for _ in range(gameCharacteristics.cellCountY)]

        self.cellImage = pygame.image.load("images/none.png")
        self.wallImage = pygame.image.load("images/wall.png")

        self.noneRect = self.cellImage.get_rect()
        self.wallRect = self.wallImage.get_rect()

        self.snake = Snake()



