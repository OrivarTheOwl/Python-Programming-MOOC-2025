def print_sudoku(sudoku: list):
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                sudoku[row][column] = "_"
    
    new_row = 0
    new_column = 0
    new_matrix = sudoku[:]

    for new_row in range(9):
        if new_row > 0 and new_row % 3 == 0:
            print()

        for new_column in range(9):
            print(new_matrix[new_row][new_column], end=" ")
            if (new_column+1) % 3 == 0:
                print(end=" ")
        
        print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []

    for row in sudoku:
        temporary = []
        for index in row:
            temporary.append(index)
        new_sudoku.append(temporary)

    new_sudoku[row_no][column_no] = number
    return new_sudoku





if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)