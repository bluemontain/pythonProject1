import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)
df.set_index('Name', inplace=True)
new_df=df.loc['Sarah':'David']
print(new_df)