import pandas as pd
df = pd.DataFrame({"name":["乌镇中心","雄衡中心","哈尔滨中心","合肥中心"],
                   "CX55":[10000,1000,2000,8000],
                   "DCU":[20000,2000,4000,8000]})
first_two=df.iloc[:,0:3]
secont=df[['name','CX55']]

print(first_two)