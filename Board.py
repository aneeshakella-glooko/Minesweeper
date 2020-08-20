import random

from Tile import Tile


class Board(object):
    def __init__(self):
        self.width = 30
        self.height = 30;
        self.board = []
        for i in range(0, self.height):
            tmp = []
            for j in range(0, self.width):
                number = random.randint(0, 100)
                if number >= 95:
                    tmp.append(Tile(True))
                else:
                    tmp.append(Tile())
            self.board.append(tmp)

    def get(self, y, x):
        return self.board[int(y)][int(x)]

    def calculate_bombs(self, y, x):
        bombs = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (y == 0 and x == 0) or not self.isValid(y + i, x + j):
                    continue
                elif self.board[y + i][x + j].destruct:
                    bombs += 1
        self.board[y][x].set_bombs(bombs)

    def isValid(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width

    def destruct(self, y, x):
        self.board[y][x].visible = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (y == 0 and x == 0) or not self.isValid(y + i, x + j):
                    continue
                elif self.board[y + i][x + j].destruct and not self.board[y + i][x + j].visible:
                    self.destruct(y + i, x + j)
                else:
                    self.board[y + i][x + j].visible = True




