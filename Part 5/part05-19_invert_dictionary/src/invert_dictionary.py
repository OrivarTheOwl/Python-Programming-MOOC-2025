def invert(dictionary: dict):
    copy = {}
    for key, value in dictionary.items():
        copy[value] = key
    dictionary.clear()
    for key, value in copy.items():
        dictionary[key] = value


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)