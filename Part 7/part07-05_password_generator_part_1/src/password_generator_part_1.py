from random import randint, seed
from string import ascii_lowercase


def generate_password(length: int):
    password = ""

    for i in range(length):
        letter = ascii_lowercase[randint(0, len(ascii_lowercase)-1)]
        password += letter

    return password


if __name__ == "__main__":
    seed(1)
    for i in range(10):
        print(generate_password(8))