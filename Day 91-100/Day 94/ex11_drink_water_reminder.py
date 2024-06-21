from plyer import notification
import time

title = 'DRINK WATER!'
message = "It's time to get up"

i=0
while i <5:
    notification.notify(title=title,
                        message=f"{message}. This is reminder number {i+1}",
                        timeout=2)
    i+=1
    time.sleep(5)