# Typen
a = 1
print(type(a))

a = "Test"
print(type(a))


# Funktionen
def something(a):
    a = a + 1
    return a

aa = 1
something(aa) # Call-by-Copy
print(aa) # Ausgabe ist 1

ab = 1
ab = something(ab)
print(ab) # Ausgabe ist 2

print("----")
# Rekursion
# def beispiel():
#     beispiel()

# beispiel() # maximum recursion depth exceeded

# 0 1 1 2 3 5 8 13
# fibu(0) = 0
# fibu(1) = 1
# fibu(2) = fibu(0) + fibu(1) = 1
# fibu(3) = fibu(1) + fibu(2) = 2
# fibu(4) = fibu(2) + fibu(3) = 3
def fibu(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibu(n - 2) + fibu(n - 1)

print(fibu(0))
print(fibu(1))
print(fibu(2))
print(fibu(3))
print(fibu(4))

print("---")

# Datenstruktur
someList2 = [1, 2, 3] # erzeugen einer Liste mit drei Elementen
print(someList2[0]) # würde 1 ausgeben
someList2[0] = 42
print(someList2[0]) # würde 42 ausgeben
print("List:")
for i in someList2:
    print(i)
anzahlDerElemente = len(someList2) # Zugriff auf Anzahl
print(f'Laenge: {anzahlDerElemente}')

# Iteration mit while
i = 0
while i < len(someList2):
    print(someList2[i])
    i = i + 1

# Dicts -> hashtable
print('---Dict')
someDict = {"Test": 123, "Anderes": "Zeichenkette"} # Erzeugung mit Vorbelegung
print(someDict)
print(someDict["Test"])
print(someDict["Anderes"])
someDict["Mehr"] = 432
print(someDict)
for key in someDict:
    print(f'{key}: {someDict[key]}')


print(type(someDict))
print(someDict.values())
for value in someDict.values():
    print(value)
for key, value in someDict.items():
    print(f'{key}: {value}')


print('---Set')
someSet = {"Test", "Anderes", "Mehr", "Mehr"}
someSet2 = set(["Test", "Anderes", "Mehr"])
someSet3 = ({"Test", "Anderes", "Mehr"})
# someSet["Test"] = 1 sowas geht nicht :)

print(type(someSet))
print(type(someSet2))
print(type(someSet3))
for key in someSet:
    print(key)

# Klassen
class SomeClass:
    #__slots__ = ['someAttr']
    def __init__(self):
        self.someAttr = 123
    def someMethod(self):
        print(f'Hello {self.someAttr}')

someObj1 = SomeClass()
someObj1.someAttr = 42
someObj2 = SomeClass()
someObj2.someAttr = 21

print(someObj1.someAttr)
print(someObj2.someAttr)
someObj1.someMethod()
someObj2.someMethod()

someObj1.otherAttr = 21
#print(someObj1["otherAttr"]) so nicht, das geht nicht direkt
#print(someObj1["someAttr"])
print(someObj1.__dict__['someAttr'])
print(someObj1.__dict__['otherAttr'])

class SomeImmutable: # im sinne seiner Attribute -> Attribut-Werte sind änderbar
    __slots__ = ['example']
    def __init__(self):
        self.example = 3

someObj3 = SomeImmutable()
# someObj3.other = 32
someObj3.example = 42
print(someObj3.example)

class SomeRefExample:
    def __init__(self):
        self.example = 3

someObj4 = SomeRefExample()
someObj5 = someObj4

someObj4.example = 42
someObj5.example = 21

print(someObj4.example)
print(someObj5.example)

def someMethod(classRef):
    classRef.example = 100
someMethod(someObj4)
print(someObj4.example)

class SomeStrExample:
    def __init__(self):
        self.example = 3
        self.other = 42
    def __str__(self):
        return f'Example: {self.example}'
    def __eq__(self, other):
        return self.example == other.example and self.other == other.other

someObj6 = SomeStrExample()
# someObj6.other = 1
someObj7 = SomeStrExample()
# someObj7.other = 2
print(str(someObj6))

if someObj6 == someObj7:
    print("Ist identisch!")
else:
    print("Ist nicht identisch!")

# Aggregationsbeispiel

class Auto:
    def __init__(self):
        self.reifen = [Reifen(), Reifen(), Reifen(), Reifen()]
        self.lenkrad = Lenkrad()

class Reifen:
    def __init__(self):
        pass

class Lenkrad:
    def __init__(self):
        pass

auto1 = Auto()

class Tier:
    def __init__(self):
        pass
    def makeSound(self):
        print("...")

class Hund(Tier):
    def __init__(self):
        pass
    def makeSound(self):
        print("wuff")

class Katze(Tier):
    def __init__(self):
        pass
    def makeSound(self):
        print("miau")

# Wie könnte ein Auto mehrere Reifen haben?
# -> Verwendung von Klassen in Klassen als Attribute


print("---")
def someErrorMethod():
    print("Macht sinnvolles...")
    raise Exception("Fehler!")
    print("Toter Code")

try:
    someErrorMethod()
except Exception:
    print("Oho...")
print("Weitermachen...")


#def add2(a : int, b : int) -> int:
#    return a + b
#print(add2("str", "str"))



tier1 = Hund()
tier2 = Katze()

# ---

t = tier2
t.makeSound()

def nutzeTier(tier: Tier):
    tier.makeSound()

nutzeTier(tier1)