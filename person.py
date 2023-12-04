"""
This module defines the Person class.
"""


from order import Order


class Person:
    """
    Represents a person with a name and favorite drink.
    """

    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink


    def my_order(self):
        """
        Creates a new Order class instance with the person's favorite drink and name,
        and returns the output of the to_string() method.
        """
        new_order = Order(self.favorite_drink, self.name)
        return new_order


if __name__ == "__main__":
    amy = Person('Amy', 'Coffee')
    bob = Person('Bob', 'Tea')
    cat = Person('Cat', 'Milk')

    print(amy.my_order())
    print(bob.my_order())
    print(cat.my_order())
