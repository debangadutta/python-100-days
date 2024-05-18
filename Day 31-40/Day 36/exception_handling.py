a = input("Enter a number: ")

try:
    for i in range(1,6):
        print(f"{a} x {i} = {int(a)*i}")
except:
    print("Invalid input!")

try:
    num = int(input("Enter a number: "))
    x = [5,6,7]
    print(x[num])
except ValueError:
    print("Invalid input!")
except IndexError:
    print("Index not in the list!")