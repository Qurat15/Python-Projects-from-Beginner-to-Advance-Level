
# Project : Pizza Order ------------------------
print('Welcome to Python Pizza Deliveries!')
pizza_size = input('What size of pizza you want: S, M or L? ')
want_pepparoni = input('Do you want pepporani on your pizza. Type Y or N. ')
extra_cheese = input('Do you want extra cheese. Type Y or N. ')

if pizza_size == 'S':
    price = 15
    if want_pepparoni == 'Y':
        price = price + 2
elif pizza_size == 'M':
    price = 20
    if want_pepparoni == 'Y':
        price = price + 3
elif pizza_size == 'L':
    price = 25
    if want_pepparoni == 'Y':
        price = price + 3

if extra_cheese == 'Y':
    price = price + 1

print(f'You will pay ${price}.')

