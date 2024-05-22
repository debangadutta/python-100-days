#higher order functions-> function taking function as an input

#map-> map(function, iterable)
def cuber(x):
    return x**3

input_list = [1,2,3,4,5]

output_list = list(map(cuber, input_list))      #we do not have to use a loop and another list to iterate and store the cubes
print(f"Without lambda fxn: {output_list}")

output_list2 = list(map(lambda x: x**3, input_list))
print(f"With lambda fxn: {output_list2}")

#filter -> filter(function, iterable)
def filter_func(y):
    return y>3

filtered_list = list(filter(filter_func, input_list))
print(f"Filtered list: {filtered_list}")

filtered_list2 = list(filter(lambda x:x>3,input_list))
print(f"Filtered list using lambda fxn: {filtered_list2}")

#reduce-> reduce(function, iterable)
from functools import reduce
numbers = [1,2,3,4,5]

reduced_list = reduce(lambda x,y: x+y, numbers)
print(f"Reduced list add: {reduced_list}")
reduced_list2 = reduce(lambda x,y: x*y, numbers)
print(f"Reduced list multiply: {reduced_list2}")