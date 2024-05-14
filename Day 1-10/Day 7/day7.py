print("CALCULATOR!!!")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation to perform: ")

if operation=='+': print(num1+num2)
elif operation=='-': print(num1-num2)
elif operation=='*': print(num1*num2)
elif operation=="/": 
    if num2!=0:
        print(num1/num2)
    else: print("Denominator cannot be 0!")
else: print("Invalid Operation!")