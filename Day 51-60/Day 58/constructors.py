class Person:
    def __init__(self, name):
        self.name = name
        print(f"Constructor of {self.name} here!")

    def info(self):
        print(f"Your name is {self.name}")

a = Person("Debanga")
a.info()

b = Person("Ramesh")