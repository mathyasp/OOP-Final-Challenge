"""
This module defines the Order class.
"""

class Order:
    """
    Represents an order made by a person.
    """

    def __init__(self, order_type, person):
        """
        Initializes a new Order instance.

        Args:
            order_type (str): The type of the order.
            person (str): The person who placed the order.
        """
        self.order_type = order_type
        self.person = person

    def to_string(self):
        """
        Returns a string representation of the order.

        Returns:
            str: The string representation of the order.
        """
        return f'{self.person} orders: {self.order_type}'
