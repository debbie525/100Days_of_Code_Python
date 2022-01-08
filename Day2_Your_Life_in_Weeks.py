
# Day 2-3 Exercise

# date: December 5, 2021

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months



age = input("What is your current age?")

final_age_day = 90*365
final_age_week = 90*52
final_age_month = 90*12

remaining_day = final_age_day - (int(age)*365)
remaining_week = final_age_week - (int(age)*52)
remaining_month = final_age_month - (int(age)*12)

print (f"You have {remaining_day} days, {remaining_week} weeks, and {remaining_month} months left")
