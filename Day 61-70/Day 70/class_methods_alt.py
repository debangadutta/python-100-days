class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
emp1 = Employee("Debanga", 12000)
print(emp1.name)
print(emp1.salary)

emp2_details = "Debu-15000"
emp2 = Employee.fromStr(emp2_details)
print(emp2.name)
print(emp2.salary)