'''
This module defines the Order class.
'''

class Order:
    '''
    Represents an order made by a person.
    '''

    def __init__(self, order_type, person, price=0.0, tip_amount=0.0):
        '''
        Initializes a new Order instance.

        Args:
            order_type (str): The type of the order.
            person (str): The person who placed the order.
        '''
        self.order_type = order_type
        self.person = person
        self.price = price
        self.tip_amount = tip_amount

    def to_string(self):
        '''
        Returns a string representation of the order.

        Returns:
            str: The string representation of the order.
        '''
        tip = self.price * self.tip_amount
        total = self.price + tip

        return f'{self.person.name} orders: {self.order_type}\nPrice: ${self.price:.2f}, Tip: ${tip:.2f}, Total: ${total:.2f}'
