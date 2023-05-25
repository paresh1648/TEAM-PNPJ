import pandas as pd
data=pd.read_csv('drive/MyDrive/Login_Data.csv')
df=data.head()

data.describe()

percentile_95 = np.percentile(data['median'], 95, method='median_unbiased')

percentile_5 = np.percentile(data['median'], 5, method='median_unbiased')

greater_than_95 = (data[['median']] > percentile_95)

smaller_than_5 = (data[['median']] < percentile_5)

# create column named colors to store the color of each point based on the condition above 

data['colors'] = np.where(greater_than_95,'r',np.where(smaller_than_5,'r','b'))

data.plot.scatter(x='year', 

                       y='median', 

   c=data['colors'].apply(lambda x: dict(r='red', b='blue')[x]), 

                       figsize=(10, 5),

                       title='Median World Inflation Rate',

                       xlabel='Year',

                       ylabel='Median Inflation Rate')

plt.xticks(rotation=65);