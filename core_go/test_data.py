from data import Core

def test_check_win_on_line():
    core = Core()
    assert core._Core__check_win_on_line(0, [0, 0, 0, 0, 0]) == False
    assert core._Core__check_win_on_line(0, [1, 1, 1, 1, 1]) == True
    assert core._Core__check_win_on_line(0, [2, 2, 2, 2, 2]) == True
    assert core._Core__check_win_on_line(4, [1, 1, 1, 1, 2,2,2,2,2]) == True
    assert core._Core__check_win_on_line(0, [1, 1, 1, 1, 2]) == False
    assert core._Core__check_win_on_line(5, [1, 1, 1, 1, 0,2,2,2,2,1,2]) == False
    print("All tests passed!")

if __name__ == "__main__":
    test_check_win_on_line()
    core = Core(10)
    core.reset_board()
    core.place_stone(0, 0)
    core.place_stone(1, 0)
    core.place_stone(0, 1)
    core.place_stone(1, 1)
    core.place_stone(0, 2)
    core.place_stone(1, 2)
    core.place_stone(0, 3)
    core.place_stone(1, 3)
    core.place_stone(0, 4)
    core.place_stone(1, 4)

    print(core)
    print(core.turn)
