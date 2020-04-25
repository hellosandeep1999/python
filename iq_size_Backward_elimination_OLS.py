# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:52:20 2020

@author: user
"""
"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
""" 


# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('iq_size.csv')
dataset.ndim
dataset.shape

# Check for categorical data
dataset.dtypes 

# Check for missing data
dataset.isnull().any(axis=0)


# Seperate features and labels
features = dataset.iloc[:, 1:].values
print(features)

labels = dataset.iloc[:, [0]].values
print(labels)


#it is to remove they columns which are not effect on our model.

import statsmodels.api as sm
import numpy as np

features_obj = features[:, [0,1,2]]
features_obj = sm.add_constant(features_obj)
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break


#In Features_obj we get only one column(Brain) which is most important for our dataset. 




# NOTE: - Using Polynomial algorithm.
        
#so now we will take Polinomial algorithm and we do solve now.


features = dataset.iloc[:,[1]].values #In Features_obj we get only one column(Brain) which is most important for our dataset.
print(features)

labels = dataset.iloc[:, [0]].values
print(labels)


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
print(features.shape)

features_poly = poly_object.fit_transform(features)
print(features_poly)
print(features_poly.shape) # x0 x1 x2 x3 x4 x5    


# Algo is same for Polynomial Regression, its only the data format is changed
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)


# This will give error dim1 != dim 6
# We need to convert the data into polynomial format
#print (lin_reg_2.predict([[1981]]))



print ("Predicting result with Polynomial Regression")
print (lin_reg_2.predict(poly_object.transform([[90]]))) #if our Brain Size =90

#Output:- [[100.32445269]]

# This value has huge difference from the Linear Regression 
# But if we visualize it, we will come to know that Poly is better predictions



# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()













