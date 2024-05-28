class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"Employee {self.id} has name {self.name}")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def show_languages(self):
        print(f"Speaks {self.lang}")

e1=Employee("Debanga", 1)
e1.show_details()
e2=Programmer("Dutta", 2, "Hindi")
e2.show_details()
e2.show_languages()