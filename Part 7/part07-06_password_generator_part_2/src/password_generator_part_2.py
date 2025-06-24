from random import choice, shuffle, seed
from string import ascii_lowercase

def generate_strong_password(length: int, yes_nums: bool, yes_special: bool):
    special_chars = ["!", "?", "=", "+", "-", "(", ")", "#"]
    password = []
    i = 0

    password += choice(ascii_lowercase)
    i += 1

    if yes_nums:
        password.append(str(choice(range(1,10))))
        i += 1
    if yes_special:
        password.append(choice(special_chars))
        i += 1

    while i < length:
        password.append(choice(ascii_lowercase) or str(choice(range(1,10))) or choice(special_chars))
        i += 1

    shuffle(password)
    password = "".join(password)
    return password       



if __name__ == "__main__":
    seed(1)
    for i in range(10):
        print(generate_strong_password(8, True, True))