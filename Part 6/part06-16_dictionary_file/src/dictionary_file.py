#open("dictionary.txt", "w").close()

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_input = int(input("Function: "))

    if user_input == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        
        full_phrase = finnish + ";" + english

        with open("dictionary.txt", "a") as file:
            file.write(f"{full_phrase}\n")
        
        print("Dictionary word added")

    elif user_input == 2:
        search_term = input("Search term: ")

        with open("dictionary.txt") as file:
            for line in file:
                if search_term in line:
                    temp_phrase = line

                    parts = temp_phrase.split(";")
                    part1 = parts[0]
                    part2 = parts[1]

                    print(f"{part1} - {part2}", end="")
    

    elif user_input == 3:
        print("Bye!")
        break