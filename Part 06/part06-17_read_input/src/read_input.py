def read_input(phrase: str, lower_bound: int, upper_bound: int):
    while True:
        try:
            user_input = int(input(phrase))
            if lower_bound < user_input < upper_bound:
                return user_input
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_bound} and {upper_bound}")



if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)