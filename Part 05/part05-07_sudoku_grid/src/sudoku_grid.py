def row_correct(soduko: list, row_no: int):
    number_list = []
    for index in soduko[row_no]:
         if index != 0:
              if index in number_list:
                   return False
              number_list.append(index)
    return True


def column_correct(sudoku: list, column_no: int):
    number_list = []
    for index in sudoku:
        if index[column_no] != 0 and index[column_no] in number_list:
            return False
        number_list.append(index[column_no])
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for row in sudoku[row_no:row_no+3]:
        for number in row[column_no:column_no+3]:
            if number != 0 and number in numbers:
                return False
            numbers.append(number)
    return True


def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if row_correct(sudoku, row) == False:
            return False

    for column in range(0,9):
        if column_correct(sudoku, column) == False:
            return False

    for row in range(0,9,3):
        for column in range(0,9,3):
            if block_correct(sudoku, row, column) == False:
                return False

    return True







if __name__ == "__main__":
    
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))