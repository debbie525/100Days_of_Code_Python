# Create a  calculator using functions and dictionary
# Build a calculator (add, subract, multiply and divide)
# Ask the user for 1st number , 2nd number and operation
# print out the inputs, operation and answer
# Ask the user if will continue in calculation using the answer or start a new calculation
# If the user wants to start a new calculation,clear the terminal 


import os 
from Day10_Art import logo

def add(n1, n2):
     return n1+n2

def subract(n1, n2):
     return n1-n2

def multiply(n1, n2):
     return n1*n2

def divide(n1, n2):
     return n1/n2

operations ={
    "+": add,
    "-": subract,
    "*": multiply,
    "/": divide }

def calculate():
     print(logo)
     resume =True
     num1 = float(input("What's the first number?: "))
     for symbol in operations:
          print(symbol)

     while resume is True:
          symbol = input("Please pick an operation: ")
          num2 = float(input("What's the next number?: "))
          answer = operations[symbol](num1,num2)      # operation[symbol] represent the function for add/subract/multiply/divide from "operations" dict
          print (f"{num1} {symbol} {num2} = {answer}")
          message = input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculation: ").lower()

          if message =="y":
               num1 = answer
               resume= True
          elif message =="n":
               os.system("cls||clear")
               calculate()                                  # recursion, call the function itself
          else:
               print("Thank you for using Python Calculator.Goodbye!")
               break
               
     

# call the function
calculate()

