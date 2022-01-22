# Build a calculator (add, subract, multiply and divide)
# Ask the user for 1st number , 2nd number and operation
# print out the inputs, operation and answer
# Ask the user if will continue in calculation using the answer or start a new calculation
 

import os

first_number = int(input("What's the first number?: "))
operation = input("What's the operation?: ")
second_number = int(input("What's the second number?: "))


def calculate (n1, n2, operation):     
    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        result = n1 / n2
    return result

resume = True

while resume is True:
    answer = calculate(n1=first_number, n2= second_number, operation=operation)
    print(f"{first_number} {operation} {second_number} = {answer}")

    message = input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculationn or 'e' to exit: ")
    
    if message == 'n':
        os.system("cls||clear")
        first_number = int(input("What's the first number?: "))
        operation = input("What's the operation?: ")
        second_number = int(input("What's the second number?: "))
        resume = True

    elif message == 'y':
        first_number= answer
        operation = input("What's the operation?: ")
        second_number = int(input("What's the second number?: "))
    else:
        print("Thank you for using Python Calculator.Goodbye!")
        resume=False
        




 
   




