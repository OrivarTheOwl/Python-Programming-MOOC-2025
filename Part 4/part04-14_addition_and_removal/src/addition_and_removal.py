list = []

print(f"The list is now {list}")

while True:
    selection = input("a(d)d, (r)emove or e(x)it: ")
    if selection == "x":
        print("Bye!")
        break
    elif selection == "d":
        list.append(len(list) + 1)
        print(f"The list is now {list}")
    elif selection == "r":
        list.pop(len(list) - 1)
        print(f"The list is now {list}")