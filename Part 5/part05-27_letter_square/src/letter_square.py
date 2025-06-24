user_input = int(input("Layers: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layers = (user_input * 2) - 1
half = (layers // 2)

current_row = []
all_rows = []
i = 0
j = -1
k = 0
l = 1

for index in range(layers):
    current_row.append(alphabet[user_input - 1])

for row in range(layers):
    
    
    # First half rows
    if row < half:
        while i < row:
            current_row[i + 1] = alphabet[user_input - 1 - row]
            current_row[j - 1] = alphabet[user_input - 1 - row]
            i += 1
            j -= 1

        remaining_indexes = layers - (row * 2) - 2
        replacement = layers - remaining_indexes
        start = replacement // 2
        k = 0

        while k < remaining_indexes:
            current_row[start + k] = alphabet[user_input - 1 - row]
            k += 1

        current_row_string = "".join(current_row)
        all_rows.append(current_row_string) 


    # Middle row
    elif row == half:
        current_row = []
        current_row_string = ""
        
        # First 3 indexes + middle index
        for index in range(half + 1):
            current_row.append(alphabet[user_input - 1 - index])

        # Last 3 indexes
        for index in range(half):
            current_row.append(alphabet[index + 1])
            
        current_row_string = "".join(current_row)
        all_rows.append(current_row_string)


    # Second half rows
    elif row > half:
        all_rows.append(all_rows[-l * 2])
        l += 1


# Print out all rows 1 by 1
for row in range(len(all_rows)):
    print(all_rows[row])