class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

emp1 = Employee("Debanga", 50)
emp2 = Programmer("Dutta", 1, "Python")
print(f"Employee 1 name: {emp1.name}\nID: {emp1.id}\nLanguage: DNE as no language attribute here")
print(f"\nEmployee 2 name: {emp2.name}\nID: {emp2.id}\nLanguage: {emp2.lang}")