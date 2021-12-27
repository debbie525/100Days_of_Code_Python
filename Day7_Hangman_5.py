
'''
Continuation of Hangman...
Improving the user experience

TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
Delete this line: word_list = ["ardvark", "baboon", "camel"]

#TODO-2: - Import the stages from hangman_art.py

TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

TODO-4: - If the user has entered a letter they've already guessed, 
print the letter and let them know.


'''
import random
from Day7_hangman_words import hangman_words
from Day7_hangman_art import hangman_art, logo

logo()

stages_life = hangman_art()

chosen_word = random.choice(hangman_words())

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display=[]
for letter in chosen_word:
    display += '_'
print(display)

end_of_game = False
lives = 6 

while end_of_game == False:
    # guess a letter
    guess = input("Guess a letter: ").lower()
    if guess in display:            # check if guess is repeated
            print(f"You already guess this letter: {guess}")

     # this will check if a guess/letter is included in the word. If wrong guess, decrease the number of lives
    index = 0
    for letter in chosen_word:     
        if letter == guess:
            display[index] = letter    
        index += 1    
    print(display)


    if guess not in chosen_word:         
        lives-=1
        print(f'Letter "{guess}" is not included in the mystery word. You lose a life.')
        print(f"remaining no. of lives: {lives}")
        print(stages_life[lives])
        if lives == 0:
            end_of_game = True
            print(f'The mystery word is "{chosen_word}".')
            print("You Lose!")

    # this will check if all letters of the word are complete. If completed,  the player wins and program will exit the loop
    if display.count('_') == 0:    
        end_of_game = True
        final_display =''
        for letter in display:
            final_display += letter
        print(f"The word is: {final_display}")
        print("You win!")

    
        
    
    
      

    

