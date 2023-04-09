# -*- coding: utf-8 -*-
"""Placement_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vr2szF_hYBtJ8_e5v1B3lORxXWwPDlTV
"""

import pandas as pd

import numpy as np  

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/placement.csv')

df

df.isnull().sum()

df.dropna()

df.shape

df.isnull().sum()

df.info()

df.drop(['sl_no','gender','ssc_b','hsc_b','hsc_s','degree_t','workex','specialisation'],axis=1,inplace=True)

df

df.drop(['salary'], axis=1, inplace=True)

df

x= df.drop('status',axis=1)

y= df['status']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

df1=pd.DataFrame({'Actual Status':y_test,'Predicted Status':y_pred})

df1.head(15)

print(accuracy_score(y_test,y_pred)*100)

x_train.shape

from numpy import array

from sklearn.preprocessing import LabelEncoder

data = y_pred


a=y_pred

values = array(data)

label_encoder = LabelEncoder()

integer_encoded = label_encoder.fit_transform(values)

print(integer_encoded)


y_pred=integer_encoded

print(data)

plt.scatter(x_test['mba_p'], y_pred)

sample=model.predict([[50,59,43,50,45]])

print(sample)

