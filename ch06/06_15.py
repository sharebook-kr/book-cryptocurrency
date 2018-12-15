import time
from datetime import datetime

now = datetime.now()
mid = datetime(now.year, now.month, now.day + 1)

while True:
    now = datetime.now()
    if mid < now < mid + datetime.delta(seconds=10) : 
        print("정각입니다")
        now = datetime.now()
        mid = datetime(now.year, now.month, now.day + 1)

    time.sleep(1)