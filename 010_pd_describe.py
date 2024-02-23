import pandas as pd
#read dataframe from csv
data={"A":[1,2,3,4,5],
      'B':[2.1,4.2,6.3,4,10.5],
      'C':['a','b','a','b','a']
      }
df=pd.DataFrame(data)
print(df)
print(df.describe())