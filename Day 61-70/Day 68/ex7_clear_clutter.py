import os

files = os.listdir("Day 61-70/Day 68")
i=1
for file in files:
    if file.endswith(".txt"):
        print(file)
        os.rename(f"Day 61-70/Day 68/{file}", f"Day 61-70/Day 68/{i}.txt")
        i+=1