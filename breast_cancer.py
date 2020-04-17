# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:06:56 2020

@author: user
"""



"""
Code Challenges

Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)----> represented by column A.

Clump Thickness (1 – 10) ----> represented by column B.
Uniformity of Cell Size(1 - 10)----> represented by column C.
Uniformity of Cell Shape (1 - 10)----> represented by column D.
Marginal Adhesion (1 - 10)----> represented by column E.
Single Epithelial Cell Size (1 - 10)----> represented by column F.
Bare Nuclei (1 - 10)----> represented by column G.
Bland Chromatin (1 - 10)----> represented by column H.
Normal Nucleoli (1 - 10)----> represented by column I.
Mitoses (1 - 10)----> represented by column J.
Class: (2 for Benign and 4 for Malignant)----> represented by column K.
 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.


Impute the missing values with the most frequent values.

Perform Classification on the given data-set to predict if the tumor is 
cancerous or not.

Check the accuracy of the model.

Predict whether a women has Benign tumor or Malignant tumor, 
if her Clump thickness is around 6, uniformity of cell size is 2, 
Uniformity of Cell Shape is 5, Marginal Adhesion is 3, 
Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, 
Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)



"""


----------------------------------------------------------------------------------------------------









"""
Impute the missing values with the most frequent values.

"""








import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("breast_cancer.csv")


dataset.isnull().any(axis=0)

#here we know that column "G" is have null values so we need fill it by most fequent values.

Most_frequently_values = dataset["G"].value_counts().idxmax()
dataset["G"] = dataset["G"].fillna(Most_frequently_values)

#now we will again check for missing values
dataset.isnull().any(axis=0)

#differentiat the features and labels
features = dataset.iloc[:, 1:-1].values
labels = dataset.iloc[:, -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)


# Fitting Kernel SVM to the Training set
# kernels: linear, rbf and poly
# If you want you can make your own customized function to convert 2D to 3D
# Poly takes alot of time to create the visualisation 
# Linear will draw a straight line
# run the code 3 times with 3 different kernel function 

from sklearn.svm import SVC
# SVM ( SVC for classification and SVR for Regression )
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Comparing the predicted and actual values
my_frame= pd.DataFrame(labels_pred, labels_test)
print(my_frame)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)









"""

Check the accuracy of the model.

"""




# Model Score
print( (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))

# Model Score
score = classifier.score(features_test,labels_test)
print(score)

#Check the accuracy of the model.  ---->  0.9285714285714286














-------------------------------------------------------------------------------







"""
Predict whether a women has Benign tumor or Malignant tumor, 
if her Clump thickness is around 6, uniformity of cell size is 2, 
Uniformity of Cell Shape is 5, Marginal Adhesion is 3, 
Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, 
Normal Nuclei is 2 and Single Epithelial Cell Size is 2

"""




labels_pred = classifier.predict([[6,2,5,3,2,7,9,2,4]])
print(labels_pred) #it gives [4] it means it have cancerous tumor


















