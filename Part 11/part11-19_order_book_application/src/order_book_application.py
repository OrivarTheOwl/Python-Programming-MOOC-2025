class Task:
    _count = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task._count
        self.finished = False
        Task._count += 1

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished_status()}"
    
    def is_finished(self):
        return self.finished
    
    def finished_status(self):
        return "FINISHED" if self.finished else "NOT FINISHED"
    
    def mark_finished(self):
        self.finished = True

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set([person.programmer for person in self.orders]))
    
    def mark_finished(self, id: int):
        for person in self.orders:
            if person.id == id:
                person.mark_finished()
                return
        raise ValueError("ID not found")
        
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if order.is_finished() == False]
    
    def status_of_programmer(self, programmer: str):
        finished_hours = 0
        unfinished_hours = 0
        finished_orders = [order for order in self.finished_orders() if order.programmer == programmer]
        unfinished_orders = [order for order in self.unfinished_orders() if order.programmer == programmer]

        for person in self.orders:
            if person.programmer == programmer:
                for order in finished_orders:
                    finished_hours += order.workload
                for order in unfinished_orders:
                    unfinished_hours += order.workload
                return f"tasks: finished {len(finished_orders)} not finished {len(unfinished_orders)}, hours: done {finished_hours} scheduled {unfinished_hours}"
        raise ValueError("No programmer with the given name")

class UserInterface:
    def __init__(self):
        self.action = OrderBook()

    def commands(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def run(self):
        self.commands()
        while True:
            print()
            user_input = input("command: ")
            if user_input == "0":
                break
            elif user_input == "1":
                description = input("description: ")
                name_and_hours = input("programmer and workload estimate: ")
                parts = name_and_hours.split(" ")
                name = parts[0]
                try:
                    hours = int(parts[1])
                except:
                    print("erroneous input")
                    continue
                self.action.add_order(description, name, hours)
                print("added!")

            elif user_input == "2":
                finished = self.action.finished_orders()
                if finished:
                    for order in finished:
                        print(order)
                else:
                    print("no finished tasks")

            elif user_input == "3":
                unfinished = self.action.unfinished_orders()
                if unfinished:
                    for order in unfinished:
                        print(order)
                else:
                    print("no unfinished tasks")

            elif user_input == "4":
                user_input = input("id: ")
                try:
                    user_id = int(user_input)
                except:
                    print("erroneous input")
                    continue
                try:
                    self.action.mark_finished(user_id)
                except:
                    print("erroneous input")
                    continue
                print("marked as finished")

            elif user_input == "5":
                programmers = self.action.programmers()
                if programmers:
                    for programmer in programmers:
                        print(programmer)
                else:
                    print("no programmers")

            elif user_input == "6":
                name = input("programmer: ")
                try:
                    print(self.action.status_of_programmer(name))
                except:
                    print("erroneous input")



test = UserInterface()
test.run()