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
                return (len(finished_orders), len(unfinished_orders), finished_hours, unfinished_hours)
        raise ValueError("No programmer with the given name")





if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)