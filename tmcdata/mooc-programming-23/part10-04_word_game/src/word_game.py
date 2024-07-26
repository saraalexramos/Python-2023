
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
        if len(player1_word) < len(player2_word):
            return 2
        

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        player1_vowels = 0
        player2_vowels = 0

        vowels = ["a", "e", "i", "o", "u"]

        for letter in player1_word:
            if letter in vowels:
                player1_vowels += 1
        for letter in player2_word:
            if letter in vowels:
                player2_vowels += 1


        if player1_vowels > player2_vowels:
            return 1
        if player1_vowels < player2_vowels:
            return 2  

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_choice: str, player2_choice: str):
        valid_choices = ["rock", "paper", "scissors"]

        if player1_choice not in valid_choices and player2_choice in valid_choices:
            return 2
        
        elif player2_choice not in valid_choices and player1_choice in valid_choices:
            return 1

        elif player1_choice not in valid_choices and player2_choice not in valid_choices:
            return 0

        elif player1_choice == player2_choice:
            return 0  

        if (
            (player1_choice == "rock" and player2_choice == "scissors") or
            (player1_choice == "paper" and player2_choice == "rock") or
            (player1_choice == "scissors" and player2_choice == "paper")
        ):
            return 1  
        else:
            return 2  


if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()    