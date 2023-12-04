class Order:
    def __init__(self, type, person):
        self.type = type
        self.person = person

    def to_string(self):
        return f'{self.person} orders: {self.type}'

if __name__ == "__main__":
    order = Order('Coke', 'John')
    print(order.to_string())