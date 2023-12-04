'''
This module defines the Barista class.
'''


from person import Person


class Barista(Person):
    '''
    Represents a barista.

    Attributes:
        name (str): The name of the barista.
    '''
    def __init__(self, name, greeting, favorite_drink=''):
        super().__init__(name, favorite_drink)
        self.greeting = greeting
