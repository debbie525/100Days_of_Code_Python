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

end_of_game = False
lives = 6 

while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    index = 0
    for letter in chosen_word:
        if letter == guess:
            display[index] = letter    
        index += 1
    print(display)

    if guess not in chosen_word:         # this will check if a guess/letter is included in the word, 0 is incorrect , >0 is a correct guess
        lives-=1
        print(f"no. of lives: {lives}")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    if display.count('_') == 0:    # this will check if all letters of the word are complete. If completed,  the player wins and program will exit the loop
        end_of_game = True
        final_display =''
        for letter in display:
            final_display += letter
        print(f"The word is: {final_display}")
        print("You win!")
        
    
    
      

    

