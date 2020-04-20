# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:38:12 2020

@author: user
"""


import numpy as np 
import pandas as pd 
import sklearn
import seaborn as sns
from sklearn.preprocessing import StandardScaler
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



#Import dataset and create a dataframe
data = pd.read_csv("kc_house_data.csv")
data.head()
features = data.loc[:,['bedrooms', 'bathrooms', 'sqft_living','sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade','sqft_basement','lat', 'long', 'sqft_living15', 'sqft_lot15']]

labels = data.loc[:,["price"]]
#Create train and test data with 70o/o and 30°/o split
features_train, features_test, labels_train,labels_test	=	train_test_split(features, labels, test_size=0.3, random_state=1)

features_train.shape

features_test.shape

labels_train.shape
labels_test.shape



#Let's import the Lasso, Ridge, Elasticnet regression object and define model 
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso 
from sklearn.linear_model import Ridge  # RidgeClassier is also there
from sklearn.linear_model import ElasticNet
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 


#Fit a model on the train data
lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
lm_elastic.fit(features_train, labels_train)


#Evaluate the model
plt.figure (figsize= (15,10))

ft_importances_lm .plot(kind = 'barh')
plt.show()


#R2 Value

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (lm .score(features_test,labels_test)*100,2))

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lm_elastic.score(features_test,labels_test)*100,2))

#Predict on test and training data

predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)
predict_test_elastic = lm_elastic.predict(features_test)

#Print the Loss Funtion - MSE & MAE

import numpy as np
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

print ("ElasticNet Mean Square Error (MSE) for TEST data is")
print (np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2))
