#Continuation ,part 3

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word 
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.


import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display=[]
for letter in chosen_word:
    display += '_'
print(display)

while display.count('_') != 0:
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
        index += 1
    print(display)

print("You win!")






