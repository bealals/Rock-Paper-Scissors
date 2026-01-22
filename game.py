import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    @abstractmethod
    def play(self):
        pass

    def reset_score(self):
        self.wins = 0
        self.losses = 0

class HumanPlayer(Player):
    def play(self):
        choice = input("Rock, Paper, or Scissors: ").strip().lower()
        while choice not in ["rock", "paper", "scissors"]:
            choice = input("Invalid...try again: ").strip().lower()
        return choice

class AI(Player):
     def computer_play(self):
        return random.choice(["rock", "paper", "scissors"])
    
class Combat:
    def __init__(self, player):
        self.player = player
   
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or 
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "win"
        else:
            return "lose"
    
    def play_round(self):
        computer_choice = self.computer_play()
        player_choice = self.player.play()

        print(f"You chose {player_choice}\nComputer chose {computer_choice}")
        result = self.determine_winner(player_choice, computer_choice)

        if result == "win":
            self.player.wins += 1
            print("You win :D")
        elif result == "lose":
            self.player.losses += 1
            print("You lose this round :(")
        else:
           print("It's a tie")

    def play_game(self, rounds = 5):
        self.player.reset_score()

        for i in range(rounds):
            print(f"\nRound {i + 1}")
            self.play_round()

        print("\n---- Game Results ----")
        print(f"Wins: {self.player.wins} | Losses: {self.player.losses}")

        if self.player.wins > self.player.losses:
            print("Overall Winner: You ✨")
        elif self.player.losses > self.player.wins:
            print("Overall Winner: Computer 🤖")
        else:
            print("Overall Result: Tie")