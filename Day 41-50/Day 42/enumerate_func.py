fruits = ["Apple", "Banana", "Mango", "Pineapple", "Cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, fruit: {fruit}")

print("\n")
#custom start value
for index, fruit in enumerate(fruits, start=10):
    print(f"Index: {index}, fruit: {fruit}")