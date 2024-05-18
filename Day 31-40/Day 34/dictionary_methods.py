#update
dict1 = {1: 50,2: 60,3: 70}
dict2 = {4: 50,5: 60}
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
dict1.update(dict2)
print(f"After update-> dict1: {dict1}\n")

#clear-> empty dictionary

#pop-> a key-value pair
dict1.pop(3)
print(f"After popping 3-> dict1: {dict1}")

#popitem-> pops last key-value pair
#del-> deletes full dictionary, if no args