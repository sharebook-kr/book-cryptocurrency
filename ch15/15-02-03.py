import pykorbit
import pykorbit.history

df = pykorbit.history.get_daily_ohlc("BTC", start="2018-01-01")
ma5 = df['close'].rolling(window=5).mean()
df.insert(4, "ma5", ma5)

cur_price = pykorbit.get_current_price("btc_krw")
ma5_price = df.iloc[-1]['ma5']
print(cur_price, ma5_price)

if cur_price > ma5_price:
    print("상승장")
else:
    print("하락장")
