import pandas as pd
import numpy as np

data = {
    'Name':['Tom','Mary','Jack'],
    'Age':[20,25,30],
    'Gender':['M','F','M']
}

df=pd.DataFrame(data)
print(df)

for index,rows in df.iterrows():
    print(index,rows)