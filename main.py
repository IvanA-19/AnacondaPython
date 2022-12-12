import gameCharacteristics
from menu import openMainMenu, openSettingsMenu
from game import Game
import os

class Main:
    def __init__(self):
        pass

    def run(self):
        while True:

            if not gameCharacteristics.gameRestarted:
                if not gameCharacteristics.openedSettingsMenu:
                    openMainMenu()
                else:
                    openSettingsMenu()

            if gameCharacteristics.gameStarted:
                NewGame = Game()
                NewGame.gameCicle()
                gameCharacteristics.gameOver = False
                # gameCharacteristics.gameStarted = True


if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    app = Main()
    app.run()

