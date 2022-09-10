# class Tier:
#     def __init__(self):
#         pass
#     def makeSound(self):
#         """Has to implement some make sound method"""
#         pass
#
#
# class Hund(Tier):
#     def makeSound(self):
#         print("Sound!")
#
#
# someObj = Hund()
# someObj.makeSound()


class Figure:
    def __init__(self):
        pass

    def boundary(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def boundary(self):
        return self.a + self.b + self.c


class Square(Figure):
    def __init__(self, a):
        self.a = a
    def boundary(self):
        return self.a * 4



class WrongFigure(Figure):
    pass

def printBoundaries(figure : Figure):
    print(figure.boundary())


printBoundaries(Triangle(2, 4, 6))