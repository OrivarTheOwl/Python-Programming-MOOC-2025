def times_ten(start_index: int, end_index: int):
    new_dict = {}
    for index in range(start_index, end_index+1):
        new_dict[index] = index * 10
    return new_dict




if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)