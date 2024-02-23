import pandas as pd
import numpy as np

data = {
    'A':[1,2,np.nan,4,5],
    'B':['a','b','c','d','e'],
    'C':[0,1,np.nan,3,4]
}

df = pd.DataFrame(data)
#将缺失值填按列填充不同的值
df.fillna(value={'A':-1,'C':2},inplace=True)
#将缺失值填充为指定的值0
df.fillna(value=0,inplace=True)
#ffile向前填充将缺失值填充为前一个值
df.fillna(method='ffill',inplace=True)
#bfile向后填充将缺失值填充为前一个值
df.fillna(method='bfill',inplace=True)
print(df)