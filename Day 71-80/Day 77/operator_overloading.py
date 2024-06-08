class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, vec):
        return Vector(self.i + vec.i, self.j + vec.j, self.k + vec.k)
    
    def __sub__(self, vec):
        print("\nSubtracting...")
        return Vector(self.i - vec.i, self.j - vec.j, self.k - vec.k)



vec1 = Vector(3, 4, 5)
print(vec1)

vec2 = Vector(2, 3, 4)
print(vec2)

print(f"\nSum: {vec1 + vec2}")
print(type(vec1 + vec2))        #gives str unless we return Vector in __add__

print(f"Subtract: {vec2 - vec1}")