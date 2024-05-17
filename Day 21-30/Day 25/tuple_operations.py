fruits = ("Apple", "Banana", "Mango")
print(fruits)
temp = list(fruits)     #convert tuple to list
temp.append("Orange")       #append an item to the list
print(temp)
temp.pop(2)     #remove an item from the list
print(temp)
temp[1] = "Pineapple"       #change an item in the list
print(temp)
fruits = tuple(temp)        #convert list back to tuple
print(fruits)

print(fruits.index("Pineapple"))