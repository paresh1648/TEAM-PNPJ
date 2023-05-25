#We have written code to detect outliers in Python in this big Data
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('Login_Data.csv')
df

df.describe()

model=IsolationForest(n_estimators=1000,max_samples='auto',contamination=float(0.2),max_features=1.0)
model.fit(df[['User ID']])

df['login']=model.decision_function(df[['User ID']])
df['anomaly']=model.predict(df[['User ID']])
df.head(20)

outliers_counter = len(df[df['User ID'] > 36])
outliers_counter