class Student:
    def __init__(self):
        self._name = "Debanga"

    #protected method
    def _funName(self):
        return "Debanga Dutta"
    
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(f"Student class variable: {obj._name}")
print(f"Student class method: {obj._funName()}")

print(f"\nSubject class variable: {obj1._name}")
print(f"Subject class method: {obj1._funName()}")