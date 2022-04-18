import Main

def tests_board():
    b = Main.build_board()
    assert Main.get_board_value(b, 1) == -1
    assert Main.get_board_value(b, 2) == 38
    assert Main.get_board_value(b, 3) == -1
    assert Main.get_board_value(b, 4) == -1
    assert Main.get_board_value(b, 5) == -1
    assert Main.get_board_value(b, 6) == -1
    assert Main.get_board_value(b, 7) == 14
    assert Main.get_board_value(b, 8) == 31
    assert Main.get_board_value(b, 9) == -1
    assert Main.get_board_value(b, 10) == -1
    assert Main.get_board_value(b, 11) == -1
    assert Main.get_board_value(b, 12) == -1
    assert Main.get_board_value(b, 13) == -1
    assert Main.get_board_value(b, 14) == -1
    assert Main.get_board_value(b, 15) == 26
    assert Main.get_board_value(b, 16) == 6
    assert Main.get_board_value(b, 17) == -1
    assert Main.get_board_value(b, 18) == -1
    assert Main.get_board_value(b, 19) == -1
    assert Main.get_board_value(b, 20) == -1
    assert Main.get_board_value(b, 46) == 25
    assert Main.get_board_value(b, 89) == 68
    assert Main.get_board_value(b, 90) == -1
    assert Main.get_board_value(b, 91) == -1
    assert Main.get_board_value(b, 92) == 88
    assert Main.get_board_value(b, 93) == -1
    assert Main.get_board_value(b, 94) == -1
    assert Main.get_board_value(b, 95) == 75
    assert Main.get_board_value(b, 96) == -1
    assert Main.get_board_value(b, 97) == -1
    assert Main.get_board_value(b, 98) == -1
    assert Main.get_board_value(b, 99) == 80
    

def tests_check_sum():
    for i in range(1,7):
        for j in range(1,101):
            cond = i == (j // 100 + j // 10 % 10 + j % 10)
            assert Main.check_sum(i, j) == cond


if __name__ == "__main__":
    tests_board()
    tests_check_sum()