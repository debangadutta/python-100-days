#default arguments
def average_calc(a=9, b=1):
    print("Average is: ", (a+b)/2)

average_calc()
average_calc(5)

#required arguments
def sum_calc(a, b=10):
    print("Sum is:", a+b)

sum_calc(10)
sum_calc(10,5)

#keyword arbitrary arguments - as tuple
def arbitrary_avg(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average of", len(numbers), "is:", sum/len(numbers))

arbitrary_avg(10,20,30)
arbitrary_avg(100,200)
arbitrary_avg(1,2,3,4,5)

#keyword arbitrary arguments - as dictionary
def names_system(**name):
    print("Your name is:", name["fname"], name["lname"])

names_system(fname="Debanga",lname="Dutta")