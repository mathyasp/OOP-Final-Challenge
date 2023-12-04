from order import Order

class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):
        new_order = Order(self.favorite_drink, self.name)
        return new_order.to_string()

if __name__ == "__main__":
    amy = Person('Amy', 'Coffee')
    bob = Person('Bob', 'Tea')
    cat = Person('Cat', 'Milk')

    print(amy.my_order())
    print(bob.my_order())
    print(cat.my_order())