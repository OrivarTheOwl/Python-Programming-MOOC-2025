from fractions import Fraction

def fractionate(amount: int):
    numerator = 1
    denominator = amount

    all_parts = []
    for i in range(amount):
        all_parts.append(Fraction(numerator, denominator))

    return all_parts


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))