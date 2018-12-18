import time
import pybithumb
from datetime import datetime

def get_target_price(ticker):
    df = pybithumb.get_ohlcv("BTC")
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

now = datetime.now()
mid = datetime(now.year, now.month, now.day) + datetime.timedelt(1)
target_price = get_target_price("BTC")

while True:
    now = datetime.now()
    if mid < now < mid + datetime.delta(seconds=10) : 
        target_price = get_target_price("BTC")
        mid = datetime(now.year, now.month, now.day) + datetime.timedelt(1)

    current_price = pybithumb.get_current_price("BTC")
    print(current_price)

    time.sleep(1)