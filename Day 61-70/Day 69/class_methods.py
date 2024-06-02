class Employee:
    company = "Microsoft"

    def show(self):
        print(f"\nName: {self.name}\nCompany: {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


emp1 = Employee()
emp1.name = "Debanga"
emp1.show()

'''
emp1.changeCompany("Apple")
emp1.show()
print(Employee.company)  -> Microsoft
==>doing this without decorator in the function does NOT change class variable, only instance variable.
so we add @classmethod decorator in the changeCompany function
'''
emp1.changeCompany("Apple")
emp1.show()
print(Employee.company)     #now company (class variable) has been changed but not earlier as now we used decorator