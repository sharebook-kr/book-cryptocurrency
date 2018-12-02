import pybithumb

btc = pybithumb.get_ohlcv("BTC")
print(btc)
close = btc['close']
print(close)