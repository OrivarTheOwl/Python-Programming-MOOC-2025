def largest():
    with open("numbers.txt") as test_file:
        largest_number = 0

        for line in test_file:
            if int(line) > largest_number:
                largest_number = int(line)
    print(largest_number)
    return largest_number

if __name__ == "__main__":
    largest()
    