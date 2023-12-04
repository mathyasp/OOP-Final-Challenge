'''
This module contains the main code for the OOP Final Challenge.
'''
from person import Person
from coffeebar import CoffeeBar
from barista import Barista


# Create three instances of the Person class
amy = Person('Amy', 'Coffee', wallet=10, tip_amount=0.20)
bob = Person('Bob', 'Tea', wallet=15, tip_amount=0.18)
cat = Person('Cat', 'Milk', wallet=5, tip_amount=0.15)


# Make an instance of a barista named Kevin. Kevin's greeting is 'Hey dude!'
kevin = Barista('Kevin', greeting='Hey dude!')
print(kevin.greeting)


# Create an instance of CoffeeBar. Give your CoffeeBar a name.
mathyas_bar = CoffeeBar('Mathyas\' Bar', kevin)
print(f'Welcome to {mathyas_bar.name}!')
print('\n-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n')


# Print statements to show initial wallet amount for each person.
print(f'{amy.name} has ${amy.wallet:.2f} in their wallet.')
print(f'{bob.name} has ${bob.wallet:.2f} in their wallet.')
print(f'{cat.name} has ${cat.wallet:.2f} in their wallet.')


# Have each of your three customers (Amy, Bob, Cat)
# place an order with your coffee bar.
mathyas_bar.place_order(amy.my_order())
mathyas_bar.place_order(bob.my_order())
mathyas_bar.place_order(cat.my_order())


# Show the initial balance of the coffee bar's register.
mathyas_bar.cash_out()


# Process all of the orders at your Coffeebar instance.
mathyas_bar.process_orders()


# Show the receipts for each order.
mathyas_bar.audit()


# Show the final balance of the coffee bar's register.
mathyas_bar.cash_out()


# Show how much Kevin made in tips.
print(f'Kevin made ${kevin.wallet} in tips today.')
