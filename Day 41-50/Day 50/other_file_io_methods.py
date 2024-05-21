#read by line
f = open('Day 41-50/Day 50/myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

#another example
g = open('Day 41-50/Day 50/marks.txt', 'r')
i=0
while True:
    i+=1
    line1 = g.readline()
    if not line1:
        break
    m1 = line1.split(",")[0]
    m2 = line1.split(",")[1]
    m3 = line1.split(",")[2]
    print(f"Marks of student {i} in Math: {m1}")
    print(f"Marks of student {i} in Science: {m2}")
    print(f"Marks of student {i} in English: {m3}")
g.close()

#writing
h = open('Day 41-50/Day 50/myfile2.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3']
h.writelines(lines)
h.close()