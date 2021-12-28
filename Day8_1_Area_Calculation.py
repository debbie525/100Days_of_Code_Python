'''
You are painting a wall. The instructions on the paint can says that 1 can of paint 
can cover 5 square meters of wall. Given a random height and width of wall, 
calculate how many cans of paint you'll need to buy.

Calculation:
number of cans = (wall height ✖️ wall width) ÷ coverage per can.

'''

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height=test_h, width=test_w, cover=coverage):
    num_cans =(height*width)/coverage
    # round off to nearest whole number (up)
    if num_cans%int(num_cans)>0:
        num_cans = int(num_cans)+1
    else:
        num_cans= int(num_cans)
    print(f"You'll need {num_cans} cans of paint")

paint_calc()

