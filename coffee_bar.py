"""
This module defines the CoffeeBar class.
"""


class CoffeeBar:
    """
    Represents a coffee bar.

    Attributes:
        name (str): The name of the coffee bar.
        orders_list (list): A list of orders placed at the coffee bar.
    """


    def __init__(self, name, barista):
        self.name = name
        self.barista = barista
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
            print(self.barista.greeting, order.to_string())
