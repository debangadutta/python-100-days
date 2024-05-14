num = int(input("Enter a number: "))
if(num>0):
    if(num%2==0): print("Positive and Even")
    else: print("Positive and Odd")
elif(num==0):
    print("Zero")
else:
    print("Negative")