import time
from datetime import datetime

now = datetime.now()
mid = datetime(now.year, now.month, now.day + 1)

while True:
    now = datetime.now()
    if now == mid : 
        print("정각입니다")
        now = datetime.now()
        mid = datetime(now.year, now.month, now.day + 1)
       
    print(now, "vs", mid)
    time.sleep(1)
