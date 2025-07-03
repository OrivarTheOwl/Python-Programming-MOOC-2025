my_list = []
i = 0

how_many = int(input("How many items: "))

while i < how_many:
    item_count = int(input(f"Item {i+1}: "))
    my_list.append(item_count)

    i += 1

print((my_list))