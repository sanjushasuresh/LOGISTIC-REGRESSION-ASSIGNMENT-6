# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:51:40 2022

@author: LENOVO
"""

import pandas as pd
import numpy as np
df=pd.read_csv("bank-full.csv",sep=';')
df
df.head()
df.isnull().sum()
# There are no null values
df.dtypes
df.columns
df.duplicated()
df[df.duplicated()] 
# There are no duplicates in data
df.shape
df.info()

# Data visualization
df.boxplot("age",vert=False)
Q1=np.percentile(df["age"],25)
Q3=np.percentile(df["age"],75)
IQR=Q3-Q1
LW=Q1-(2.5*IQR)
UW=Q3+(2.5*IQR)
df["age"]<LW
df[df["age"]<LW].shape
df["age"]>UW
df[df["age"]>UW].shape
df["age"]=np.where(df["age"]>UW,UW,np.where(df["age"]<LW,LW,df["age"]))
#
df.boxplot("balance",vert=False)
Q1=np.percentile(df["balance"],25)
Q3=np.percentile(df["balance"],75)
IQR=Q3-Q1
LW=Q1-(2.5*IQR)
UW=Q3+(2.5*IQR)
df["balance"]<LW
df[df["balance"]<LW].shape
df["balance"]>UW
df[df["balance"]>UW].shape
df["balance"]=np.where(df["balance"]>UW,UW,np.where(df["balance"]<LW,LW,df["balance"]))
#
df.boxplot("day",vert=False)
#
df.boxplot("duration",vert=False)
Q1=np.percentile(df["duration"],25)
Q3=np.percentile(df["duration"],75)
IQR=Q3-Q1
LW=Q1-(2.5*IQR)
UW=Q3+(2.5*IQR)
df["duration"]<LW
df[df["duration"]<LW].shape
df["duration"]>UW
df[df["duration"]>UW].shape
df["duration"]=np.where(df["duration"]>UW,UW,np.where(df["duration"]<LW,LW,df["duration"]))
#
df.boxplot("campaign",vert=False)
Q1=np.percentile(df["campaign"],25)
Q3=np.percentile(df["campaign"],75)
IQR=Q3-Q1
LW=Q1-(2.5*IQR)
UW=Q3+(2.5*IQR)
df["campaign"]<LW
df[df["campaign"]<LW].shape
df["campaign"]>UW
df[df["campaign"]>UW].shape
df["campaign"]=np.where(df["campaign"]>UW,UW,np.where(df["campaign"]<LW,LW,df["campaign"]))

# Splitting the variables
X1=df[["age","balance","day","duration","campaign","pdays","previous"]]
X1.dtypes
X1.corr()
X1.corr().to_csv("logicorr.csv")
X2=df[["job","marital","education","default","housing","loan","contact","month","poutcome"]]
X=pd.concat([X1,X2],axis=1)
X.head()
list(X)

# Standardization
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
LE=LabelEncoder()
MM=MinMaxScaler()
X["job"]=LE.fit_transform(X["job"])
X["job"]=pd.DataFrame(X["job"])

X["marital"]=LE.fit_transform(X["marital"])
X["marital"]=pd.DataFrame(X["marital"])

X["education"]=LE.fit_transform(X["education"])
X["education"]=pd.DataFrame(X["education"])

X["default"]=LE.fit_transform(X["default"])
X["default"]=pd.DataFrame(X["default"])

X["housing"]=LE.fit_transform(X["housing"])
X["housing"]=pd.DataFrame(X["housing"])

X["loan"]=LE.fit_transform(X["loan"])
X["loan"]=pd.DataFrame(X["loan"])

X["contact"]=LE.fit_transform(X["contact"])
X["contact"]=pd.DataFrame(X["contact"])

X["month"]=LE.fit_transform(X["month"])
X["month"]=pd.DataFrame(X["month"])

X["poutcome"]=LE.fit_transform(X["poutcome"])
X["poutcome"]=pd.DataFrame(X["poutcome"])

X["age"]=MM.fit_transform(X[["age"]])
X["balance"]=MM.fit_transform(X[["balance"]])
X["day"]=MM.fit_transform(X[["day"]])
X["duration"]=MM.fit_transform(X[["duration"]])
X["campaign"]=MM.fit_transform(X[["campaign"]])
X["pdays"]=MM.fit_transform(X[["pdays"]])
X["previous"]=MM.fit_transform(X[["previous"]])

X

Y=LE.fit_transform(df["y"])
Y=pd.DataFrame(Y)

from sklearn.preprocessing import StandardScaler
SS=StandardScaler()
X=SS.fit_transform(X)
X=pd.DataFrame(X)

# Train and Test
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

# Model fitting
from sklearn.linear_model import LogisticRegression
LR=LogisticRegression()
LR.fit(X_train,Y_train)
Y_predtrain=LR.predict(X_train)
Y_predtest=LR.predict(X_test)

# Metrics
from sklearn.metrics import accuracy_score, f1_score, log_loss
ac1=accuracy_score(Y_train,Y_predtrain)
ac2=accuracy_score(Y_test,Y_predtest)

fs1 = f1_score(Y_train,Y_predtrain)
fs2 = f1_score(Y_test,Y_predtest)

LL1=log_loss(Y_train,Y_predtrain)
LL2=log_loss(Y_test,Y_predtest)
