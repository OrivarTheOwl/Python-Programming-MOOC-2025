def first_word(sentence):
    i = 0
    while i < len(sentence) - 1:
        if sentence[i] == " ":
            return sentence[:i]
        i += 1


def second_word(sentence):
    i = 0
    j = 0
    while i < len(sentence) - 1:
        if sentence[i] == " " and j == 0:
            k = i
            j += 1
        elif sentence[i] == " " and j == 1:
            return sentence[k+1:i]
        i += 1
    return last_word(sentence)
            



def last_word(sentence):
    i = len(sentence) - 1
    while i <= len(sentence) - 1:
        if sentence[i] == " ":
            return sentence[i+1:]
        i -= 1







# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was a dark and stormy night"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))