def longest_series_of_neighbours(numbers : list):
    longest = 1
    record_longest = 1
    for i in range(len(numbers) - 1):
        if numbers[i] + 1 == numbers[i+1] or numbers[i] - 1 == numbers[i+1]:
            longest += 1
            if longest > record_longest:
                record_longest = longest
        else:
            longest = 1
    return record_longest




if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))