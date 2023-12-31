'''
This module defines the Person class.
'''


from order import Order


class Person:
    '''
    Represents a person with a name and favorite drink.
    '''
    def __init__(self, name, favorite_drink='', wallet=0.0, tip_amount=0.0):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip_amount = tip_amount


    def my_order(self):
        '''
        Creates a new Order class instance with the person's favorite drink and name,
        and returns the output of the to_string() method.
        '''
        new_order = Order(self.favorite_drink, self, tip_amount=self.tip_amount)
        return new_order
