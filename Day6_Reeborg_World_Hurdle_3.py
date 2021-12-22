'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

Reeborg has entered a hurdle race. Make him run the ccourse , following the path shown.
The position and the number of hurdles changes each time this world is reloaded.

'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

   
while at_goal() is not True: 
    if wall_in_front():
            turn_left()
            move()
            turn_right()
            move()
            turn_right()
            move()
            turn_left()
    while front_is_clear()==True and at_goal() is not True:
            move()

        

        
        
        
        
    

    

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
