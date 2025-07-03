def shortest(list):
    shortest_word = list[0]
    for i in list:
        if len(i) < len(shortest_word):
            shortest_word = i
    return shortest_word






if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)