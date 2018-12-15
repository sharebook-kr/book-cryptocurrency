import time
import pybithumb
from datetime import datetime

with open("bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(key, secret)

def get_target_price():
	try:
		df = pybithumb.get_ohlcv("BTC")
		yesterday = df.iloc[-2]

		today_open = yesterday['close']
		yesterday_high = yesterday['high']
		yesterday_low = yesterday['low']
		target = today_open + (yesterday_high - yesterday_low) * 0.5
		return target
	except:
		return None
		
def try_buy(price, target, ma5):
    try:
        krw = bithumb.get_balance("BTC")[2]
        orderbook = pybithumb.get_orderbook("BTC")
        asks = orderbook['asks']
        sell_price = asks[0]['price']               # 최우선 매도가
        unit = krw/float(sell_price)

        if price > target and price > ma:
            print("매수조건", price, target)
            bithumb.buy_market_order("BTC", unit)
        else:
            print("매수조건아님", price, target)
    except:
        pass

def try_sell():
    try:
        unit = bithumb.get_balance("BTC")[0]
        bithumb.sell_market_order("BTC", unit)
    except:
        print("try sell error")
	
def cal_moving_average(window):
    try:
        df = pybithumb.get_ohlcv("BTC")
        close = df['close']
        ma = close.rolling(window=window).mean()
        return ma[-2]
    except:
        return None
	
	
now = datetime.now()
mid = datetime(now.year, now.month, now.day + 1)
target_price = get_target_price()
ma5 = cal_moving_average(5)

while True:
    now = datetime.now()
    if mid < now < mid + datetime.delta(seconds=10): 
        target_price = get_target_price()
        ma5 = cal_moving_average(5)
        now = datetime.now()
        mid = datetime(now.year, now.month, now.day + 1)
        try_sell()
        time.sleep(10)

    current_price = pybithumb.get_current_price("BTC")
    if current_price is not None:
        try_buy(current_price, target_price, ma5)
			    	
    time.sleep(1)