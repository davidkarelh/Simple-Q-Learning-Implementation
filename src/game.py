class Game:
    __board = [-100, -1, 0, -1, -1, -1, -1, -1, -1, 100]
    playerIndex = 2

    def __init__(self) -> None:
        pass

    def moveLeft(self):
        if (self.playerIndex == 0):
            return False
        else:
            self.playerIndex -= 1
            self.__board[self.playerIndex] = 0
            self.__board[self.playerIndex + 1] = -1
        
    def moveRight(self):
        if (self.playerIndex == 8):
            return False
        else:
            self.playerIndex += 1
            self.__board[self.playerIndex] = 0
            self.__board[self.playerIndex - 1] = -1