class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    
    def __str__(self):
        return f"Name of the employee is {self.name}. ADIOS!"
    
    def __call__(self):
        print("Call methodo printo")
    
emp1 = Employee("Debanga")
print(emp1.name)
print(len(emp1))

# print(emp1)         
#gives o/p-> <__main__.Employee object at 0x0000022E9553A890>
#if used with __str__ function

#after defining __str__ in class
print(emp1)
emp1()