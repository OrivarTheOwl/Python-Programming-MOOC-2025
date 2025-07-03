def no_shouting(words : list):
    lower_only = []
    for word in words:
        if word.isupper() == False:
            lower_only.append(word)

    return lower_only






if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)