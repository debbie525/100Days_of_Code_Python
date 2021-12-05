'''
Create a tip calculator that would calculate the share of each person including the tip
Final answer should be rounded off into 2 decimal places
'''

print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
num_people = input("How many people to split the bill?")

share = round((float(total_bill) * (1 +(float(tip)/100)))/int(num_people),2)

print(f"Each person should pay: ${share}")