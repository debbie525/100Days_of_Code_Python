'''
You are going to write a program which will mark a spot with an X.

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']

'''

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


'''
example:
position = "23"

column =2  # y
row = 3    # x


'''

y = int(position[0])  # column
x = int(position[1])  # row

# always remember that index of lists always start at 0
selected_row = map[x-1]
selected_row[y-1] = "X"    

print(f"{row1}\n{row2}\n{row3}")