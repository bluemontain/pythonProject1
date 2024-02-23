import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)

df.rename(columns={"Name":"姓名"},inplace=True)

print(df.columns)
print(df)