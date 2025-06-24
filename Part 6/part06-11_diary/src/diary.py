while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_input = int(input("Function: "))

    if user_input == 1:
        entry = input("Diary entry: ") + "\n"
        with open("diary.txt", "a") as my_file:
            my_file.write(entry)
            print("Diary saved")
            print()

    elif user_input == 2:
        with open("diary.txt") as my_file:
            for line in my_file:
                print(line, end = "")

    elif user_input == 0:
        print("Bye now!")
        break