from random import randint

def lottery_numbers(amount: int, lower: int, upper:int ):
    selected_numbers = []

    while len(selected_numbers) < amount:
        new_number = randint(lower, upper)
        if new_number not in selected_numbers:
            selected_numbers.append(new_number)
    selected_numbers.sort()
    return selected_numbers




if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)