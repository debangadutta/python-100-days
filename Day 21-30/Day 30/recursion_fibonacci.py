def fibonacci(n):
    if(n==0): return 0
    elif(n==1): return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    
num = int(input("Enter the n-th term: ")) 
print(fibonacci(num))

# 0 1 1 2 3 5 8 13 21 34 55