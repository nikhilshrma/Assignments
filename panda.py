import pandas as pd

data={'Name':['nikhil','dfad'],'Age':[20,190],'mailid':['xyz@gmail.com','ddd@gmail.com'],'phn':['91952','91152']}
df=pd.DataFrame(data)
print(df)

df=pd.read_csv('/home/nikhil/anaconda3/envs/iris_2/weather.csv')
print(df.head())
print(df.head(10))
print(df.describe())
print(df.tail(5))
print(df.Location.describe())