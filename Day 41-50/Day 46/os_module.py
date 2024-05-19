import os

# os.mkdir("Day 41-50/Day 46/Folder created")

# os.rename("Day 41-50/Day 46/Folder created", "Day 41-50/Day 46/Folder created by os")

folders = os.listdir("Day 41-50")
print(folders)

for folder in folders:
    print(f"Folder: {folder}")
    print(os.listdir(f"Day 41-50/{folder}"))