# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:11:48 2020

@author: user
"""

"""
Q1. (Create a program that fulfills the following specification.)
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

import pandas as pd
import numpy as np

df = pd.read_csv("iq_size.csv")

print(df.dtypes)

#check the datset have null value or not 
#if it is have null then we need to handle it.

df.isnull().any(axis=0)

#here we need to seprate features and labels

features = df.iloc[:,1:].values
label = df.iloc[:,0].values 

from sklearn.model_selection import train_test_split

features_train,features_test,label_train,label_test = train_test_split(features,label,test_size = 0.2, random_state=0)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(features_train,label_train)

pred = reg.predict(features_test)

print(pd.DataFrame(zip(pred,label_test)))

x = [90,70,150]

x = np.array(x)
x = x.reshape(1,3)
reg.predict(x)


#OutPut:
    
#   reg.predict(x)
#   array([105.76890364])













