def transpose(matrix: list):
    temp_matrix = []
    for row in matrix:
        temp = []
        for index in row:
            temp.append(index)
        temp_matrix.append(temp)


    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] = temp_matrix[column][row]



if __name__ == "__main__":
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

    print(input_matrix[0])
    print(input_matrix[1])
    print(input_matrix[2])
    print()
    transpose(input_matrix)
    print(input_matrix[0])
    print(input_matrix[1])
    print(input_matrix[2])