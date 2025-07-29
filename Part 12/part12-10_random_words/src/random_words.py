from random import choice

def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        word = ""
        for i in range(length):
            letter = choice(characters)
            word += letter
        yield word

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)