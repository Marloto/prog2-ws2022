import csv

class Order:
    def __init__(self, nr, date = None, delivery = None):
        self.__date = date
        self.__delivery = delivery
        self.__number = nr

    def get_date(self):
        return self.__date

    def get_delivery(self):
        return self.__delivery

    def get_number(self):
        return self.__number

    def __str__(self):
        return f'Order-Number: {self.__number}\nDate: {self.__date}\nDelivery: {str(self.__delivery)}'

def save(values):
    with open("orders.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for value in values:
            writer.writerow([value.get_number(), value.get_date(), value.get_delivery()])

orders = []
try:
    with open("orders.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            orders.append(Order(row[0], row[1], row[2]))
except FileNotFoundError:
    pass

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
        save(orders)
