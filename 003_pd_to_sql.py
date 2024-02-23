import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import  *

df = pd.DataFrame({"name":["乌镇中心","雄衡中心","哈尔滨中心","合肥中心"],
                   "CX55":[10000,1000,2000,8000],
                   "DCU":[20000,2000,4000,8000]})
df = pd.read_csv("C:\\workspace\\pandas\\download\\FL_insurance_sample.csv",encoding='utf-8')
engin=create_engine('mysql+mysqlconnector://root:laomao@127.0.0.1/info')
df.to_sql('new_table',engin,if_exists='append')
#df.to_sql('tutest',engin,if_exists='append',index=None)

