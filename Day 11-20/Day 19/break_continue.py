for i in range(10):
    if i==5: break
    print("10 x", i,"=", 10*i)
print("Exited loop because of break at i=5!\n\n")

for i in range(10):
    if i==5:
        print("Skipped i=5")
        continue
    print("10 x", i,"=", 10*i)