class Customer:
    def __init__(self, name, street, zipcode, town):
        self.__name = name
        self.__street = street
        self.__zipcode = zipcode
        self.__town = town

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_street(self):
        return self.__street

    def set_street(self, value):
        self.__street = value

    def get_zipcode(self):
        return self.__zipcode

    def set_zipcode(self, value):
        self.__zipcode = value

    def get_town(self):
        return self.__town

    def set_town(self, value):
        self.__town = value

    def __str__(self):
        return f'{self.__name}, {self.__street}, {self.__zipcode} {self.__town}'



customers = []
while True:
    print("(1) Liste")
    print("(2) Hinzufügen")

    selection = input()
    if selection == '1':
        for element in customers:
            print(str(element))
    else:
        name = input('Name: ')
        street = input('Street: ')
        zipcode = input('Zipcode: ')
        town = input('Town: ')
        customer = Customer(name, street, zipcode, town)
        customers.append(customer)