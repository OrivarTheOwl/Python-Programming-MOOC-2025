def histogram(word: str):
    letter_count = {}
    star = "*"
    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    
    for key, value in letter_count.items():
        print(f"{key} {star * value}")



if __name__ == "__main__":
    print(histogram("statistically"))