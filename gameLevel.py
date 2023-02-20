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
                    for i in range(gh.cellCountX):
                        if i < 17 or i > 22:
                            self.gameField.field[0][i] = self.gameField.cellTypeWall
                            self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall
                        if i > 4 and i < 16 or i > 23 and i < 35:
                            self.gameField.field[5][i] = self.gameField.cellTypeWall
                            self.gameField.field[19][i] = self.gameField.cellTypeWall
                        if i == 6 or i == 33:
                            self.gameField.field[4][i] = self.gameField.cellTypeWall
                            self.gameField.field[6][i] = self.gameField.cellTypeWall
                            self.gameField.field[18][i] = self.gameField.cellTypeWall
                            self.gameField.field[20][i] = self.gameField.cellTypeWall
                        if i == 9 or i == 11 or i == 28 or i == 30:
                            self.gameField.field[12][i] = self.gameField.cellTypeWall

                    for j in range(gh.cellCountY - 1):
                        if j < 10 or j > 14:
                            self.gameField.field[j][0] = self.gameField.cellTypeWall
                            self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall
                            self.gameField.field[j][5] = self.gameField.cellTypeWall
                            self.gameField.field[j][34] = self.gameField.cellTypeWall
                        if j > 4 and j < 10 or j < 20 and j > 14:
                            self.gameField.field[j][16] = self.gameField.cellTypeWall
                            self.gameField.field[j][23] = self.gameField.cellTypeWall
                        if j > 10 and j < 14:
                            self.gameField.field[j][10] = self.gameField.cellTypeWall
                            self.gameField.field[j][29] = self.gameField.cellTypeWall
                case 6:
                    for i in range(gh.cellCountX):
                        self.gameField.field[0][i] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall
                        if i > 3 and i < 18 or i > 21 and i < 36:
                            self.gameField.field[3][i] = self.gameField.cellTypeWall
                            self.gameField.field[21][i] = self.gameField.cellTypeWall

                        if i > 6 and i < 34:
                            self.gameField.field[6][i] = self.gameField.cellTypeWall
                            self.gameField.field[18][i] = self.gameField.cellTypeWall
                        if i > 9 and i < 18 or i > 21 and i < 30:
                            self.gameField.field[9][i] = self.gameField.cellTypeWall
                            self.gameField.field[15][i] = self.gameField.cellTypeWall

                    for j in range (1, gh.cellCountY - 1, 1):
                        if j < 11 or j > 13:
                            self.gameField.field[j][0] = self.gameField.cellTypeWall
                            self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall
                        if j > 2 and j < 22:
                            self.gameField.field[j][3] = self.gameField.cellTypeWall
                            self.gameField.field[j][36] = self.gameField.cellTypeWall
                        if j > 8 and j < 16:
                            self.gameField.field[j][9] = self.gameField.cellTypeWall
                            self.gameField.field[j][30] = self.gameField.cellTypeWall
                        if j > 5 and j < 11 or j > 13 and j < 19:
                            self.gameField.field[j][6] = self.gameField.cellTypeWall
                            self.gameField.field[j][33] = self.gameField.cellTypeWall
                case 7:
                    for i in range(gh.cellCountX):
                        self.gameField.field[0][i] = self.gameField.cellTypeWall
                        self.gameField.field[gh.cellCountY - 1][i] = self.gameField.cellTypeWall
                        if i > 3 and i < 16:
                            self.gameField.field[9][i] = self.gameField.cellTypeWall
                            self.gameField.field[15][i] = self.gameField.cellTypeWall
                        if i > 5 and i < 14:
                            self.gameField.field[6][i] = self.gameField.cellTypeWall
                            self.gameField.field[18][i] = self.gameField.cellTypeWall
                        if i > 3 and i < 13:
                            self.gameField.field[3][i] = self.gameField.cellTypeWall
                            self.gameField.field[21][i] = self.gameField.cellTypeWall
                        if i > 16 and i < 37:
                            self.gameField.field[9][i] = self.gameField.cellTypeWall
                            self.gameField.field[15][i] = self.gameField.cellTypeWall
                        if i > 18 and i < 37:
                            self.gameField.field[3][i] = self.gameField.cellTypeWall
                            self.gameField.field[21][i] = self.gameField.cellTypeWall
                        if i > 19 and i < 34:
                            self.gameField.field[6][i] = self.gameField.cellTypeWall
                            self.gameField.field[18][i] = self.gameField.cellTypeWall
                    for j in range(1, gh.cellCountY - 1, 1):
                        if j < 11 or j > 13:
                            self.gameField.field[j][0] = self.gameField.cellTypeWall
                            self.gameField.field[j][gh.cellCountX - 1] = self.gameField.cellTypeWall
                        if j > 13 and j < 22 or j > 2 and j < 11:
                            self.gameField.field[j][3] = self.gameField.cellTypeWall
                        if j > 13 or j < 11:
                            self.gameField.field[j][16] = self.gameField.cellTypeWall
                        if j > 18 and j < 22 or j > 2 and j < 7:
                            self.gameField.field[j][13] = self.gameField.cellTypeWall
                        if j > 2 and j < 7 or j > 17 and j < 22:
                            self.gameField.field[j][19] = self.gameField.cellTypeWall
                        if j > 2 and j < 11 or j > 13 and j < 21:
                            self.gameField.field[j][36] = self.gameField.cellTypeWall