import pandas as pd

df = pd.DataFrame({'Name':['Alice','Bob','Charlie'],
                   'Age':[10,22,27],
                   'city': ['New York','Paris','London']
                   })
#默认升序排序
df_sort=df.sort_values('Age')
#降序排序
df_sort_ascen_F=df.sort_values('Age',ascending=False)

df_sorted=df.sort_values(['Age','Name'])
print(df_sorted)