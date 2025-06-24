# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum() / self.count_numbers()
    

def main():
    all_nums = NumberStats()
    evens = NumberStats()
    odds = NumberStats()

    while True:
        user_input = int(input("Please type in integer numbers: "))
        if user_input == -1:
            break
        all_nums.add_number(user_input)

        if user_input % 2 == 0:
            evens.add_number(user_input)
        elif user_input % 2 == 1:
            odds.add_number(user_input)
        

    print("Sum of numbers:", all_nums.get_sum())
    print("Mean of numbers:", all_nums.average())
    print("Sum of even numbers:", evens.get_sum())
    print("Sum of odd numbers:", odds.get_sum())


main()