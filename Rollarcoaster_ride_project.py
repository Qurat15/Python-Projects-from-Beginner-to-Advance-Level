# -------- Project : Sell Tickets for Rollarcoaster Ride --------------------
height = int(input('Enter your height: '))
age = int(input('Enter your age: '))
want_photo = input('Do you want to get photo. Type"Yes" or "No".')
if height >= 120:
    print('You can ride rollarcoaster.')
    if age > 18:
        price = 12
        # print(f'Please pay ${price}')
    
    elif age >= 12 and age <= 18:
        price = 7
        # print(f'Please pay ${price}.')

    elif age < 12:
        price = 5
        # print(f'Please pay ${price}.')

    if want_photo == 'Yes':
        total_price = price + 3
        print(f'You will pay ${total_price}')

    elif want_photo == 'No':
        print(f'You will pay ${price}.')
    
else:
    print('Sorry, you have to grow taller to take a ride!')
