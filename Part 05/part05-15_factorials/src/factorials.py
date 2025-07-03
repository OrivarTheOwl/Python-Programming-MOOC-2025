def factorials(n: int):
    new_dict = {}
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        new_dict[i] = factorial
        i += 1
    return new_dict


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])