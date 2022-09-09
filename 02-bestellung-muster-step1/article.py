class Article:
    def __init__(self, name, price, id=None):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    def __str__(self):
        return f'{self.__name} á {self.__price}'

articles = []
while True:
    print("(1) Liste")
    print("(2) Hinzufügen")

    selection = input()
    if selection == '1':
        for element in articles:
            print(str(element))
    else:
        id = input('ID: ')
        name = input('Name: ')
        price = float(input('Price: '))
        article = Article(name, price, id)
        articles.append(article)

