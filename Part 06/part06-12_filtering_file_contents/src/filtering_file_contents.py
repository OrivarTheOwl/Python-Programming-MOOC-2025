def filter_solutions():
    open("correct.csv", "w").close()
    open("incorrect.csv", "w").close()

    with open("solutions.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            num3 = int(parts[2])
            if "+" in parts[1]:
                numbers = parts[1].split("+")
                num1 = int(numbers[0])
                num2 = int(numbers[1])

                if num1 + num2 == num3:
                    with open("correct.csv", "a") as file:
                        file.write(line)
                elif num1 + num2 != num3:
                    with open("incorrect.csv", "a") as file:
                        file.write(line)

            elif "-" in parts[1]:
                numbers = parts[1].split("-")
                num1 = int(numbers[0])
                num2 = int(numbers[1])

                if num1 - num2 == num3:
                    with open("correct.csv", "a") as file:
                        file.write(line)
                elif num1 - num2 != num3:
                    with open("incorrect.csv", "a") as file:
                        file.write(line)


if __name__ == "__main__":
    filter_solutions()