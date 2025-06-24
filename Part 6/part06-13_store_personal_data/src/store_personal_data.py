def store_personal_data(person: tuple):
    name = person[0]
    age = person[1]
    height = person[2]

    with open("people.csv", "a") as file:
        file.write(f"{name};{age};{height}")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))