import pandas as pd
df = pd.DataFrame({"name":["乌镇中心","雄衡中心","哈尔滨中心","合肥中心"],
                   "CX55":[10000,1000,2000,8000],
                   "DCU":[20000,2000,4000,8000]})
first_two=df.loc[[0,1]]
sub = df.loc[[0,2],['name','CX55']]
print(sub)