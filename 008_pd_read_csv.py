import pandas as pd
#从csv文件中读入数据，并输出前三行和后三行
df = pd.read_csv("C:\\workspace\\pandas\\download\\downloadfile.csv",encoding='utf-8')
print(df.head(3))
print(df.tail(3))
