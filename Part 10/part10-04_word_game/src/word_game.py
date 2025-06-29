# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass # Tie

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a", "e", "i", "o", "u"]
        player1_vowels = 0
        player2_vowels = 0

        for vowel in vowels:
            i = 0
            j = 0
            while i in range(len(player1_word)):
                if vowel == player1_word[i]:
                    player1_vowels += 1
                i += 1
            while j in range(len(player2_word)):
                if vowel == player2_word[j]:
                    player2_vowels += 1
                j += 1

        if player1_vowels > player2_vowels:
            return 1
        elif player1_vowels < player2_vowels:
            return 2
        else:
            pass # Tie

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        combos = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        auto_lose1 = False
        auto_lose2 = False

        if player1_word not in ["rock", "paper", "scissors"]:
            auto_lose1 = True
        if player2_word not in ["rock", "paper", "scissors"]:
            auto_lose2 = True
        if (auto_lose1 and auto_lose2) or player1_word == player2_word:
            pass # Tie
        elif auto_lose1:
            return 2
        elif auto_lose2:
            return 1

        elif combos[player1_word] == player2_word:
            return 1
        else:
            return 2


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()