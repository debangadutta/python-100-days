class Mathematix:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num += n
        print(f"It is now {self.num}")

    @staticmethod
    def additioner(x, y):
        print("Calling static method now")
        return x+y
    
a = Mathematix(5)
a.add_to_num(10)
print(Mathematix.additioner(20,30))