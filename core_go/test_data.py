from data import Core
import numpy as np


def test_check_win_on_line():
    core = Core()
    assert core._Core__check_win_on_line(0, [0, 0, 0, 0, 0]) == False
    assert core._Core__check_win_on_line(0, [1, 1, 1, 1, 1]) == True
    assert core._Core__check_win_on_line(0, [2, 2, 2, 2, 2]) == True
    assert core._Core__check_win_on_line(
        4, [1, 1, 1, 1, 2, 2, 2, 2, 2]) == True
    assert core._Core__check_win_on_line(0, [1, 1, 1, 1, 2]) == False
    assert core._Core__check_win_on_line(
        5, [1, 1, 1, 1, 0, 2, 2, 2, 2, 1, 2]) == False
    print("All tests passed!")


def test_check_win():
    core = Core(10)
    core._Core__board = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                          [2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 2, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 2, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]])
    core._Core__switch_turn()
    core.place_stone(7, 4)
    # core._Core__switch_turn()
    core.place_stone(0, 5)



if __name__ == "__main__":
    test_check_win_on_line()
    test_check_win()
    core = Core(8)
    core.place_stone(0, 0)
    print(core)
    core.place_stone(1, 1)
    print(core)
    core.place_stone(2, 2)
    print(core)
    core.place_stone(3, 3)
    print(core)
    core.undo_move()
    print(core)
    core.place_stone(3, 3)
    print(core)
    # core.place_stone(1, 4)
