# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:51:07 2018

@author: Hrishikesh
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 

#x = [1,2,3] 
#a = np.asarray(x) 
style.use ('ggplot')

df=pd.read_csv("ddata.csv")
#print(df.head())
df.drop(['Unnamed: 0','Stn.Code'], axis=1, inplace=True)
df["Sampling.Date"]=pd.to_datetime(df["Sampling.Date"])

df.rename(columns={'City.Town.Village.Area':'City'},inplace=True)
print(df.describe())
for i in df["City"].unique():
    df1=df.loc[df["City"]==i]
    df1.set_index("Sampling.Date",inplace=True)
    plt.title(i)
    df1.plot.box()
    plt.show()
print(df1.describe())

#print(df1.head())
#style.use ('presentation')
plt.scatter(df1["NO2"],df1["SO2"],label='skitscat', color='k', s=25, marker="o")
plt.xlabel("NO2")
plt.ylabel("SO2")
plt.show()
grr=pd.scatter_matrix(df1)
plt.show()
#plt.savefig('foo.png')
#print(df1["Sampling.Date"])
#print(df1["NO2"])
#df1.plot()
#df1["NO2"].T.squeeze()

