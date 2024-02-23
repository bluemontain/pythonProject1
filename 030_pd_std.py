import pandas as pd
data = {
    'Name': ['Jack', 'Sarah', 'Mike','David'],
    'Age': [24, 30, 21,29],
    'Height': [175,165,180,170]
}

df = pd.DataFrame(data)

std_age=df['Age'].std()
std_Height=df['Height'].std()
print(std_age)
print(std_Height)