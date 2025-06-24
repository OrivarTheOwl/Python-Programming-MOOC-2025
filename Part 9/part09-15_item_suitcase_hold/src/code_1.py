class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__storage = []
        self.__current_weight = 0

    def add_item(self, item: Item):
        if self.__current_weight + item.weight() <= self.max_weight:
            self.__storage.append(item)
            self.__current_weight += item.weight()

    def __str__(self):
        if len(self.__storage) == 1:
            return f"{len(self.__storage)} item ({self.__current_weight} kg)" 
        else:
            return f"{len(self.__storage)} items ({self.__current_weight} kg)"

    def print_items(self):
        for item in self.__storage:
            print(item)

    def weight(self):
        return self.__current_weight
    
    def heaviest_item(self):
        heaviest_weight = 0
        heaviest_item = None
        if len(self.__storage) == 0:
            return None
        else:
            for item in self.__storage:
                if item.weight() > heaviest_weight:
                    heaviest_weight = item.weight()
                    heaviest_item = item
        return heaviest_item


class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__storage = []
        self.__current_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.__current_weight + suitcase.weight() <= self.max_weight:
            self.__storage.append(suitcase)
            self.__current_weight += suitcase.weight()

    def __str__(self):
        if len(self.__storage) == 1:
            return f"{len(self.__storage)} suitcase, space for {self.max_weight - self.__current_weight} kg"
        else:
            return f"{len(self.__storage)} suitcases, space for {self.max_weight - self.__current_weight} kg"

    def print_items(self):
        for suitcase in self.__storage:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()