import pandas as pd
import numpy as np

data = {
    'A':[1,2,None,4,5],
    'B':['a','b',None,None,'e'],
    'C':[0,1,None,3,4]
}

df = pd.DataFrame(data)
#按行删除
#df.dropna(inplace=True)
#df_dropna_colums=df.dropna(axis=1)
df_dropna_columB=df.dropna(subset=['B'])
print(df_dropna_columB)