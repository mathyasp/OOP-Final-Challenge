from person import Person
from order import Order
from coffee_bar import CoffeeBar
from barista import Barista


# Create three instances of the Person class
amy = Person('Amy', 'Coffee')
bob = Person('Bob', 'Tea')
cat = Person('Cat', 'Milk')


# Make an instance of a barista named Kevin. Kevin's greeting is "Hey dude!"
kevin = Barista('Kevin', greeting='Hey dude!')
print(kevin.greeting)


# Create an instance of CoffeeBar. Give your CoffeeBar a name.
mathyas_bar = CoffeeBar('Mathyas\' Bar', kevin)
print(f'Welcome to {mathyas_bar.name}!')


# Have each of your three customers (Amy, Bob, Cat)
# place an order with your coffee bar.
mathyas_bar.place_order(amy.my_order())
mathyas_bar.place_order(bob.my_order())
mathyas_bar.place_order(cat.my_order())


# Process all of the orders at your Coffeebar instance.
mathyas_bar.process_orders()



