lst = [i*i for i in range(5)]
print(lst)

lst1 = [i*i for i in range(10) if i%2==0]
print(lst1)

a = [i for i in range(3)]
lst2 = [lst1[i] for i in a]
print(lst2)