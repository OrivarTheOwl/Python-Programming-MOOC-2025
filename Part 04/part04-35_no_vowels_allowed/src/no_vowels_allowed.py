def no_vowels(sentence):
    new_sentence = ""
    letter = sentence[0]
    vowels = ["a", "e", "i", "o", "u"]
    for letter in sentence:
        if letter not in vowels:
            new_sentence += letter
    return new_sentence




if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))