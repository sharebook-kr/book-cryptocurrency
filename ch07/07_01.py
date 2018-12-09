import pybithumb

df = pybithumb.get_ohlcv("BTC")
print(df.tail())