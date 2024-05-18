def random_func():
    try:
        list1 = [1,2,3,4,5]
        print(list1)
        num = int(input("Enter an index: "))
        print(list1[num])
        return 1
    except:
        print("Invalid index entered!")
        return 0
    finally:
        print("\nFinally block is executed!\n")

f = random_func()
print(f)