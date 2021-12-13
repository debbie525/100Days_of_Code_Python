"""
Make a rock, paper and scissors game.

Rules:

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.


"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def selected(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)

your_choice = int(input("What do you choose?\nType 0 for rock, 1 for paper or 2 for scissors.\n"))
selected(your_choice)

computer_choice = random.randint(0,2)
print("Computer chose:")
selected(computer_choice)


if your_choice == 0 and computer_choice ==2:    # rock vs. scissors
    print("You win!")
elif your_choice == 2 and computer_choice ==1:  # scissors vs. paper
    print("You win!")
elif your_choice ==1 and computer_choice ==0:   # paper vs. rock
    print("You win!")
elif your_choice==computer_choice:
    print("Same , it's a draw")
elif your_choice >2:
    print( "Invalid number, you lose!")
else: 
    print("You lose!")

