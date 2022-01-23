# Create a game that will guess who has the most number of followers in Instagram
# The program should continue as long as the player's guess is correct

import random
from Day13_game_data import data
from Day13_art import logo
import os

def compare(a_follower, b_follower, guess, score):
    """check which has higher follower count"""
    win_score = score + 1
    if a_follower > b_follower:
        answer= 1
    else:
        answer= 0

    if guess == 'A' and answer == 1:
        print(f"Your're right! Current Score: {win_score} \n")
        resume = 1
    elif guess =='B' and answer == 0:
        print(f"Your're right! Current Score: {win_score} \n")
        resume = 1
    else:
        print(f"Sorry, that's wrong. Current Score: {score} \n")
        resume = 0
    return resume   #value of 1 means the guess is correct and game will resume


def game():
    a = random.choice(data)
    b = random.choice(data)

    game_over = False
    score = 0

    while game_over is False:
        #ensure no duplicate entries for A and B
        while a==b:
            new_celebrity = random.choice(data)
            b= new_celebrity

        a_name = a["name"]
        a_description = a["description"]
        a_country = a["country"]
        a_follower = a["follower_count"]

        b_name = b["name"]
        b_description = b["description"]
        b_country = b["country"]
        b_follower = b["follower_count"]

        # print(f"A: {a_follower}")
        # print(f"B: {b_follower}")

        print(f"Compare A: {a_name}, a {a_description}, from {a_country}")

        print("\n----------------------VERSUS----------------------------\n")

        print(f"Against B: {b_name}, a {b_description}, from {b_country}\n")

        guess = input("Who has more followers? Type 'A' or 'B'?:" ).upper()
        os.system("cls||clear")
        print(logo)
        result = (compare(a_follower, b_follower, guess, score))

        # Guess is correct
        if result == 1:
            game_over = False
            a=b                        # update the value of A
            b = random.choice(data)    # generate another celebrity
            score += 1

        # Guess is wrong
        else:
            game_over = True
            print("Game Over!")


# --------------------------------------------------------------

play_again = True
print(logo)

while play_again is True: 
    game()
    message =input("Do you want to play again? Type 'y' or 'no'?: ").lower()
    if message == 'y':
        play_again = True
        os.system("cls||clear")
        print(logo)
    else:
        play_again = False
        print("Goodbye!")
