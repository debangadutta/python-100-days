a = int(input("Enter a number: "))

match a:
    case num if num > 0:
        print("Positive number")
        if(num%2)==0: print("Even")
        else: print("Odd")
    case num if num < 0:
        print("Negative number")
    case _:
        print("Zero")