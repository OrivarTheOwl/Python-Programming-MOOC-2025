# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __gt__(self, another):
        greater = False
        if self.year > another.year:
            greater = True
        elif self.year == another.year:
            if self.month > another.month:
                greater = True
            elif self.month == another.month:
                if self.day > another.day:
                    greater = True
        return greater

    def __lt__(self, another):
        lesser = False
        if self.year < another.year:
            lesser = True
        elif self.year == another.year:
            if self.month < another.month:
                lesser = True
            elif self.month == another.month:
                if self.day < another.day:
                    lesser = True
        return lesser

    def __eq__(self, another):
        return ((self.year == another.year) and (self.month == another.month) and (self.day == another.day))

    def __ne__(self, another):
        return ((self.year != another.year) or (self.month != another.month) or (self.day != another.day))
    
    def __add__(self, added_days):
        new_date = SimpleDate(self.day, self.month, self.year)
        new_date.day += added_days
        while new_date.day > 30:
            new_date.day -= 30
            new_date.month += 1
            if new_date.month > 12:
                new_date.month -= 12
                new_date.year += 1
        return new_date
    
    def __sub__(self, another):
        self_total_days = (self.day + (self.month * 30) + (self.year * 360))
        another_total_days = (another.day + (another.month * 30) + (another.year * 360))
        return abs(self_total_days - another_total_days)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)