# Build a calculator (add, subract, multiply and divide)
# Ask the user for 1st number , 2nd number and operation
# print out the inputs, operation and answer
# Ask the user if will continue in calculation using the answer or start a new calculation

import os

operation_list = ["+", "-", "*", "/"]
def user_input():
    inputs = {}
    first_number = int(input("What's the first number?: "))
    operation = input("What's the operation?: ")
    second_number = int(input("What's the second number?: "))
    inputs[operation] = [first_number, second_number]
    return inputs


def add(n1,n2):
    return n1 +n2
def subract (n1,n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2

#print(inputs)

resume = True
console_clear = True

while resume is True:
    if console_clear == True:
        inputs = user_input()

    for key in inputs:
        first_number = inputs[key][0]
        second_number = inputs[key][1]
        if key == "+":
            answer = add(first_number,second_number)
        elif key == "-":
            answer = subract(first_number, second_number)
        elif key == "*":
            answer = multiply(first_number, second_number)
        elif key == "/":
            answer = divide(first_number, second_number)
        else:
            print("Invalid operation. Try again.")
            break
        
          
        print(f"{first_number} {key} {second_number} = {answer}")

        message = input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculationn or 'e' to exit: ")

        if message == "n":
            os.system("cls||clear")
            console_clear = True
        elif message == 'y':
            console_clear = False
            inputs={}
            operation = input("What's the operation?: ")
            if operation not in operation_list:
                print("Invalid operation. Try again.")
                console_clear=True
                break
            second_number = int(input("What's the second number?: "))
            inputs[operation] = [answer, second_number]
        else:
            print("Thank you for using Python Calculator.Goodbye!")
            resume = False


    






        

 
   




