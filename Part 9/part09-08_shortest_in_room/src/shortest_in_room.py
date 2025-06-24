class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people_list = []

    def add(self, person: Person):
        self.people_list.append(person)

    def is_empty(self):
        return len(self.people_list) == 0

    def print_contents(self):
        total_height = 0
        for person in self.people_list:
            total_height += person.height

        print(f"There are {len(self.people_list)} persons in the room, and their combined height is {total_height} cm")
        for person in self.people_list:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = self.people_list[0]
            for person in self.people_list:
                if person.height < shortest_person.height:
                    shortest_person = person
        return shortest_person
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortest = (self.shortest())
            self.people_list.remove(shortest)
            return shortest

            


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()