import time

def using_while():
    i = 0
    while i<50000:
        i+=1

def using_for():
    i = 0
    for i in range(50000):
        i+=1


init1 = time.time()
using_while()
print(time.time() - init1)

init2 = time.time()
using_for()
print(time.time() - init2)

print(4)
time.sleep(3)
print("Printed after 3 seconds!")