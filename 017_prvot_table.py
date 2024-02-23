import pandas as pd

df = pd.DataFrame({'Product':['A','B','C','A','B','C','A','B','C'],
                   'SalesDate':['2024-02-02','2024-02-02','2024-02-02',
                                '2024-02-03','2024-02-03','2024-02-03',
                                '2024-02-04','2024-02-04','2024-02-04'],
                   'SalesAmount': [100,200,150,50,75,125,300,250,200]
                   })

df_pivot = df.pivot_table(index='Product',columns='SalesDate',values='SalesAmount',aggfunc='sum')
print(df_pivot)