def prime_numbers():
    number = 1
    while True:
        if is_prime(number):
            yield number
        number += 1

def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))