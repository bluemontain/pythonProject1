import pandas as pd

df = pd.DataFrame({'Name':['Alice','Bob','Charlie'],
                   'Age':[21,22,27],
                   'city': ['New York','Paris','London']
                   })
#选择年龄大于25岁的行且只输出Name和age两个列
sub = df.loc[df['Age'] > 25,['Name','Age']]
sub1 = df.loc[df['Name'] == 'Bob',['Name','city']]
sub2 = df.iloc[[0,2],[0,1]]
sub3 = df.iloc[1,1:]
print(sub2)