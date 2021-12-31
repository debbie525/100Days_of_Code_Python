'''
Continuation...

TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# check the index of each letter in the word
# create a new word using previous index position + shift
def caesar(input_text, shift_amount, cipher_direction):
    word = ""
    for item in input_text:
        position = alphabet.index(item)
        if cipher_direction == "encode":
            position_shift = position + shift_amount
            if position_shift > 25:
                position_shift = position_shift - 26
        elif cipher_direction == "decode":
            position_shift = position - shift_amount
            if position_shift < 0:
                position_shift = position_shift + 26
        letter = alphabet[position_shift]
        word += letter
    print(f"The {cipher_direction}d text is {word}")

# call the function
caesar(input_text=text, shift_amount=shift, cipher_direction=direction)    

