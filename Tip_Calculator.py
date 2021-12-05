'''
Create a tip calculator that would calculate the share of each person including the tip
Final answer should be rounded off into 2 decimal places
'''

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))

total_tip_amount = bill * (tip/100)
total_bill = bill + total_tip_amount
share_per_person = round((total_bill/num_people),2)  # round off into 2 decimal places

print(f"Each person should pay: ${share_per_person}")