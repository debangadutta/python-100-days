class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()
    
class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__(b, h)
    
    def area(self):
        return 0.5*super().area()
    
rect = Shape(4,3)
print(f"Area of rectangle with sides 4 and 3: {rect.area()}")

circ = Circle(10)
print(f"Area of circle with radius 10: {circ.area()}")

triang = Triangle(10, 5)
print(f"Area of triangle with dimensions 10 and 5: {triang.area()}")