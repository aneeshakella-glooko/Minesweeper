class Tile(object):
    def __init__(self, destruct = False):
        self.visible = False
        self.destruct = destruct
        self.bombs = 0

    def set_bombs(self, bombs):
        self.bombs = bombs

    def get_bombs(self):
        return self.bombs