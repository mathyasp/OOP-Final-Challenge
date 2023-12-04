class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):
        return self.favorite_drink

if __name__ == "__main__":
    person = Person('John', 'Coke')
    print(person.my_order())