import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

ma5 = close.rolling(5).mean()
print(ma5)
