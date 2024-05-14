import time

time_now = time.localtime()

if(time_now.tm_hour>6 and time_now.tm_hour<12):
    print("Good morning!")
elif(time_now.tm_hour>12 and time_now.tm_hour<17):
    print("Good afternoon!")
else:
    print("Good evening!")