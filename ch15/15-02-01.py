import pykorbit.history

df = pykorbit.history.get_daily_ohlc("BTC", start="2018-01-01")
print(df)