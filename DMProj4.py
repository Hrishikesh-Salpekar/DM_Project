# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:35:50 2018

@author: Hrishikesh
"""

import datetime
import warnings
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
from matplotlib import style
style.use ('ggplot')

def mod(val):
    if val<0:
        return -1*val
    else:
        return val

def MAPE(test,predictions):
    sum=0.0
    n=len(predictions)
    for i in range(n):
        sum=sum+(mod((test[i]-predictions[i])/test[i]))
    error=sum/n
    return error

def evaluate_arima_model(X, arima_order):
    size=int(len(X))
    test_size=int(0.33*size)
    train,test=X[0:-test_size],X[-test_size:]
    history=[x for x in train]
    predictions = list()
    for t in range(test_size):
        model = ARIMA(history,order=arima_order)
        model_fit=model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        yh=yhat[0]
        predictions.append(yh)
        history.append(test[t])
    error=MAPE(test,predictions)
    return error

def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order=(p,d,q)
                try:
                    mpe = evaluate_arima_model(dataset,order)
                    if mpe<best_score:
                        best_score,best_cfg=mpe,order
                    print("ARIMA%s MAPE=%.3f" %(order,mpe))
                except:
                    continue
    return best_cfg,best_score

df=pd.read_csv("type3DataBase(new).csv")
df1=df.loc[df.City=="Hyderabad"]
series=df1.NO2.T.squeeze()
p_values=range(0,3)
d_values=range(0,3)
q_values=range(0,3)
warnings.filterwarnings("ignore")
cfg,error=evaluate_models(series.values,p_values,d_values,q_values)
print(cfg,error)
try:
    history=[x for x in series]
    predictions=list()
    for t in range(30):
        model=ARIMA(history,order=cfg)
        model_fit=model.fit(disp=0)
        yhat=model_fit.forecast()[0]
        yh=mod(yhat[0])
        predictions.append(yh)
        history.append(yh)
        print(t)
except:
    print("Error")
Y=history
X=[x for x in range(len(Y))]

plt.plot(X,Y)
plt.show()
#print(type(series.values))
#pred=list()
#for i in predictions:
#    pred.append(mod(i))
print(predictions)
