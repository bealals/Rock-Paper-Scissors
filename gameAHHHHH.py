import random

# imports necessary items in order to be able to show the super duper cool image
from PIL import Image
from term_image.image import AutoImage
import io

# global dictionary bc i'm cooler than you guys
player_data = {}

# Get the player's name in order to keep everything orderly and allow the global dictionary to keep track of wins and losses
def player_info():
    name = input("Please enter your name: ").strip().capitalize()
    if name not in player_data:
        player_data[name] = {"wins": 0, "losses": 0}    # 
    return name

# Get the player's input for what they want to play within that round
def player_play():
    play = input("Rock 🪨, Paper 📄, or Scissors ✂️").strip().lower()
    while play not in ["rock", "paper", "scissors"]:
        play = input("Nope! Try again...").strip().lower()
    return play

# Have the computer randomize a choice
def computer_play():
    return random.choice(["rock", "paper", "scissors"])

# Figure out which player (computer or player) won
def winner(player_play, computer_play):
    if player_play == computer_play:
        return "tie 👔"
    elif (
        (player_play == "rock" and computer_play == "scissors") or
        (player_play == "paper" and computer_play == "rock") or
        (player_play == "scissors" and computer_play == "paper")
        ):
        return "win 🏆"
    else:
        return "lose 💔"
    
# Update the overall score in order to keep track with the wins and losses per round     
def update_score(name, result):
    if result == "win 🏆":
        player_data[name]["wins"] += 1
    elif result == "lose 💔":
        player_data[name]["losses"] += 1

# Importing an image because I'm cooler than all of you doo-doos
def import_image(file_path):
    with open(file_path, "rb") as file:
        binary_data = file.read()

    print(binary_data[:50])
    return binary_data

# Run everything so that it works -- run each function and print out the specific responses using each functions
def main():
    name = player_info()

    # Runs 5 rounds
    for i in range(5):
        computer_choice = computer_play()
        player_choice = player_play()

        print(f"Round {i+1}: You chose: {player_choice}, you're opponent chose: {computer_choice}")
        result = winner(player_choice, computer_choice)
        update_score(name, result)

        # Allows the player to keep track of scoring
        print(f"Wins: {player_data[name]['wins']} || Losses: {player_data[name]['losses']}")
    
    # Decide who wins in at the end of the game
    if player_data[name]["wins"] >= player_data[name]["losses"]:
        print("Congratulations! You win ✨")
    elif player_data[name]["losses"] >= player_data[name]["wins"]:
        print("Sucks to suck, buckaroo... you lose 🥸")
    elif player_data[name]["wins"] == player_data[name]["losses"]:
        print("Gosh darn, looks like there's a tie...")

    # Get user input as a way to decide if you should repeat the code or let it be
    again = input("Do you want to play again? (yes/no) \n").lower()

    # Show image ehehhahhahaha
    if again.lower() not in ["yes", "y"]:
        file_path = r"C:\Users\icampa74\Downloads\congrats.webp"

        binary_data = import_image(file_path)

        img = Image.open(io.BytesIO(binary_data))
        #img.show()
        image_display= AutoImage(img)
        image_display.draw()

        print("Thank you for playing :D")

# Run main
if __name__ =="__main__":
    main()
