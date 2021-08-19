import pyinputplus


prices = {'wheat': 0.5, 'white': 0, 'sourdough': 1, 'chicken': 2, 'turkey': 2.5, 'ham': 3, 'tofu': 2, 'cheddar': 0.5, 'swiss': 2, 'mozzarella': 1, 'mayo': 0.5, 'mustard': 0.5, 'lettuce': 1, 'tomato': 1}
price = 0

print('Hello, welcome to the Sandwich Maker program. Please follow instructions.')

print('Please select your bread')
bread = pyinputplus.inputMenu(['wheat', 'white', 'sourdough'])
price += prices[bread]
print(f'£{price}')

print('Please select your protein ')
protein = pyinputplus.inputMenu(['chicken','turkey', 'ham', 'tofu'])
price += prices[protein]
print(f'£{price}')


prompt = ('Do you want cheese? ')
cheese = pyinputplus.inputYesNo(prompt)

if cheese == 'yes' or cheese == 'Yes':
    cheese_type = pyinputplus.inputMenu(['cheddar','swiss','mozzarella'])
    price += prices[cheese_type]
print(f'£{price}')

mayo = pyinputplus.inputYesNo('Do you want mayo? ')
if mayo == 'Yes' or mayo == 'yes':
    price += prices['mustard']
print(f'£{price}')

mustard = pyinputplus.inputYesNo('Do you want mustard? ')
if mustard == 'Yes' or mustard == 'yes':
    price += prices['mustard']
print(f'£{price}')

lettuce = pyinputplus.inputYesNo('Do you want lettuce? ')
if lettuce == 'Yes' or lettuce == 'yes':
    price += prices['lettuce']
print(f'£{price}')

tomato = pyinputplus.inputYesNo('Do you want tomato? ')
if tomato == 'Yes' or tomato == 'yes':
    price += prices['tomato']
print(f'£{price}')

amount_prompt = 'How many sandwiches do you want? '
amount = pyinputplus.inputInt(amount_prompt)
price = price * amount
print(f'Your total comes to: £{price}')
