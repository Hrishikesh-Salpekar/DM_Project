# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:39:53 2018

@author: Hrishikesh
"""

import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
i=0
typ1=pd.DataFrame()
typ2=pd.DataFrame()
typ3=pd.DataFrame()
typ0=pd.DataFrame()
fin=pd.DataFrame()
df=pd.read_csv("ddata.csv")
loctype=df.loctype.unique().tolist()
df.drop(['Unnamed: 0','Stn.Code','RSPM.PM10','SPM','PM.2.5'], axis=1, inplace=True)

df.drop_duplicates(inplace=True)
# Treating Missing Values
for state in df.State.unique():
    it=df.loc[df["State"]==state]
    so2=it.SO2.describe()[5]
    no2=it.NO2.describe()[5]
    it.SO2.fillna(so2,inplace=True)
    it.NO2.fillna(no2,inplace=True)
    fin=fin.append(it)
    
so2_2=fin.SO2.describe()[6]
so2_1=fin.SO2.describe()[4]
so2=fin.SO2.tolist()
out_so2=[x for x in so2 if x<so2_1 or x>so2_2]

for city in fin["City.Town.Village.Area"].unique():
    df2=fin.loc[fin["City.Town.Village.Area"]==city]
    for typ in df2["loctype"].unique():
        df3=df2.loc[df2["loctype"]==typ]
        for date in df3["Sampling.Date"].unique():
            df1=df3.loc[df3["Sampling.Date"]==date]
            flag=0
            state=df1.State.unique()[0]
            SO2=mean(df1.SO2)
            NO2=mean(df1.NO2)
            itr=pd.DataFrame({"Sampling.Date":date,"State":state,"City":city,"LocType":typ,"SO2":SO2,"NO2":NO2},index=[i])
            i=i+1
            loc=loctype.index(typ)
            for x in set(out_so2):
                if x in df1["SO2"]:
                    flag=1
            if flag==0:
                if loc == 1:
                    typ1=typ1.append(itr,ignore_index=True)
                if loc == 2:
                    typ2=typ2.append(itr,ignore_index=True)
                if loc == 3:
                    typ3=typ3.append(itr,ignore_index=True)
                if loc == 0:
                    typ0=typ0.append(itr,ignore_index=True)
            print(i)

typ1.to_csv("type1DataBase(new).csv")
typ0.to_csv("type0DataBase(new).csv")
typ3.to_csv("type3DataBase(new).csv")
typ2.to_csv("type2DataBase(new).csv")

# Scaling Features
df=pd.read_csv("type3DataBase(new).csv")
df["Scale_SO2"]=(df["SO2"]/max(df.SO2))
df["Scale_NO2"]=(df["SO2"]/max(df.NO2))
print(df)
df.to_csv("type3DataBase(new)(scaled).csv")
    