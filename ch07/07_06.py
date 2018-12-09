import numpy as np
from pandas import DataFrame

data = {'빗썸': [100, 100, 100],
        '코빗': [90, 110, 120]}

df = DataFrame(data)
df['최저가'] = np.where(df['빗썸'] < df['코빗'], '빗썸', '코빗')
df.to_excel("거래소.xlsx")