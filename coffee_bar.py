"""
This module defines the CoffeeBar class.
"""


from order import Order
from person import Person


class CoffeeBar:
    """
    Represents a coffee bar.

    Attributes:
        name (str): The name of the coffee bar.
        orders_list (list): A list of orders placed at the coffee bar.
    """


    def __init__(self, name):
        self.name = name
        self.orders_list = []


    def place_order(self, order):
        """
        Places an order at the coffee bar.

        Args:
            order (Order): The order to be placed.
        """
        self.orders_list.append(order)


    def process_orders(self):
        """
        Processes all the orders placed at the coffee bar.
        """
        for order in self.orders_list:
            print(order.to_string())


if __name__ == "__main__":
    mathyas_bar = CoffeeBar('Mathyas\' Bar')
    print(f'Welcome to {mathyas_bar.name}!')

    amy = Person('Amy', 'Coffee')
    bob = Person('Bob', 'Tea')
    cat = Person('Cat', 'Milk')

    mathyas_bar.place_order(amy.my_order())
    mathyas_bar.place_order(bob.my_order())
    mathyas_bar.place_order(cat.my_order())

    mathyas_bar.process_orders()