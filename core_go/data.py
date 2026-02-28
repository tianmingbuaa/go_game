import numpy as np
from enum import Enum, unique
import logging
logging.basicConfig(level=logging.INFO)


@unique
class Color(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Core(object):

    def __init__(self, board_size=19):
        assert board_size > 0 and board_size <= 30, "Board size must be positive and less than or equal to 30"
        self.__board_size = board_size
        self.__board = np.zeros((board_size, board_size), dtype=int)
        self.__turn = Color.BLACK
        self.__winner = Color.EMPTY
        self.__place_list = []

    @property
    def turn(self):
        return self.__turn

    @property
    def winner(self):
        return self.__winner

    def __str__(self):
        return str(self.__board)+'\n'+f'Turn: {self.__turn.value}, Winner: {self.__winner.value}'

    def reset_board(self,bord_size=None):
        if bord_size is not None:
            self.__board_size = bord_size
        self.__board = np.zeros(
            (self.__board_size, self.__board_size), dtype=int)
        self.__turn = Color.BLACK
        self.__winner = Color.EMPTY
        self.__place_list=[]

    def place_stone(self, x, y):
        assert x >= 0 and x < self.__board_size, "Invalid x coordinate"
        assert y >= 0 and y < self.__board_size, "Invalid y coordinate"
        if self.__board[x, y] == Color.EMPTY.value:
            self.__board[x, y] = self.__turn.value
            if self.__check_win(x, y):
                self.__winner = self.__turn
                logging.info(f"Winner is {self.__winner}")
            self.__place_list.append([(x,y),self.__turn])
            if len(self.__place_list) > 20:
                self.__place_list = self.__place_list[-10:]
            self.__switch_turn()
            return True
        return False
    
    def undo_move(self):
        if not self.__place_list:
            return False
        last_move = self.__place_list.pop()
        x, y = last_move[0]
        self.__board[x, y] = Color.EMPTY.value
        self.__turn = last_move[1]
        return True

    def __switch_turn(self):
        if self.__turn == Color.BLACK:
            self.__turn = Color.WHITE
        else:
            self.__turn = Color.BLACK

    def __check_win_on_line(self, i, go_line):
        if go_line[i] == Color.EMPTY.value:
            return False
        if len(go_line) < 5:
            return False
        count = 1
        t = i+1
        while t < len(go_line) and go_line[t] == go_line[i]:
            count += 1
            t += 1
        t = i-1
        while t >= 0 and go_line[t] == go_line[i]:
            count += 1
            t -= 1
        return count >= 5

    def __check_win(self, x, y):
        ifwin = False
        ifwin |= self.__check_win_on_line(y, self.__board[x, :])
        ifwin |= self.__check_win_on_line(x, self.__board[:, y])
        ifwin |= self.__check_win_on_line(
            min(x, y), self.__board.diagonal(y - x))
        ifwin |= self.__check_win_on_line(min(x, self.__board_size - 1 - y), np.fliplr(
            self.__board).diagonal((self.__board_size - 1 - y)-x))
        return ifwin


if __name__ == "__main__":
    pass
