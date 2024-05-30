class Employee:
    company_name = "Microsoft"      #class variable
    no_of_employees = 0         #class variable

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.no_of_employees += 1    #we want to increase company size and not instance size. Instance here would be an individial employee

    def show_details(self):
        print(f"\nName of employee: {self.name}\nRaise amount: {self.raise_amount}")
        print(f"Company name: {self.company_name}")
        print(f"Company size: {self.no_of_employees}")

#Employee 1
emp1 = Employee("Debanga")
emp1.show_details()
#what happens when this is called
# Employee.show_details(emp1)
emp1.company_name = "Microsoft India"       #changing the class variable for THIS instance
print("\nCompany name changed for THIS instance:")
emp1.show_details()     #can see the change in company name

#Employee 2
emp2 = Employee("Ramesh")
emp2.raise_amount = 0.5     #can change individually as it is instance variable
emp2.show_details()

print(f"\nClass variable-> company_name: {Employee.company_name}")
Employee.company_name = "Apple"
print(f"Changed company_name: {Employee.company_name}")

print("\nNow Ramesh works for new company as company_name class variable was changed")
emp2.show_details()

print("\nBut since Debanga's company_name variable was changed explicitly, it remains the same as given above.")
emp1.show_details()