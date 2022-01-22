# Create a guessing number game
# Numbers are from 1- 100
# Ask the user to choose a category (easy, hard)
# Easy category has 5 attempts to guess
# Hard category has 10 attempts to guess

import random
import os
from Day_12_Art import logo

# Global Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare(computer_num):
    user_num = int(input("Make a guess: "))
    if user_num == computer_num:
        print(f"You got it . The answer was {computer_num}")
        return 1
    elif user_num > computer_num:
        print("Too high")
    else:
        print("Too low")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    category = input("Choose a category. Type 'easy' or 'hard': ").lower()

    if category == "hard":
        num_guess = HARD_LEVEL_TURNS
        print(f"You have {num_guess} attempts to guess the number.")
    elif category == "easy":
        num_guess = EASY_LEVEL_TURNS
        print(f"You have {num_guess} attempts to guess the number.")
    else:
        print("Invalid response")
        num_guess = 0

    computer_num = random.randint(1, 100)  # randomly choose a number between 1 and 100

    game_over = False

    while game_over is False:
        while num_guess >0:
            if compare(computer_num) == 1: # the user already guessed the number
                game_over = True
                break
            num_guess-=1
            print("Guess again.")
            print(f"You have {num_guess} attempts to guess the number.")
        else:
            print("You've run out of guesses. You lose!")

        game_over = True

# --------------------------------------------------------------------------------

play_game = True

while play_game is True:
    os.system("cls||clear")
    game()
    if input("Do you want to play again. Type 'y' or 'n': ?") == "y":
        play_game = True
    else:
        play_game = False
        print("Thank you for playing the Number Guessing Game. Goodbye!")