'''
Write a program that calculates the average student height from List of heights using for loop

'''

height_list = input ("Input a list of students heights, separated by comma:\n").split(",")

total_height = 0
counter = 0
for height in height_list:
    total_height += int(height)
    counter += 1

average_height = total_height/counter
round_average_height = round(average_height)


print(f"Average Height: {round_average_height}")