'''
This module defines the CoffeeBar class.
'''


class CoffeeBar:
    '''
    Represents a coffee bar.

    Attributes:
        name (str): The name of the coffee bar.
        orders_list (list): A list of orders placed at the coffee bar.
    '''

    def __init__(self, name, barista):
        self.name = name
        self.barista = barista
        self.register = 0.0
        self.orders_list = []
        self.receipts = []
        self.tip_jar = 0.0

    def place_order(self, order):
        '''
        Places an order at the coffee bar.

        Args:
            order (Order): The order to be placed.
        '''
        if order.order_type == 'Coffee':
            order.price = 1.50
        elif order.order_type == 'Tea':
            order.price = 1.00
        elif order.order_type == 'Milk':
            order.price = 0.50

        self.orders_list.append(order)

    def process_orders(self):
        '''
        Processes all the orders placed at the coffee bar.
        '''
        for order in self.orders_list.copy():
            total = order.price + (order.price * order.tip_amount)
            order.person.wallet -= total
            self.register += order.price
            self.tip_jar += order.tip_amount
            self.receipts.append(order)
            self.orders_list.remove(order)
            message = (
                f'{self.barista.greeting} {order.to_string()}\n'
                f'{order.person.name} now has ${order.person.wallet:.2f} in their wallet.\n'
            )
            print(message)
        self.barista.wallet += self.tip_jar
        self.tip_jar = 0.0

    def cash_out(self):
        '''
        Prints the total amount of money in the coffee bar's register.
        '''
        print(f'\nThe register has ${self.register:.2f} in it.\n')

    def audit(self):
        '''
        Prints the receipts.
        '''
        print('\n-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n')
        print('Receipts:\n')
        for receipt in self.receipts:
            print(receipt.to_string() + '\n')
        print('-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n')
