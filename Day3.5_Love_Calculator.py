'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

Example:

Input:
name1 = "Kanye West"
name2 = "Kim Kardashian"

Output:
Your score is 42, you are alright together.

'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

word_list = ["true", "love"]

first_digit = 0
second_digit = 0

for word in word_list:
    for letter in word:
        count_name1 = name1.lower().count(letter)
        count_name2 = name2.lower().count(letter)
        if word == "true":
            first_digit += count_name1
            first_digit += count_name2
        if word == "love":
            second_digit += count_name1
            second_digit += count_name2

percentage = int(str(first_digit) + str(second_digit))

if percentage <= 10 or percentage >= 90:
    print(f"Your score is {percentage}, you go together like coke and mentos.")

elif percentage >= 40 and percentage <= 50:
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")
    



