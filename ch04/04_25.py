from pandas import Series 

s = Series([100, 200, 300]) 
s2 = s.shift(1) 
print(s) 
print(s2)

