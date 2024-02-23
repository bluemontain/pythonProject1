import pandas as pd

df = pd.DataFrame({'Name':['Alice','Bob','Charlie'],
                   'Age':[21,22,21],
                   'city': ['New York','Paris','London']
                   })

sub=df.loc[[0,2],['Name','Age']]
sub1 = df.iloc[[0,2],[0,1]]
print(sub)
print(sub1)