'''
Create a password generator depending on the number of characters (letters, numbers, symbols)
 the user requested

'''

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for letter in range (1, num_letters+1):
    selected_letter = random.choice(letters)
    password_list += selected_letter
    print(selected_letter)

for symbol in range (1, num_symbols+1):
    selected_symbol = random.choice(symbols)
    password_list += selected_symbol
    print(selected_symbol)

for number in range (1, num_numbers+1):
    selected_number = random.choice(numbers)
    password_list += selected_number
    print(selected_number)


password =''

for count in range(1, len(password_list)+1):
    selected_item = random.choice(password_list)
    password +=selected_item
    password_list.remove(selected_item)


print(f"Generated Password: {password}")
