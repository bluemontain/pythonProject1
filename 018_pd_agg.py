import pandas as pd

df = pd.DataFrame({'Product':['A','B','C','A','B','C','A','B','C'],
                   'SalesDate':['2024-02-02','2024-02-02','2024-02-02',
                                '2024-02-03','2024-02-03','2024-02-03',
                                '2024-02-04','2024-02-04','2024-02-04'],
                   'SalesAmount': [100,200,150,50,75,125,300,250,200]
                   })

juhe_df = df.groupby('Product')['SalesAmount'].agg(['mean','std','sum','max'])
print(juhe_df)