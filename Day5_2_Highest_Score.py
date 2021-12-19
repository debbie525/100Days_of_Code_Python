'''
Write a program that calculates the highest score from a List of scores using "for loop"

Note: Do not use max() function

'''

score_list = input("Input a list of students scores, separated by comma:\n").split(',')
print(score_list)

max_number = 0

for score in score_list:
    if int(score) > max_number:
        max_number = int(score)
    
print(f"The highest score in the class is: {max_number}")