'''
Banker Roulette

Write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

'''
import random
names_string = input("Give me everybody's names separated by a comma.\n")

names_list = names_string.split(",")

selected_index = random.randint(0, len(names_list)-1)    # take note of this len() 

selected_name = names_list[selected_index].title()  # title()- capitalize the first letter

print(f"{selected_name} will going to buy the meal today!")