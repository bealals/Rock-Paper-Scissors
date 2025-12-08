import random

# imports necessary items in order to be able to show the super duper cool image
from PIL import Image
from term_image.image import AutoImage
import io
import os

# global dictionary bc i'm cooler than you guys
player_data = {}

# the functions that chatgpt told me to add or else this wouldn't work
SCORE_FILE = "highscore.txt"
DELIMITER = "|"

# high score thingy because sure why not
def scores():
    score = {}

    if not os.path.exists(SCORE_FILE):
        return score
    
    with open(SCORE_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            name, win, loss = line.split(DELIMITER)
            score[name] = {"win": int(win), "loss": int(loss)}
    return score

def save(name, win, loss):
    score = scores()

    if name not in score or win > score[name]["win"]:
        score[name] = {"win": win, "loss": loss}

    with open("highscore.txt", "w") as file:
        for player, record in score.items():
            file.write(f"{player}{DELIMITER}{record['win']}{DELIMITER}{record['loss']}\n")

def show():
    score = scores()

    if not score:
        print("\nNo high score is available yet :)")

    print()
    sort_score = sorted(score.items(), key = lambda x: x[1]["win"], reverse=True)

    for name, record in sort_score:
        print(f"{name}: {record['win']} wins, {record['loss']} loss")

# Get the player's name in order to keep everything orderly and allow the global dictionary to keep track of wins and losses
def player_info():
    name = input("Please enter your name: ").strip().capitalize()
    if name not in player_data:
        player_data[name] = {"wins": 0, "losses": 0}    # 
    return name

# Get the player's input for what they want to play within that round
def player_play():
    play = input("Rock 🪨, Paper 📄, or Scissors ✂️: ").strip().lower()
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
    # Error-checking to make sure the image in able to load properly
    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()

        print(binary_data[:50])
        return binary_data
    except FileNotFoundError:
        print("Whoopsies, this image was not found. Sounds like you problem so go check your file path... 🤷")
    except PermissionError:
        print("🚫 Womp womp... You don't have permission to access that file")

# Run everything so that it works -- run each function and print out the specific responses using each functions
def main():
    print("----*** Welcome to Rock-Paper-Scissors! ***----")
    name = player_info()

    while True:
        # Runs 5 rounds
        for i in range(5):
            computer_choice = computer_play()
            player_choice = player_play()

            print(f"Round {i+1}: You chose: {player_choice}, you're opponent chose: {computer_choice}")
            result = winner(player_choice, computer_choice)
            update_score(name, result)

            # Allows the player to keep track of scoring
            print(f"Wins: {player_data[name]['wins']} || Losses: {player_data[name]['losses']}")
        
        print("----*** Results ***----")
        # Decide who wins in at the end of the game
        if player_data[name]["wins"] > player_data[name]["losses"]:
            print("Congratulations! You win ✨")
        elif player_data[name]["losses"] > player_data[name]["wins"]:
            print("Sucks to suck, buckaroo... you lose 🥸")
        elif player_data[name]["wins"] == player_data[name]["losses"]:
            print("Gosh darn, looks like there's a tie...")
        
        save(name, player_data[name]["wins"], player_data[name]["losses"])

        print("----*** High Scores ***----")
        show()
        print()

        # Making my own class in case someone doesn't want to continue playing this amazing game
        class HeHeHaHa(Exception):
            pass
        # Error checking to see if they want to play again or if they hate me
        try:
            # Get user input as a way to decide if you should repeat the code or let it be
            again = input("Do you want to play again? (yes/no) \n").lower()
            # Show image ehehhahhahaha
            if again not in ["yes", "y"]:
                raise HeHeHaHa(again)
        except HeHeHaHa:
            file_path = r"C:\Users\icampa74\Downloads\congrats.webp"

            binary_data = import_image(file_path)

            img = Image.open(io.BytesIO(binary_data))
            #img.show()
            image_display= AutoImage(img)
            image_display.draw()

            # Fake enthusiasm when in reality I will forever hate them for not wanting to continue my spectacular game
            print(f"Thank you for playing, {name} :D")
            # Allowing this loser to not use my code
            break

# Run main
if __name__ =="__main__":
    main()
