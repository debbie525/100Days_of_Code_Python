
'''
continuation....

TODO-1: Import and print the logo from art.py when the program starts.

TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
Try running the program and entering a shift number of 45.
Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
Hint: Think about how you can use the modulus (%).

TODO-3: What happens if the user enters a number/symbol/space?
Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
e.g. start_text = "meet me at 3"
end_text = "•••• •• •• 3"

TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

'''

from Day8_Project_Art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

resume = True

while resume is True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # check the index of each letter in the word
    # create a new word using previous index position + shift
    def caesar(input_text, shift_amount, cipher_direction):
        word = ""
        for char in input_text:
            if char in alphabet:
                position = alphabet.index(char)
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                    if new_position > 25:
                        new_position = new_position % 26

                elif cipher_direction == "decode":
                    new_position = position - shift_amount
                    if new_position < 0:
                        new_position = new_position % 26

                item = alphabet[new_position]
            else:
                item = char

            word += item
        print(f"The {cipher_direction}d text is {word}")

    # call the function

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    message = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    if message == "yes":
        resume = True
    else:
        print("Goodbye!")
        resume = False




