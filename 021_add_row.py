import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)
new_row={'Name':'Jeames','Age':28,'Height':181}
df.loc[len(df)]=new_row
print(df)