import pyinputplus

prices = {'wheat': 0.5, 'white': 0, 'sourdough': 1, 'chicken': 2, 'turkey': 2.5, 'ham': 3, 'tofu': 2, 'cheddar': 0.5, 'swiss': 2, 'mozzarella': 1, 'mayo': 0.5, 'mustard': 0.5, 'lettuce': 1, 'tomato': 1}
price = 0

print('Hello, welcome to the Sandwich Maker program. Please follow instructions.')

def bread(money, prices):
    print('Please select your bread')
    bread = pyinputplus.inputMenu(['wheat', 'white', 'sourdough'])
    money += prices[bread]
    return money

price = bread(price, prices)
print(price)
    
def protein(price, prices):
    print('Please select your protein ')
    protein = pyinputplus.inputMenu(['chicken','turkey', 'ham', 'tofu'])
    price += prices[protein]
    return price

price = protein(price, prices)
print(f'£{price}')

def cheese(price, prices):
    
    prompt = 'Do you want cheese? '
    cheese = pyinputplus.inputYesNo(prompt)
    if cheese.lower() == 'yes':
        cheese_type = pyinputplus.inputMenu(['cheddar','swiss','mozzarella'])
        price += prices[cheese_type]
        return price

price = cheese(price, prices)        
print(f'£{price}')

def condiments(price, prices):
    
    mayo = pyinputplus.inputYesNo('Do you want mayo? ')
    if mayo.lower() == 'yes':
        price += prices['mustard']
    print(f'£{price}')
    
    mustard = pyinputplus.inputYesNo('Do you want mustard? ')
    if mustard.lower() == 'yes':
        price += prices['mustard']
    print(f'£{price}')

    lettuce = pyinputplus.inputYesNo('Do you want lettuce? ')
    if lettuce.lower() == 'yes':
        price += prices['lettuce']
    
    print(f'£{price}')

    tomato = pyinputplus.inputYesNo('Do you want tomato? ')
    if tomato.lower() == 'yes':
        price += prices['tomato']
    print(f'£{price}')
    return price

price = condiments(price,prices)

amount = pyinputplus.inputInt('How many sandwiches would you like? ')
price = price * amount
print(f'Your total comes to: £{price}')
