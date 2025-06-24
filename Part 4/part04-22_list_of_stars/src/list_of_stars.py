def list_of_stars(numbers):
    for i in numbers:
        star_count = "*" * i
        print(star_count)



if __name__ == "__main__":
    list_of_numbers = [3, 7, 1, 1, 2]
    print(list_of_stars(list_of_numbers))