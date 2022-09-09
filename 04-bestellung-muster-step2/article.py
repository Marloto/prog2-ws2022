import csv

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

def save(values):
    with open("articles.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for value in values:
            writer.writerow([value.get_id(), value.get_name(), value.get_price()])

articles = []
try:
    with open("articles.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            articles.append(Article(row[1], row[2], row[0]))
except FileNotFoundError:
    pass

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
        save(articles)

