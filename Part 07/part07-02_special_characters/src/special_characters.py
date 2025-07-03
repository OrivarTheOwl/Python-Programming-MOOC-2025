from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    normal_chars = ""
    punctuation_chars = ""
    other_chars = ""
    
    
    for letter in my_string:
        if letter in ascii_letters:
            normal_chars += letter
        elif letter in punctuation:
            punctuation_chars += letter
        else:
            other_chars += letter

    all = (normal_chars, punctuation_chars, other_chars)
    return all
    



if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])