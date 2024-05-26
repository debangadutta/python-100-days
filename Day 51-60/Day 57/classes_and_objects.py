class Person:
    name="Debanga"
    role="Student"
    mouse="Razer"

    def info(self):
        print(f"{self.name} is a {self.role} and has a {self.mouse} mouse.")
    
a = Person()
a.info()

b = Person()
b.name="Ramesh"
b.mouse="Logitech"
b.info()

c = Person()
c.name="Benedikt"
c.role="Professor"
c.info()