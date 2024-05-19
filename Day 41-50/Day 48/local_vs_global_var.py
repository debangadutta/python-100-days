x = 10  #global variable
print(f"x: {x}")

def printing():
    global x
    x = 4
    y=9
    print(y)

printing()
print(f"x: {x}")