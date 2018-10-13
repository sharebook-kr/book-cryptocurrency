import pybithumb

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")
