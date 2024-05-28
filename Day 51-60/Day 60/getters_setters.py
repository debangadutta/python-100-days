class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property       #GETTER
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)  #assigns 10 to _value

#returns 10*_value with current value 10 with GETTER
print(f"Getter called with value {obj._value}: {obj.ten_value}")

#prints _value with current value 10
print("\nCurrent value of _value:")
obj.show()

#sets _value to 67/10 through SETTER
obj.ten_value = 67

#prints _value with current value 6.7 set by the prev line
print("\nCurrent value of _value:")
obj.show()

##returns 10*_value with current value 6.7 with GETTER
print(f"\nGetter called with value {obj._value}: {obj.ten_value}")

#prints _value with current value 6.7 set by the SETTER
print("\nCurrent value of _value:")
obj.show()