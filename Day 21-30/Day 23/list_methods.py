#append
l = [5,2,1,67,100,200]
print(l)
l.append(8)
print(l)

#sort
m = l.copy()
m.sort()
print(m)

#reverse
n = l.copy()
n.reverse()
n[0] = 999
print(n)

#insert at index
l.insert(5,987)
print(l)

#extend
l.extend(m)
print(l)

#concatenate instead of extend
z = m+n
print(z)
print(m)
print(n)