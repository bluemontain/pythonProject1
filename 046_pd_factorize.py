import pandas as pd

data = {
    'Name': ['Tom', 'Mary', 'Jack'],
    'Age': [20, 25, 30],
    'Gender': ['M', 'F', 'M']
}

df = pd.DataFrame(data)
factorized, _ = pd.factorize(df['Gender'])
df['Genderfator'] = factorized
print(df)
