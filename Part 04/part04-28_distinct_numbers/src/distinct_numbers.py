def distinct_numbers(list):
    short_list = []
    for i in list:
        if i not in short_list:
            short_list.append(i)
    short_list.sort()
    return short_list







if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]