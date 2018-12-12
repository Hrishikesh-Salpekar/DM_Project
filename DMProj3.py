# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:15:06 2018

@author: Hrishikesh
"""

import pandas as pd

df=pd.read_csv("type3DataBase(new).csv")
df["Scale_SO2"]=(df["SO2"]/max(df.SO2))
df["Scale_NO2"]=(df["SO2"]/max(df.NO2))
print(df)
df.to_csv("type3DataBase(new)(scaled).csv")