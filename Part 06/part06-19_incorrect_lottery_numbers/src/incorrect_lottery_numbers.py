def filter_incorrect():
    open("correct_numbers.csv", "w").close()
    valid = True
    week_num = 1


    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            number_list = []
            valid = True
            index = 0

            line = line.strip()
            parts = line.split(";")
            week = parts[0]
            numbers = parts[1].split(",")

            # Condition 1 if week number is incorrect
            if week != f"week {week_num}":
                valid = False
            week_num += 1

            # Condition 2 if numbers are not integers
            try:
                for number in numbers:
                    number = int(number)
                    numbers[index] = number
                    index += 1
            except ValueError:
                valid = False
                continue

            # Condition 3 if there are too few numbers
            if len(numbers) != 7:
                valid = False

            # Condition 4 if numbers are too small or large
            for number in numbers:
                if number < 1 or number > 39:
                    valid = False

            # Condition 5 if the name number appears twice
            for number in numbers:
                if number not in number_list:
                    number_list.append(number)
                elif number in number_list:
                    valid = False
            
            if valid:
                with open("correct_numbers.csv", "a") as new_file:
                    new_file.write(f"{line}\n")

            

if __name__ == "__main__":
    filter_incorrect()