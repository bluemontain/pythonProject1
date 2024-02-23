import pandas as pd
#change python list to pandas dataframe
my_list =[('join',25,'male'),('lisa',43,'female'),('davide',18,'male')]
df=pd.DataFrame(my_list,columns=['name','age','sex'])
print(df)