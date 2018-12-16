import time
import pybithumb
from datetime import datetime

con_key = "81dd5f25e5daa70b2fff603901d2c09c"
sec_key = "82333efegeg9eg3e77c573weg34af17a"
bithumb = pybithumb.Bithumb(con_key, sec_key)

def get_target_price():
    df = pybithumb.get_ohlcv("BTC")
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

now = datetime.now()
mid = datetime(now.year, now.month, now.day + 1)
target_price = get_target_price()

while True:
    now = datetime.now()
    if mid < now < mid + datetime.delta(seconds=10): 
        target_price = get_target_price()
        mid = datetime(now.year, now.month, now.day + 1)

    current_price = pybithumb.get_current_price("BTC")
    if current_price is not None and current_price > target:
        krw = bithumb.get_balance("BTC")[2]
        orderbook = pybithumb.get_orderbook("BTC")
        sell_price = orderbook['asks'][0]['price']  # 최우선 매도호가
        unit = krw/float(sell_price)
        bithumb.buy_market_order("BTC", unit)

    time.sleep(1)