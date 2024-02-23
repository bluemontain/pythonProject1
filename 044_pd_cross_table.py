import pandas as pd
import numpy as np

data = {
    'Name':['Tom','Tom','Mary','Mary','Jack','Jack'],
    'Subject':['Math','English','Math','English','Math','English'],
    'Score':[80,71,85,75,90,95]
}

df=pd.DataFrame(data)
cross=pd.crosstab(df['Name'],df['Subject'])
print(cross)