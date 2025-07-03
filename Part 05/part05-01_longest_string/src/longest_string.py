def longest(strings: list):
    biggest_word = ""
    for string in strings:
        if len(string) > len(biggest_word):
            biggest_word = string

    return biggest_word



    
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
