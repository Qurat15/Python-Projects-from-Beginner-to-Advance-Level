
#------------- Project - Tip Calculator ---------------
print('Welcome to the Tip Calculator!')
bill_selected = int(input('What was the total bill? '))
tip_selected = int(input('How much tip you want to add.10, 12 or 15%? '))
num_of_people = int(input('How many people to split the bill? '))

tip = tip_selected / 100
total_tip = tip * bill_selected
bill_to_be_paid = bill_selected + total_tip
total = bill_to_be_paid/num_of_people
final_amount = round(total,2)

print(f'Each person should pay: {final_amount}')

# total bill = 200/2 = 100 
# tip = 12% -> 12/100 = 0.12 so, 0.12*200