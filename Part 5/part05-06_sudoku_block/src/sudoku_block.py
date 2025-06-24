def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for row in sudoku[row_no:row_no+3]:
        for number in row[column_no:column_no+3]:
            if number != 0 and number in numbers:
                return False
            numbers.append(number)
    return True









