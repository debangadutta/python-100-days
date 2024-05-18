num = input("Enter a number between 5 and 9: ")

if num=="quit":
    print("Quitting!")
elif not 5 < int(num) < 9:
    raise ValueError("Number not between 5 and 9")
else: print(num)