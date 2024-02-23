import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)
#获取Height行的最大值和最小值，本例中最大最小值均为180
max_height=df.loc[2,'Height'].max()
min_Height=df.loc[2,'Height'].min()

print(df)
print(max_height)
print(min_Height)