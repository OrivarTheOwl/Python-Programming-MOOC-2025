def row_sums(my_matrix: list): 
    for row in my_matrix:
        i = 0
        row_sum = 0
        for i in range(len(row)):
            row_sum += row[i]
        row.append(row_sum)



if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)