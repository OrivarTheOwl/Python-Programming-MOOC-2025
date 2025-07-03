from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def change_case(orig_string: str):
    new_string = []
    for letter in orig_string:
        if letter in ascii_lowercase:
            new_string.append(letter.upper())
        elif letter in ascii_uppercase:
            new_string.append(letter.lower())
        else:
            new_string.append(letter)

    return "".join(new_string)


def split_in_half(orig_string: str):
    str_len = len(orig_string)
    half_len = str_len // 2
    if str_len % 2 == 0:
        first_half = orig_string[:half_len]
        second_half = orig_string[half_len:]
    elif str_len % 2 != 0:
        first_half = orig_string[:half_len]
        second_half = orig_string[half_len:]

    return first_half, second_half



def remove_special_characters(orig_string: str):
    new_string = []
    for letter in orig_string:
        if letter in ascii_lowercase or letter in ascii_uppercase or letter in digits or letter in " ":
            new_string.append(letter)
    return "".join(new_string)


if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)