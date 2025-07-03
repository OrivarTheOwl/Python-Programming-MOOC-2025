phone_book = {}

while True:
    user_input = int(input("command (1 search, 2 add, 3 quit): "))
    if user_input == 3:
        break
    elif user_input == 2:
        name = input("name: ")
        number = input("number: ")
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print("ok!")
    elif user_input == 1:
        name = input("name: ")
        if name in phone_book:
            for number in phone_book[name]:
                print(number)
        else:
            print("no number")

print("quitting...")