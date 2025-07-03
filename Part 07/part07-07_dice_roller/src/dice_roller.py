from random import choice

def roll(die: str):
    if die == "A":
        result = choice([3, 3, 3, 3, 3, 6])
    if die == "B":
        result = choice([2, 2, 2, 5, 5, 5])
    if die == "C":
        result = choice([1, 4, 4, 4, 4, 4])

    return result


def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    
    for i in range(times):
        if die1 == "A":
            result1 = choice([3, 3, 3, 3, 3, 6])
        if die1 == "B":
            result1 = choice([2, 2, 2, 5, 5, 5])
        if die1 == "C":
            result1 = choice([1, 4, 4, 4, 4, 4])

        if die2 == "A":
            result2 = choice([3, 3, 3, 3, 3, 6])
        if die2 == "B":
            result2 = choice([2, 2, 2, 5, 5, 5])
        if die2 == "C":
            result2 = choice([1, 4, 4, 4, 4, 4])

        if result1 > result2:
            die1_wins += 1
        elif result1 < result2:
            die2_wins += 1
        elif result1 == result2:
            ties += 1
    
    final_score = (die1_wins, die2_wins, ties)
    return final_score


if __name__ == "__main__":

    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)