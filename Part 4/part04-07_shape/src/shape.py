# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if string == "":
        print(number * "*")
    else:
        print(number * string[0])


def shape(number1, letter1, number2, letter2):
    i = 1
    j = 0

    while i <= number1:
        line(i, letter1)
        i += 1

    while j < number2:
        line(number1, letter2)
        j += 1



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")