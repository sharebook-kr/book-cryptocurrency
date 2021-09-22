import time
import datetime

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10) : 
        print("정각입니다")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    time.sleep(1)
