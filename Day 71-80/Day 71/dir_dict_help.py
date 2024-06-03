#used to get info about objects-> dir(), dict and help()

print("-----------dir-----------")
x = [1, 2, 3]
print(dir(x))
print(x.__add__)


print("\n-----------dict-----------")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Debanga", 20)
print(p.__dict__)


print("\n-----------help-----------")
print(help(Person))