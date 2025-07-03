from random import choice


def words(n: int, beginning: str):
    word_list = []
    possible_words = []
    chosen_words = []
    i = 0

    with open("words.txt") as new_file:
        for line in new_file:
            word_list.append(line.strip())
    
    for word in word_list:
        if word.startswith(beginning) and word not in possible_words:
            possible_words.append(word)

    if len(possible_words) < n:
        raise ValueError
    
    while i < n:
        random_word = choice(possible_words)
        if random_word not in chosen_words:
            chosen_words.append(random_word)
            i += 1

    return chosen_words

        

if __name__ == "__main__":
    word_list = words(5, "car")
    for word in word_list:
        print(word)