class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age        #private variable

e1 = Employee("Debanga", 20)
print(e1.name)
print(e1._Employee__age)        #to access private variable-> _ClassName__PrivVariable
#above line is also called name mangling