from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*10

print(fx(20))
print("Done for 20")
print(fx(5))
print("Done for 5")
print("---------")
print(fx(20))
print("Done for 20")
print(fx(5))
print("Done for 5")
print(fx(50))
print("Done for 50")
