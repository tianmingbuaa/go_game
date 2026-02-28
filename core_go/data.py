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
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)
        self.turn = Color.BLACK
        self.winner = Color.EMPTY

    def __str__(self):
        return str(self.board)+'\n'+f'Turn: {self.turn}, Winner: {self.winner}'

    def reset_board(self):
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.turn = Color.BLACK
        self.winner = Color.EMPTY

    def place_stone(self, x, y):
        assert x >= 0 and x < self.board_size, "Invalid x coordinate"
        assert y >= 0 and y < self.board_size, "Invalid y coordinate"
        if self.board[x, y] == Color.EMPTY.value:
            self.board[x, y] = self.turn.value
            if self.__check_win(x, y):
                self.winner = self.turn
                logging.info(f"Winner is {self.winner}")
            self.__switch_turn()
            return True
        return False

    def __switch_turn(self):
        if self.turn == Color.BLACK:
            self.turn = Color.WHITE
        else:
            self.turn = Color.BLACK

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
        # Placeholder for winner determination logic
        ifwin = self.__check_win_on_line(y, self.board[x, :]) or self.__check_win_on_line(x, self.board[:, y]) or self.__check_win_on_line(
            y, self.board.diagonal(y - x)) or self.__check_win_on_line(x, np.fliplr(self.board).diagonal((self.board_size - 1 - y) - x))
        return ifwin
    
    


if __name__ == "__main__":
    pass