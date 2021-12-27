'''
Continuation of Hangman...

TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
Set 'lives' to equal 6.

TODO-2: - If guess is not a letter in the chosen_word,
Then reduce 'lives' by 1. 
If lives goes down to 0 then the game should stop and it should print "You lose."
Join all the elements in the list and turn it into a String.

TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display=[]
for letter in chosen_word:
    display += '_'
print(display)

lives =6 
while lives != 0:
    guess = input("Guess a letter: ").lower()
    index = 0
    letter_count =0
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter
            letter_count +=1     
        index += 1
    print(f"letter count: {letter_count}")
    print(display)

    if letter_count==0:          # this will check if a guess/letter is included in the word, 0 is incorrect , >0 is a correct guess
        print(stages[lives])
        lives-=1
        print(f"no. of lives: {lives}")

    if display.count('_')==0:    # this will check if all letters of the word are complete. If completed,  the player wins and program will exit the loop
        final_display =''
        for letter in display:
            final_display+=letter
        print(f"The word is: {final_display}")
        print("You win!")
        break
    
else:
    print(stages[0])
    print("You Lose!")
      

    

