def find_words(search_term: str):
    all_words = []
    word_list = []
    
    with open("words.txt") as new_file:
        for word in new_file:
            all_words.append(word.strip())


    if "." in search_term:
        i = 0
        dot_places = []
        for letter in search_term:
            if letter == ".":
                dot_places.append(i)
            i += 1

        for word in all_words:
            if len(search_term) == len(word):
                keep_going = True
                j = 0
                temp_word = ""
                for letter in search_term:
                    if letter == word[j] and j not in dot_places:
                        temp_word += word[j]
                    elif j in dot_places:
                        temp_word += word[j]
                    else:
                        keep_going = False
                        break
                    j += 1
                if keep_going == True:
                    temp_word = temp_word[::1]
                    word_list.append(temp_word)

            

    elif "*" in search_term:
        if search_term.startswith("*"):
            phrase = search_term[1:]
            for word in all_words:
                if word.endswith(phrase):
                    word_list.append(word)

        elif search_term.endswith("*"):
            phrase = search_term[:-1]
            for word in all_words:
                if word.startswith(phrase):
                    word_list.append(word)

    else:
        for word in all_words:
            if search_term == word:
                word_list.append(word)



    return word_list



if __name__ == "__main__":
    print(find_words("p.ng"))