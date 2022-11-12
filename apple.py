import pygame
import gameCharacteristics
from random import choice


class Apple():
    def __init__(self):
        pygame.mixer.init()
        self.appleImsge = pygame.image.load("images/apple.png")
        self.appleRect = self.appleImsge.get_rect()
        self.appleSound = pygame.mixer.Sound("sounds/apple_2.wav")


    def addApple(self):
        while True:
            j = choice(range(len(self.gameField.field)))
            i = choice(range(len(self.gameField.field[j])))
            if self.gameField.field[j][i] == self.gameField.cellTypeNone:
                self.gameField.field[j][i] = self.gameField.cellTypeApple
                break






