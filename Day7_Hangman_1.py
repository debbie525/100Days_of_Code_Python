

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

chosen_index = random.randint(0,2)
print(chosen_index)
chosen_word = word_list[chosen_index]
print(chosen_word)

print("--------------------------------------")
guess =input("Guess a letter:\n").lower()

print("-------------------------------------")
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")