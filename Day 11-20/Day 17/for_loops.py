fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
    for x in range(3):
        print(fruit[x])
    for y in range(len(fruit)-3, len(fruit)):
        print(fruit[y])

# #stepping in range function
print("-------Step function--------")
for p in range(0,10,2):
    print(p)