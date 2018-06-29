import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                      df['close'] / df['target'] - fee,
                      1)

df['cumprod'] = df['ror'].cumprod()
df['mdd'] = (df['cumprod'].cummax() - df['cumprod']) / df['cumprod'].cummax()  * 100
print(df['mdd'].max())
df.to_excel("mdd.xlsx")


