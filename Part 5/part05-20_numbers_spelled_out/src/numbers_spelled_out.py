def dict_of_numbers():
    ones = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

    numbers = {}

    for i in range(100):
        if i >= 0 and i < 10:
            numbers[i] = ones[i]
        elif i >= 10 and i < 20:
            numbers[i] = teens[i]
        elif i >= 20 and i < 100:
            if i % 10 == 0:
                numbers[i] = tens[i]
            else:
                first_digit = i // 10
                second_digit = i % 10
                numbers[i] = tens[first_digit * 10] + "-" + ones[second_digit]
    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])