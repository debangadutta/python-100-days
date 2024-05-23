a = [1,2,3]
b = [1,2,3]

print(a is b)       #compares exact location of object in memory
print(a == b)       #compares value

#BUT
c = 4
d = 4
print(c is d)
print(c == d)       #reason: immutable things like constants, str and tuples