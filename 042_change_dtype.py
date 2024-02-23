import pandas as pd
import numpy as np

data = {
    'Name':['Tom','Tom','Mary','Mary','Jack','Jack'],
    'Subject':['Math','English','Math','English','Math','English'],
    'Score':[80,71,85,75,90,95]
}

df=pd.DataFrame(data)
print(df.dtypes)
df['Score']=df['Score'].astype(int)
grouped=df.groupby(['Name'])['Score'].agg(['mean','max','min','count'])

print(df.dtypes)