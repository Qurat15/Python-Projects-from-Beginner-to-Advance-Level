import random
# --------- Project : Who will pay the bill? -------------
# 1st method
friends = ['Ali', 'Amna','Bano','Malaika', 'Ayesha']
person_selected_to_pay_the_bill = (random.choice(friends))
print(f'{person_selected_to_pay_the_bill} will pay the bill today!')

#2nd method
person_selected_based_on_index = random.randint(0,4)
print(f'{friends[person_selected_based_on_index]} will pay the bill! Hurrayyyyy')