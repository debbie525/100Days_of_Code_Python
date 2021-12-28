'''
Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into 
it is a prime number or not.



'''



def prime_checker(number):
    for item in range (2, number):
        if number % item ==0:
            print("It's not a prime number")
            break
    else:
        print("It's a prime number")

n=int(input("Check this number: "))
prime_checker(number=n)