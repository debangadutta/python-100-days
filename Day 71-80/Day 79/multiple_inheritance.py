#more than 1 parent of the child class

class Employee:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        return f"Name: {self.name}"

class Sport:
    def __init__(self, sport):
        self.sport = sport

    def show_details(self):
        return f"Sport: {self.sport}"

class SportsEmployee(Employee, Sport):
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    #if this function is used then we can print both the show_details of the parents
    # def show_details(self):
    #     print(Employee.show_details(self))
    #     print(Sport.show_details(self))


emp1 = SportsEmployee("Debanga", "Cricket")
print(emp1.show_details())               #will print only 1 show_details func; depends on which parent is inherited first in the child

#method resolution order
print(f"\nOrder of method execution: {SportsEmployee.mro()}")