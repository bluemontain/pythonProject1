import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)

new_df = df.sort_values(by='Age',ascending=True)
print(total_age)