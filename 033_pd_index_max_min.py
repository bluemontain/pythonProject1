import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)

max_age=df['Age'].max()
min_age=df['Age'].min()

print(max_age)
print(min_age)