# Make your own "Choose Your Own Adventure" game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_stop = input("Where do you want to go? Choose 'Left' or 'Right':\n").lower()

if first_stop == "right":
    print("You fell into a hole. Game Over!")
elif first_stop == "left":
    second_stop = input("You've come into a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_stop == "swim":
        print("You get attacked by crocodiles. Game Over!")
    elif second_stop == "wait":
        third_stop = input("You arrive at the island unharmed.\nThere is a house with 3 doors. One red, one green and one blue.\nWhich colour do you choose?\n").lower()
        if third_stop == "red":
            print("You enter a room of beats. Game Over!")
        elif third_stop == "green":
            print("Its a room full of fire. Game Over!")
        elif third_stop == "blue":
            print("Congratulations! You found the treasure. You win!")
    

