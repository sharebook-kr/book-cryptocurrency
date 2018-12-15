import pybithumb

df = pybithumb.get_ohlcv("BTC")
yesterday = df.iloc[-2]

today_open = yesterday['close']
yesterday_high = yesterday['high']
yesterday_low = yesterday['low']
target = today_open + (yesterday_high - yesterday_low) * 0.5
print(target)
