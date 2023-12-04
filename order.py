from person import Person

class Order:
    def __init__(self, type, person):
        self.type = type
        self.person = person

    def to_string(self):
        return f'{self.person.name} orders: {self.type}'

if __name__ == "__main__":
    order = Order('Coke', Person('John', 'Coke'))
    print(order.to_string())