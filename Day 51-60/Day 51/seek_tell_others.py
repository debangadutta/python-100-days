#seek
with open('Day 51-60/Day 51/file.txt', 'r') as f:
    print(type(f))

    f.seek(10)      #moves to 10th byte
    print(f.tell())     #tell-> tells the current position
    data = f.read(5)        #read from 11th byte to 5 chars
    print(data)
    print(f.tell())

print("\n")

#truncate
with open('Day 51-60/Day 51/file2.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)

with open('Day 51-60/Day 51/file2.txt', 'r') as f:
    print(f.read())