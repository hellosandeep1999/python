# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:59:47 2020

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("student_scores.csv")

print(data.shape)
print(data.ndim)
print(data.head())
print(data.describe())

print(data.dtypes)
data.isnull().any(axis = 0)

plt.boxplot(data.values)


x = [0,1,2,3,4,5]
y = [0,1,2,3,4,5]
plt.axis([0,6,0,6])

plt.scatter(x,y)

plt.plot(x,y)


data.plot(x = 'Hours',y='Scores',style='o')
plt.title("Hours And Percentage")
plt.xlabel("hours")
plt.ylabel("scores")
plt.show()


features = data.iloc[:,:-1]

print(type(features))

print(type(features.values))

features = data.iloc[:,:-1].values
label = data.iloc[:,1:].values



from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(features,label)

print(reg.coef_)
print(reg.intercept_)

print(reg.predict([[100]]))

plt.scatter(features,label,color="red")

plt.plot(features,reg.predict(features),color = "blue")




features = data.iloc[:,:-1].values
labels = data.iloc[:,1].values


from sklearn.model_selection import train_test_split

features_train,features_test,label_train,label_test = train_test_split(features,labels,test_size = 0.2, random_state = 41)      

from sklearn.linear_model import LinearRegression
regg = LinearRegression()
regg.fit(features_train,label_train)

print(regg.intercept_)
print(regg.coef_)


pred_label = regg.predict(features_test)

df = pd.DataFrame({"Actual":label_test,"Predict":pred_label})


X, y = np.arange(10).reshape((5, 2)), list(range(5))












