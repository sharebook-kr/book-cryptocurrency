import pykorbit.history

df = pykorbit.history.get_daily_ohlc("BTC", start="2018-01-01")
ma5 = df['close'].rolling(window=5).mean()
df.insert(4, "ma5", ma5)
print(df)
