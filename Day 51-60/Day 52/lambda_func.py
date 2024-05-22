doubling = lambda x : x*2

cuber = lambda x : x**3

avger = lambda x,y: (x+y)/2

def appl(fxn, value):
    return 10 + fxn(value)

print(doubling(5))
print(cuber(5))
print(avger(5,10))

print(appl(cuber, 5))
print(appl(doubling, 10))
print(appl(lambda x : x*2, 10))     #same as above line
print(appl(lambda x : x*x, 10))