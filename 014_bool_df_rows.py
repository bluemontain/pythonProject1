import pandas as pd

df = pd.DataFrame({'Name':['Alice','Bob','Charlie'],
                   'Age':[21,22,27],
                   'city': ['New York','Paris','London']
                   })

bool_index = df["Age"] > 25
filt = df[bool_index]
print(filt)