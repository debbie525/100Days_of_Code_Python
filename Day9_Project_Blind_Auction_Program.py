'''
Create a Blind Auction Program

- Ask the user for name and bid amount. Store the information in a dictionary.
- Clear the terminal after a bidder inputs a bid.
- Determine the maximum bid.
- Print the winner (name and bid amount).

'''
import os
from Day9_Art  import logo

print(logo)
print("Welcome to Blind Auction!")

bids_info = {}
resume = True

while resume is True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    other_bidder = input("Are there any other bidder? Type 'yes' or 'no'.\n")
    bids_info[name] = int(bid)   # store the infos in a dictionary, key is "name" and value is bid amount
    if other_bidder != "yes":    # stop the loop if no more bidder
        resume = False
    else:
        os.system("cls||clear")  # if there are still bidders, clear the terminal

#print(bids_info)

max_bid = 0

# check the maximum bid in bids_info dictionary 
for key in bids_info:
    if bids_info[key] > max_bid:
        max_bid = bids_info[key]
        winner = key
    else:
        continue

print(f"The winner is {winner} with a bid of ${max_bid}.")

