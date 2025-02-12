#  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle 1 challenge Solution: 
# here turn_left() and move() are built-in functions in Game
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cross_obstacle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(0,6):
    cross_obstacle()

# is same as:
cross_obstacle()
cross_obstacle()
cross_obstacle()
cross_obstacle()
cross_obstacle()
cross_obstacle()

# Hurdle-2 challenge solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cross_obstacle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
   cross_obstacle() 


# Hurdle-3 challenge solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cross_obstacle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        cross_obstacle()

# Hurdle-4 challenge solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cross_obstacle():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        cross_obstacle()

# Maze Challenge Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()  
           
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()