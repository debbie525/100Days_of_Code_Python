'''
Write a program that will add even numbers  from 1 to 100 (inluding 1 and 100)

'''

total = 0

for number in range (1, 101):
    if number % 2 ==0:
        total += number
    else:
        continue
print(total)

#other solution
# total = 0 
# for number in range (2,101,2): # start=2, stop=101, step =2
#     total += number
# print(total)

