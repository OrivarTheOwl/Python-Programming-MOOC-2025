def proper_file():
    matrix = {}
    i = 1
    row_no = f"row{i}"
    with open("matrix.txt") as file:
        for row in file:
            row = row.replace("\n", "")
            numbers = row.split(",")

            matrix[row_no] = numbers
            i += 1
            row_no = f"row{i}"

    return matrix
            


def matrix_sum():
    matrix = proper_file()
    summed_nums = 0
    for row in matrix:
        for index in matrix[row]:
            summed_nums += int(index)

    return summed_nums


def matrix_max():
    matrix = proper_file()
    max_num = 0
    for row in matrix:
        for index in matrix[row]:
            if int(index) > max_num:
                max_num = int(index)
    
    return max_num

def row_sums():
    matrix = proper_file()
    all_row_sums = []
    row_sum = 0
    for row in matrix:
        for index in matrix[row]:
            row_sum += int(index)
        all_row_sums.append(row_sum)
        row_sum = 0

    return all_row_sums


if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()