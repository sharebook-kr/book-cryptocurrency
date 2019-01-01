import pandas as pd 
df = pd.read_excel("ohlc.xlsx") 
df = df.set_index('date')
print(df)
df.to_excel("ohlc-2.xlsx")
