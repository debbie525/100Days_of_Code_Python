'''
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Reeborg was exploring a dark maze and the battery in its flashlight ran out.
Write a program using an if/elif/else statement so Reeborg can find the exit.
The secret is to have Reeborg follow along the right edge of the maze , turning right if it can ,
going straight ahead if it can't turn right, or turning left as a last resort.


'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
  
    
while at_goal() is not True:
    if right_is_clear() ==True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move() 
    elif wall_in_front() ==True and wall_on_right() == True:
        turn_left()
    elif wall_in_front() == True:
        turn_right()

   
       
        
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
