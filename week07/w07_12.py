import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")

df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
#df['bull'] = df['high'] > df['ma5']
df['bull'] = df['open'] > df['ma5']

fee = 0.0032
df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                      df['close'] / df['target'] - fee,
                      1)

df['cumprod'] = df['ror'].cumprod()
df['mdd'] = (df['cumprod'].cummax() - df['cumprod']) / df['cumprod'].cummax()  * 100
print("MDD: ", df['mdd'].max())
print("ROR: ", df['cumprod'][-2])
df.to_excel("larry_ma.xlsx")


