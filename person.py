from order import Order

class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):
        new_order = Order(self.favorite_drink, self.name)
        return new_order.to_string()

if __name__ == "__main__":
    person = Person('John', 'Coke')
    print(person.my_order())