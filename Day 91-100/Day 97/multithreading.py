import threading
import time

def func1(seconds):
    time.sleep(seconds)
    print(f"Slept for {seconds} seconds.")

#without multi-threading
time1 = time.perf_counter()
func1(4)
func1(1)
func1(2)
time2 = time.perf_counter()
print(time2 - time1)

#with multi-threading
t1 = threading.Thread(target=func1, args=[4])
t2 = threading.Thread(target=func1, args=[1])
t3 = threading.Thread(target=func1, args=[2])

t1.start()
t2.start()
t3.start()

#we wait for t1, t2 and t3 to complete, if not using join then only initializing time is counted
t1.join()
t2.join()
t3.join()

time3 = time.perf_counter()
print(time3 - time2)