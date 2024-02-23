import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)

total_age=df['Age'].sum()
print(new_df)