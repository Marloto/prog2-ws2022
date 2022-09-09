class Order:
    def __init__(self, nr, date = None, delivery = None):
        self.__date = date
        self.__delivery = delivery
        self.__number = nr

    def get_customer(self):
        return self.__customer

    def get_positions(self):
        return self.__positions

    def get_date(self):
        return self.__date

    def get_number(self):
        return self.__number

    def add_position(self, position):
        self.__positions.append(position)

    def __str__(self):
        return f'Order-Number: {self.__number}\nDate: {self.__date}\nDelivery: {str(self.__delivery)}'


orders = []
while True:
    print("(1) Liste")
    print("(2) Hinzufügen")

    selection = input()
    if selection == '1':
        for element in orders:
            print(str(element))
    else:
        date = input('Date: ')
        delivery = input('Delivery: ')
        nr = input('Number: ')
        order = Order(nr, date, delivery)
        orders.append(order)