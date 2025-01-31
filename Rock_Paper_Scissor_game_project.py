import random
print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.') 
# For user: 0,0  1,1  2,2  0,1  0,2  1,2  2,1  2,0  1,0
# For computer: 0,0  1,1  2,2  0,1  0,2  1,2  2,1  2,0  1,0
user_choice = int(input('What number do you want to choose? '))
computer_choice = random.randint(0,2)

# Algorithm:
'''
if userenter = 0, and computerenter = 1 -> rock wrap the paper. computer won!
if userenter = 0, and computerenter = 2 -> rock broke the scissor. you won!
if userenter = 1, and computerenter = 0 -> rock wrap the paper. you won!
if userenter = 2, and computerenter = 0 -> rock broke the scissor. computer won!

if userenter = 1, and computerenter = 2 -> scissor cuts the paper. computer won!
if userenter = 2, and computerenter = 1 -> scissor cuts the paper. you won!

if userenter = 0, and computerenter = 0 -> Game Draw!
if userenter = 1, and computerenter = 1 -> Game Draw!
if userenter = 2, and computerenter = 2 -> Game Draw!

'''

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Code Logic

if user_choice == 0:
    print(rock)
    if computer_choice == 1: 
        print('Computer choose: 1')
        print(paper)
        print('rock wrap the paper. computer won!')
    
    elif computer_choice == 2: 
        print('Computer choose: 2')
        print(scissor)
        print('rock broke the scissor. you won!')
    
    elif computer_choice == 0: 
        print('Computer choose: 0')
        print(rock)
        print('Game Draw!')
    

    

elif user_choice == 1:
    print(paper)
    if computer_choice == 0:
        print('Computer choose: 0')
        print(rock)
        print('rock wrap the paper. you won!')
    
    elif computer_choice == 1: 
        print('Computer choose: 1')
        print(paper)
        print('Game Draw!')
    
    elif computer_choice == 2:
        print('Computer choose: 2')
        print(scissor)
        print('scissor cuts the paper. computer won!')


elif user_choice == 2:
    print(scissor)
    if computer_choice == 0:
        print('Computer choose: 0')
        print(rock)
        print('rock broke the scissor. computer won!')

    elif computer_choice == 1:
        print('Computer choose: 1')
        print(paper)
        print('scissor cuts the paper. you won!')

    elif computer_choice == 2: 
        print('Computer choose: 2')
        print(scissor)
        print('Game Draw!')

else: 
    print('Wrong number entered!')




