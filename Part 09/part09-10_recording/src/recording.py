class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, new_length: int):
        if new_length > 0:
            self.__length = new_length
        else:
            raise ValueError

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)