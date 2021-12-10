'''
You are going to write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

'''
import random
names_string = input("Give me everybody's names separated by a comma.\n")

names_list = names_string.split(",")

print(names_list)

selected_index = random.randint(0, len(names_list))

selected_name = names_list[selected_index].title()  # use title to capitalize the first letter

print(f"{selected_name} will going to buy the meal today!")