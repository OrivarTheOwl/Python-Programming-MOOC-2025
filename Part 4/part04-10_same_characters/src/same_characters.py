def same_chars(string, x, y):
    if x > len(string) - 1 or y > len(string) - 1:
        return False
    elif string[x] == string[y]:
        return True
    else:
        return False







# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))