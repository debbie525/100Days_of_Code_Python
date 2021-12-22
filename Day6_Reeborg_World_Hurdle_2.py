
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
'''
Reeborg has entered a hurdle race , but he does not know in advance how long the 
race is. Make him run the course, following a path similar to the one shown, but stopping
at the only flag that will be shown after the race has started. 

'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def first_move():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def jump():
    turn_left()
    first_move()
    
first_move()

while at_goal() is not True:
    jump()

