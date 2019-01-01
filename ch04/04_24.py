from pandas import Series, DataFrame

data = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]} 
df = DataFrame(data) 
s = Series([300, 400]) 
df["volume"] = s
upper = df["open"] * 1.3
df["upper"] = upper
print(df)

