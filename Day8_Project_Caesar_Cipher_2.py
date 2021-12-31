''''
Continuation....

TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet 
by the shift amount and print the decrypted text.  

TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
Then call the correct function based on that 'direction' variable. You should be able to test the code to 
encrypt *AND* decrypt a message.


'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# check the index of each letter in the word
# create a new word using previous index position + shift

def encrypt(plain_text, shift_amount):
    encrypted_word=""
    for item in plain_text:
        position= alphabet.index(item)
        position_shift = position + shift_amount
        if position_shift > 25:
            position_shift = position_shift - 26
        encrypted_letter = alphabet[position_shift]
        encrypted_word+= encrypted_letter
    print(f"The encoded text is {encrypted_word}")
    

def decrypt(cipher_text =text, shift_amount =shift):
    decrypted_word = ""
    for item in cipher_text:
        position = alphabet.index(item)
        position_shift = position - shift
        if position_shift < 0:
            position_shift = position_shift + 26
        decrypted_letter = alphabet[position_shift]
        decrypted_word += decrypted_letter
    print(f"The decoded text is {decrypted_word}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print (f'You typed a wrong direction: "{direction}" ')

    

