def column_correct(sudoku: list, column_no: int):
    number_list = []
    for index in sudoku:
        if index[column_no] != 0 and index[column_no] in number_list:
            return False
        number_list.append(index[column_no])
    return True





