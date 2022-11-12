import gameCharacteristics
from menu import openMainMenu



obj = []
if __name__ == "__main__":
    from game import Game
    while True:

        if not gameCharacteristics.gameRestarted:
            openMainMenu()

        if gameCharacteristics.gameStarted:
            NewGame = Game()
            NewGame.gameCicle()
            gameCharacteristics.gameOver = False
            #gameCharacteristics.gameStarted = True


