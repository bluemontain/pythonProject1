import pandas as pd
#pandas中的行索引
data={"name":['alex','box','chery'],'age':[19,20,12]}
df=pd.DataFrame(data)
print(df.index)
