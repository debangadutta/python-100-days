#union and update
s1 = {1,2,3,4}
s2 = {4,5,6,7}
print(f"s1: {s1}, s2: {s2}")
print(f"s1 U s2: {s1.union(s2)}")

s1.update(s2)
print(f"s1.update(s2): {s1}")

#intersection and intersection_update
s3 = {"Mumbai", "Delhi", "Bangalore"}
s4 = {"Chennai", "Mumbai"}
print(f"s3: {s3}, s4: {s4}")
print(f"s3.intersection(s4): {s3.intersection(s4)}")
s3.intersection_update(s4)
print(f"After s3.intersection_update(s4)-> s3: {s3}, s4: {s4}")

#symmetric difference -> AUB - A(intersection)B
print(f"s3.symmetric_difference(s4): {s3.symmetric_difference(s4)}")

#disjoint sets
print(f"\ns3: {s3}, s4: {s4}")
print(f"Are s3 and s4 disjoint?: {s3.isdisjoint(s4)}")

#subsets and supersets
print(f"\ns1: {s1}, s2: {s2}")
print(f"Is s1 a superset of s2? {s1.issuperset(s2)}")
print(f"Is s2 a subset of s1? {s2.issubset(s1)}")

#adding elements
print(f"\ns3: {s3}")
s3.add("Guwahati")
print(f"s3: {s3}")

#remove and discard - discard does NOT throw an error when no element found to discard, remove throws an error
print(f"\ns4: {s4}")
s4.remove("Chennai")
print(f"s4: {s4}")

#pop-> pops any random element
#del-> deletes entire set
#clear-> clears entire set and prints empty set