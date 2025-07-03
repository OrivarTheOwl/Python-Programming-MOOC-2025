phone_book = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))
    if user_input == 3:
        break
    elif user_input == 2:
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    elif user_input == 1:
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")

print("quitting...")