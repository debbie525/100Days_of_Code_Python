
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## (10,11) is a blackjack. The player will win unless the computer also has a blackjack.
## Sum of cards over 21 will lose
## The computer should keep drawing cards as long as it has a score less than 17.
## The player who have a higher cards but not over 21 is the winner.

##################### References #####################

# Go to this website and try out the Blackjack game: 
# https://games.washingtonpost.com/games/blackjack/


import random
from Day11_Art import logo
import os

def deal_card():
    """ returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card

def calculate_score(cards):
    """Calculate the sum of cards.Check for a blackjack (a hand with only 2 cards: ace + 10)
    Check for ace(11), if sum is over 21, replace 11 by 1"""
    if sum(cards) == 21 and len(cards) == 2:  
        return 0               
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score, computer_cards):
    if user_score>21 :
        return "You went over 21. You Lose"
    elif computer_score==0:
        return "The computer has a blackjack. You Lose!"
    elif user_score==0:
        return "You have a blackjack. You win!"
    elif user_score==computer_score:
        return "It's a draw"
    elif computer_score > 21:   
        return "The computer went over 21. You win!"
    elif user_score>computer_score:
        return "You win!"
    else:
        return "You lose!"
    print(f"The computer's final hand: {computer_cards} , final score : {computer_score}")
    

def game():
    print(logo)
    user_cards = []
    computer_cards = []
    # deal the user and computer, 2 cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while is_game_over is False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current Score: {sum(user_cards)}")
        print(f"Computer's 1st card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0  or user_score >21:
            is_game_over =True
            print(f"Computer's final hand: {computer_cards} final_score: {computer_score}")
            print(compare(user_score,computer_score, computer_cards ))
        else:
            user_should_deal = input("Type 'y' to get another card , type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                is_game_over= False     
            else:
                # The computer should keep drawing cards as long as it has a score less than 17
                while computer_score !=0 and computer_score <17:
                    computer_cards.append(deal_card())
                    # The score will need to be rechecked with every new card drawn
                    computer_score = calculate_score(computer_cards)
            
                print(f"Your final hand:{user_cards} final score: {user_score} ")
                print(f"Computer's final hand: {computer_cards} final score: {computer_score}")
                print(compare(user_score,computer_score, computer_cards ))
                is_game_over=True

    play_game = input ("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    return play_game

        
# -----------------------------------------------------------------------------------------------------

play_game = input ("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

while play_game == "y":
    os.system("cls||clear")
    play_game = game()
   
if play_game != "y":
    print("Goodbye!")





