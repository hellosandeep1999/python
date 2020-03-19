# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:47:32 2020

@author: user
"""

"""
Q2. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""






"""
Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
"""


# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Female_Stats.Csv')

# Check data Types for each columns
print(dataset.dtypes)

# Seperate Features and Labels
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, [0]].values

# Check Column wise is any data is missing or NaN
dataset.isnull().any(axis=0)

# Check data Types for each columns
print(dataset.dtypes)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

Pred = regressor.predict(features_test)

print (pd.DataFrame(zip(Pred, labels_test)))

#eg1 :
x = [75,75]
x = np.array(x)
x = x.reshape(1,2)
Pred1 = regressor.predict(x)


---------------------------------------------------------------------------------------------------------------





"""

When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.

"""


# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Female_Stats.Csv')

# Check data Types for each columns
print(dataset.dtypes)

# Seperate Features and Labels
features = dataset.iloc[:,[1]].values
labels = dataset.iloc[:, [0]].values

# Check Column wise is any data is missing or NaN
dataset.isnull().any(axis=0)

# Check data Types for each columns
print(dataset.dtypes)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

Pred = regressor.predict(features_test)

print (pd.DataFrame(zip(Pred, labels_test)))




---------------------------------------------------------------------------------------------------------------------------


"""

When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.



"""


import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Female_Stats.Csv')

# Check data Types for each columns
print(dataset.dtypes)

# Seperate Features and Labels
features = dataset.iloc[:,[2]].values
labels = dataset.iloc[:, [0]].values

# Check Column wise is any data is missing or NaN
dataset.isnull().any(axis=0)

# Check data Types for each columns
print(dataset.dtypes)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

Pred = regressor.predict(features_test)

print (pd.DataFrame(zip(Pred, labels_test)))

























