import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

window = close.rolling(5)
ma5 = window.mean()
print(ma5)
