import pandas as pd
data = {
    'A':[1,2,3,4,5],
    'B':['a','b','c','d','e'],
    'C':[0,1,2,3,4]
}

df = pd.DataFrame(data)
df =df.replace(3,pd.NaT)
print(df)