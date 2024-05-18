for i in range(5):
    print(i)
else:
    print("In else block\n")

#with break
for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("In else block!")
print("Out of loop")