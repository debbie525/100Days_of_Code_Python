'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

Reeborg has entered a hurdle race. Make him run the course, following the path shown.
The position, the height and the number of hurdles changes each time this world is reloaded.

'''



def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    while front_is_clear() is True:
        move()
    else:
        turn_left()
    
while at_goal() is not True:
    if wall_in_front() is True:
        turn_left()
        while right_is_clear() is not True:
            move()
        else:
            jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
