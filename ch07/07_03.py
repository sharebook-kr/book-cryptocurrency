import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df.to_excel("btc.xlsx")