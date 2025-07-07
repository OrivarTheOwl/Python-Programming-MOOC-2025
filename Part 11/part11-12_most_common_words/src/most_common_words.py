def most_common_words(filename: str, lower_limit: int):
    all_words = []
    limit_words = {}
    with open(filename) as file:
        for line in file:
            words = line.split(" ")
            for word in words:
                word = word.strip()
                if "." in word or "," in word:
                    word = word[:-1]
                all_words.append(word)

    return {word: all_words.count(word) for word in all_words if all_words.count(word) >= lower_limit}


if __name__ =="__main__":
    print(most_common_words("comprehensions.txt", 3))