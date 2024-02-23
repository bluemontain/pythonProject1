import pandas as pd
#pandas中的列索引-cloums
data={"name":['alex','box','chery'],
      'age':[19,20,12]
      }
df=pd.DataFrame(data)
print(df.columns)
print(df)
