def read_fruits():
    with open("fruits.csv") as file:
        catalogue = {}

        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])

            catalogue[name] = price
    return catalogue



if __name__ == "__main__":
    read_fruits()