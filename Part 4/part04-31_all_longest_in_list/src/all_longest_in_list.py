def all_the_longest(list_of_words):
    longest_word_count = 0
    long_list = []
    for i in list_of_words:
        if len(i) > longest_word_count:
            longest_word_count = len(i)
    for i in list_of_words:
        if len(i) == longest_word_count:
            long_list.append(i)
    return long_list






if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']