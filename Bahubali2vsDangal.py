# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:48:11 2020

@author: user
"""


# Approch 1



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = int(input("Enter a number:  "))
dataset = pd.read_csv("Bahubali2_vs_Dangal.csv")

features = dataset.iloc[:,:-2]
labels1 = dataset.iloc[:,1:-1]
labels2 = dataset.iloc[:,2:]
from sklearn.linear_model import LinearRegression

reg1 = LinearRegression()
reg2 = LinearRegression()

reg1.fit(features,labels1)
reg2.fit(features,labels2)

plt.scatter(features,labels1,color="red")
plt.scatter(features,labels2,color="red")

plt.plot(features,reg.predict(features),color="Blue")
plt.plot(features,reg.predict(features),color="Blue")

a = reg1.predict([[x]])
b = reg2.predict([[x]])

if a > b:
    print("Bahubali2 collection of",x,"th day will be maximum = ",a)
else:
    print("Dangal collection of",x,"th day will be maximum = ",b)



