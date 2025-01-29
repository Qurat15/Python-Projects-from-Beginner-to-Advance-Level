

print('Welcome to Treasure Island.\n')
print('Your goal is to find treasure.\n')
print('Once upon a time, a young adventurer named Alex set out on a journey to find a hidden treasure on Treasure Island. Armed with a map, Alex was ready to explore.')
print('Start.................')
left_or_right = input('You stand at the edge of a dark forest. There are two paths in front of you: one to the left and one to the right.Type L for left and R for right.')
if left_or_right == 'R':
    print('You fall in a pit. Game Over!')
elif left_or_right == 'L':
    sit_in_boat = input('Now, you are near water with boats. Do you want to sit in boat. Type Y for yes and N for No.')
    if sit_in_boat == 'Y':
        print('You sit in broken boat. Game Over!')
    elif sit_in_boat == 'N':
        print('You had find tresure near water. Hohoo')