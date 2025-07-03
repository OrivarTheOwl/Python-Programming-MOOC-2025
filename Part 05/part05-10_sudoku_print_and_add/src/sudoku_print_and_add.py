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



def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number






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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)