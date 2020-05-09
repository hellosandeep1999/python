# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:11:34 2020

@author: user
"""

"""

Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. 
The researchers (Cook and Weisberg, 1999) measured and recorded the following 
data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Polynomial nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial 
    regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking 
into account a quadratic function of the age of the fish.



"""

#By using LinearRegression for ckecking Algorithm (which is best Algorithm ? )
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('bluegills.csv')
dataset.ndim
dataset.shape

# Check for categorical data
dataset.dtypes 

# Check for missing data
dataset.isnull().any(axis=0)


# Seperate features and labels
features = dataset.iloc[:, [0]].values
print(features)

labels = dataset.iloc[:, [1]].values
print(labels)


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)



# Predicting the Test set results
Pred = regressor.predict(features_test)


print (pd.DataFrame(zip(Pred, labels_test)))

#total sum of difference of pred and Labels_test 
print(sum(Pred-labels_test))  # if want to check from both algorithm and find that which algorithm is giving minimum value

#output :-  [-23.48651924]




                    --------     ----------      ----------     ---------

# By using LinearRegression for ckecking Algorithm (which is best Algorithm ? )



from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
print(features.shape)

features_poly = poly_object.fit_transform(features)
print(features_poly)
print(features_poly.shape) # x0 x1 x2 x3 x4 x5    





from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features_poly, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)



# Predicting the Test set results
Pred = regressor.predict(features_test)


print (pd.DataFrame(zip(Pred, labels_test)))


#total sum of difference of pred and Labels_test 
print(sum(Pred-labels_test))  # if want to check from both algorithm and find that which algorithm is giving minimum value

#Output :- [18.2878819]

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

NOTE :- By linear_Regression ->  [-23.48651924]
        By Polynomial_Linear_Regression ->  [18.2878819]
        
        So we can consider that polynomial_linear_regression is best suitable for this problem.
 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

------------------------------------------------------------------------------------------------------------------------------





"""


What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.
"""




from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
print(features.shape)

features_poly = poly_object.fit_transform(features)
print(features_poly)
print(features_poly.shape)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)


print ("Predicting result with Polynomial Regression")
print (lin_reg_2.predict(poly_object.transform([[5]])))

#Output: - [[166.125]]


plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()











