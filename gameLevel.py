import gameCharacteristics as gh


class GameLevel:
    def setGameLevel(self):
        if gh.gameGraphics == 'high':
            match gh.gameLevel:
                case 1:
                    for i in range(7):
                        self.gameField.field[0][i] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall
                        self.gameField.field[0][gh.cellCountX - 1 - i] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1][gh.cellCountX - 1 - i] = \
                            self.gameField.cellTypeWall

                    for j in range(1, 6):
                        self.gameField.field[j][0] = self.gameField.cellTypeWall
                        self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1 - j][0] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1 - j][gh.cellCountX - 1] = \
                            self.gameField.cellTypeWall
                case 2:
                    for i in range(gh.cellCountX):
                        self.gameField.field[0][i] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall

                    for j in range(1, gh.cellCountY - 1, 1):
                        self.gameField.field[j][0] = self.gameField.cellTypeWall
                        self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall

                    for i in range(gh.cellCountX - 10):
                        if i > 9 and i < 17 or i > 22:
                            self.gameField.field[5][i] = self.gameField.cellTypeWall
                            self.gameField.field[gh.cellCountY - 6][i] = self.gameField.cellTypeWall

                    for j in range(gh.cellCountY - 6):
                        if j > 5 and j < 10 or j > 14 and j < 30:
                            self.gameField.field[j][10] = self.gameField.cellTypeWall
                            self.gameField.field[j][gh.cellCountX - 11] = self.gameField.cellTypeWall

                case 3:
                    for i in range(gh.cellCountX):
                        self.gameField.field[0][i] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall

                    for j in range(1, gh.cellCountY - 1, 1):
                        self.gameField.field[j][0] = self.gameField.cellTypeWall
                        self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall

                    for i in range(gh.cellCountY - 1):
                        if i == 5 or i == 6 or i == 18 or i == 19:
                            self.gameField.field[i][6] = self.gameField.cellTypeWall
                            self.gameField.field[i][7] = self.gameField.cellTypeWall
                        if i > 0 and i < 8 or i > 16:
                            self.gameField.field[i][17] = self.gameField.cellTypeWall
                            self.gameField.field[i][18] = self.gameField.cellTypeWall

                    for j in range(31, gh.cellCountX, 1):
                        self.gameField.field[8][j] = self.gameField.cellTypeWall
                        self.gameField.field[9][j] = self.gameField.cellTypeWall
                        self.gameField.field[15][j] = self.gameField.cellTypeWall
                        self.gameField.field[16][j] = self.gameField.cellTypeWall

                case 4:
                    for i in range(gh.cellCountX):
                        if i < 15 or i > 24:
                            self.gameField.field[0][i] = self.gameField.cellTypeWall
                            self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall
                        if i > 14 and i < 25:
                            self.gameField.field[7][i] = self.gameField.cellTypeWall
                        if i > 0 and i < 8 or i == 38:
                            self.gameField.field[8][i] = self.gameField.cellTypeWall
                            self.gameField.field[16][i] = self.gameField.cellTypeWall
                    for j in range(1, gh.cellCountY - 1, 1):
                        if j < 9 or j > 15:
                            self.gameField.field[j][0] = self.gameField.cellTypeWall
                            self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall
                        if j > 7 and j < 17:
                            self.gameField.field[j][8] = self.gameField.cellTypeWall
                        if j < 8 or j == 23:
                            self.gameField.field[j][14] = self.gameField.cellTypeWall
                            self.gameField.field[j][25] = self.gameField.cellTypeWall
                case 5:
                    pass