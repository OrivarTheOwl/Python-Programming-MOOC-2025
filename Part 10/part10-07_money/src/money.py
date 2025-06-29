# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__combined = self.__euros + (self.__cents / 100)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__combined == another.__combined
    
    def __gt__(self, another):
        return self.__combined > another.__combined

    def __lt__(self, another):
        return self.__combined < another.__combined

    def __ne__(self, another):
        return self.__combined != another.__combined
    
    def __add__(self, another):
        euros_sum = self.__euros + another.__euros
        cents_sum = self.__cents + another.__cents
        if cents_sum >= 100:
            euros_sum += 1
            cents_sum -= 100

        summed = Money(euros_sum, cents_sum)
        return summed

    def __sub__(self, another):
        euros_diff = self.__euros - another.__euros
        cents_diff = self.__cents - another.__cents
        if cents_diff < 0:
            euros_diff -= 1
            cents_diff += 100
        if euros_diff < 0:
            raise ValueError("a negative result is not allowed")

        difference = Money(euros_diff, cents_diff)
        return difference




if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1