# Write your solution here
def spruce(size):
    print("a spruce!")
    star = "*"
    i = size

    while i > 0:
        print(" " * (i - 1) + star)
        star += "**"

        i -= 1
    
    i = size
    star = "*"
    print(" " * (i - 1) + star)






# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)