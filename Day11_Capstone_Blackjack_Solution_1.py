
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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import os
from Day11_Art import logo

def draw_number():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    number=random.choice(cards)
    return number

def sum_cards(list_of_number):
    result = sum(list_of_number)
    print(f"Your cards: {list_of_number}, current_score: {result}")
    return result

def compare(dealer_cards, user_result, dealer_result):
    print(f"Computer Cards: {dealer_cards}, computer_score: {dealer_result} ")
    if user_result > dealer_result:
        print("You win!")
    elif user_result==dealer_result:
        print("It's a draw!")
    else:
        print("You lose!")
    resume = False

def ask_user():
    return input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def check_if_blackjack(dealer_cards, list_of_number, dealer_result,user_result):
    if dealer_result==21:
        if dealer_cards[0]==11 or dealer_cards[1]==11:
            print(f"Computer Cards: {dealer_cards}, computer_score: {dealer_result} ")
            print("The dealer have a blackjack.You lose!")
            blackjack ='y'
            return blackjack
       
    elif user_result==21:
        if list_of_number[0]==11 or list_of_number[1]==11:
         
            print ("You have a blackjack. You win!")
            blackjack = 'y'
            return blackjack
        
    

def procedure(resume, n1, dealer_cards, dealer_result, counter): 
    next_num = draw_number()
    user_cards.append(next_num)
    user_result=sum_cards(user_cards)              
    
    while counter <1:
        if check_if_blackjack(dealer_cards, user_cards, dealer_result,user_result) == 'y':
            resume =False
            message = "n"
        counter +=1
    
    while resume is True:
        if 11 in user_cards and sum(user_cards)>21:
            user_cards.remove(11)
            user_cards.append(1)
            print(f"You have an ace in your cards\nYou're new cards are {user_cards}")
        
        elif user_result >21:
            resume = False
            message = 'n'
            print("You went over 21. You Lose")
            break
               
        message = input("Type 'y' to draw another card, type 'n' to pass: ").lower()

        if message == 'y':
            resume = True
            n1=user_result
            procedure(resume,n1, dealer_cards, dealer_result, counter)
            break
            
        elif message == 'n':
            while dealer_result<17:
                next_num = draw_number()
                dealer_cards.append(next_num)
                dealer_result += next_num
                if dealer_result >21:
                    resume = False
                    message = 'n'
                    print(f"Dealer's Cards: {dealer_cards}")
                    print("The dealer went over 21. You win!")
                    break

            else:    
                resume= False
                compare(dealer_cards,user_result,dealer_result)
                break
                    
           
        else:
            resume =False
            break
           
            
                
# --------------------------------------------------------------------------
print(logo)
want_to_play = ask_user()
resume = True

while want_to_play=='y':
    dealer_num1 = draw_number()
    dealer_num2 = draw_number()
    dealer_cards =[dealer_num1,dealer_num2]
    dealer_result = dealer_num1 + dealer_num2
    user_cards = []
    num1 = draw_number()
    user_cards.append(num1)
    counter =0
    procedure(resume, num1, dealer_cards,dealer_result, counter)               
    want_to_play = ask_user()
    if want_to_play=="y":
        os.system("cls||clear")
    
else:
    print("Goodbye!")