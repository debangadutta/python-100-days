#reading
f = open('Day 41-50/Day 49/myfile.txt', 'r')
text = f.read()
print(text)
f.close()

#writing
g = open('Day 41-50/Day 49/myfile2.txt', 'w')
g.write("contents of file 2")
g.close()

#append -> adds text at the end instead of overwriting

#automatic close
with open('Day 41-50/Day 49/myfile.txt', 'a') as f:
    f.write("New content!")