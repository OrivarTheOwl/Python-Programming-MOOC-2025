def who_won(game_board: list):
    p1_score = 0
    p2_score = 0
    for row in game_board:
        for tile in row:
            if tile == 1:
                p1_score += 1
            elif tile == 2:
                p2_score += 1
    if p1_score > p2_score:
        return 1
    elif p2_score > p1_score:
        return 2
    else:
        return 0





if __name__ == "__main__":
    matrix = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    who_won(matrix)