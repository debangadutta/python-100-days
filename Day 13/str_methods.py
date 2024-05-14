# strings are immutable

a = "Apple"
print(a.upper())
print(a.lower())

b = "Banana!!!!!!!"
print(b)
print(b.rstrip("!"))

#replace ALL instances of p with JJ
print(a.replace("p","JJ"))

c = "My name is Debanga"
print(c.split(" "))

#1st letter upper, rest lowercase
d = "hundred days of PythoN"
print(d.capitalize())

#count no. of occurances of a particular letter
print(c.count("a"))

#finding first occurance of a given value, returns index, else -1
e = "Debanga is my name. My name is not ABC."
print(e.find("is"))

#isalnum() - alphanumeric detection
#title() - first chars of all words capital