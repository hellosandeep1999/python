# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:10:39 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('mushrooms.csv')
features = dataset.iloc[:,[5,21,22]].values
labels = dataset.iloc[:, [0]].values

dataset.isnull().any(axis=0)


#For label ---> Label encoding
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder

# Create objct of LabelENcoder
labelencoder = LabelEncoder()

# Fit and Use the operation Transform
labels[:, 0] = labelencoder.fit_transform(labels[:, 0])   #poisonous = 1, eldible = 0



#For features ----> Label Encoding
for i in range(3):
    features[:, i] = labelencoder.fit_transform(features[:, i])


#onehotEncoding
#For features   -----> onehotEncoding
from sklearn.preprocessing import OneHotEncoder
# Creation of Object




#for ---->  column = 0
onehotencoder = OneHotEncoder(categorical_features = [0])
# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]




#for ---->  column = 1
onehotencoder = OneHotEncoder(categorical_features = [8])
# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]





#for ---->  column = 2
onehotencoder = OneHotEncoder(categorical_features = [13])
# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]





from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)



# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

labels_train = labels_train.astype(float)
# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)







#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)
labels_test = labels_test.astype(float)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)




"""
Output:-
[[1056    0]
 [  10  965]]


accuracy of model = 0.9950763170851797


"""


















