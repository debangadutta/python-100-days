dict1 = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D"
}

print(f"Value of ID 1: {dict1[1]}")
#get
print(f"Using .get to get value of ID 1: {dict1.get(1)}")
print(f"Using .get to get value of ID 5: {dict1.get(5)}")

print(f"\nEntire dictionary dict1: {dict1}")

#accessing all keys
print(f"\nAll keys in dict1: {dict1.keys()}\n")
#accessing all values
print(f"\nAll values in dict1: {dict1.values()}\n")

#looping through
for key in dict1.keys():
    print(f"Key: {key}, Value: {dict1[key]}")

#.items -> unpacks
print(dict1.items())
for key, value in dict1.items():
    print(f"Key is {key}, value is {value}")