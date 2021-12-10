# virtual coin toss

import random

guess = (input ("What is your guess? Head or tail?\n")).lower()

random_int = random.randint(0,1)

if random_int == 0:
    result = "head"
if random_int == 1:
    result = "tail"

if result == guess:
    print(f"The result is {result}, your guess is correct!")
else:
    print(f"The result is {result}, your guess is wrong!")