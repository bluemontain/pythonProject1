import pandas as pd
#read dataframe from csv
data={"name":['alex','box','chery'],'age':[19,20,12]}
df=pd.DataFrame(data)
print(df.dtypes)