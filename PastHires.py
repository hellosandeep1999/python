# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:58:08 2020

@author: user
"""



#Mathod - 1




"""

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your 
    prediction is for a being hired.
    
    
"""







import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

dataset = pd.read_csv("PastHires.csv")  

#data analysis
dataset.shape

# Checking for Categorical Data
# Best part is that DT and RF works on the categorical data also
# We do not need to perform the Label encoding for it, Algo does it internally 

dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)


# Preparing the dataset
# This technique of dropping can be used when the label is in between features
features = dataset.drop('Hired', axis=1)
features = features.values

# Label Encoding for Features



# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

#For Column --->  Employed?
features[:, 1] = labelencoder.fit_transform(features[:, 1])

#For Column --->  Level of Education
features[:, 3] = labelencoder.fit_transform(features[:, 3])

#For Column --->  Top-tier school
features[:, 4] = labelencoder.fit_transform(features[:, 4])

#For Column --->  Internet
features[:, 5] = labelencoder.fit_transform(features[:, 5])


#we need to onehotencoding for this column
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [3])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]




# Label Encoding for Features
labels = dataset['Hired']  
labels = labels.values

#For Column --->  Hired
labels = labelencoder.fit_transform(labels)



# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20)  

# Training and making predictions 
# We need to be careful in using DecissionTreeClassifier or DecissionTreeRegressor
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)


labels_pred = classifier.predict(features_test) 

# Comparing the predicted and actual values
my_frame= pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})
print(my_frame)


# Evaluating score
# For classification tasks some commonly used metrics are confusion matrix, 
# precision, recall, and F1 score.
from sklearn.metrics import confusion_matrix  
cm = confusion_matrix(labels_test, labels_pred)
print(cm)  

# Model Score = 100% times out of 100 model prediction was RIGHT
print((cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))


#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))


#So we have here for decision Tree


----------------------------------------------------------------------------------------------------------------






#Now we will take Random Forest and solve it



"""
Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to 
    top-tire school, having Bachelor's Degree without Internship.
"""




import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

dataset = pd.read_csv("PastHires.csv")  

#data analysis
dataset.shape

# Checking for Categorical Data
# Best part is that DT and RF works on the categorical data also
# We do not need to perform the Label encoding for it, Algo does it internally 

dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)


# Preparing the dataset
# This technique of dropping can be used when the label is in between features
features = dataset.drop('Hired', axis=1)
features = features.values

# Label Encoding for Features



# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

#For Column --->  Employed?
features[:, 1] = labelencoder.fit_transform(features[:, 1])

#For Column --->  Level of Education
features[:, 3] = labelencoder.fit_transform(features[:, 3])

#For Column --->  Top-tier school
features[:, 4] = labelencoder.fit_transform(features[:, 4])

#For Column --->  Internet
features[:, 5] = labelencoder.fit_transform(features[:, 5])


#we need to onehotencoding for this column
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [3])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]




# Label Encoding for Features
labels = dataset['Hired']  
labels = labels.values

#For Column --->  Hired
labels = labelencoder.fit_transform(labels)



# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20)





#train the model
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  



# Now we will predict with some data that this employe will Hired or not?
# so our features = [0,0,10,1,4,1,0]
 
labels_pred = classifier.predict([[0,0,10,1,4,1,0]]) # we predict that Employee will be hired -->array([1])






"""

Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any 
top-tire school, having Master's Degree with Internship. 

[1,0,10,0,4,0,1]


"""


labels_pred = classifier.predict([[1,0,10,0,4,0,1]])   # we predict that Employee will be hired -->array([1])








----------------------------------------------------------------------------------------------------------------






















#Mathod - 2




"""Here, we are building a decision tree to check if a person is hired or
 not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale 
of 0-2.

Build and perform Decision tree based on the predictors and see how accurate 
your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific 
candidate profiles:

Predict employment of a currently employed 10-year veteran, previous 
employers 4, went to top-tire school, having Bachelor's Degree without Internship.

Predict employment of an unemployed 10-year veteran, ,previous employers 4, 
didn't went to any top-tire school, having Master's Degree with Internship.

filename "PastHires.py"

"""
import pandas as pd

df = pd.read_csv("PastHires.csv")
col = df.columns[[1,4,5,6]]

for i in col:
    df[i][df[i]=='Y'] = 1
    df[i][df[i]=='N']=0

d = {"BS":0,"MS":1,"PhD":2}
df["Level of Education"] = df["Level of Education"].map(d)

x = df[df.columns[:6]]
y = df["Hired"]

from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor(random_state=0)
dtr = dtr.fit(x,y)
D_pred = dtr.predict(x)

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators=10)
rfr = rfr.fit(x,y)
R_pred = rfr.predict(x)

#Predict employment of an employed 10-year veteran
emp = rfr.predict([[10, 1, 4, 0, 0, 0]])

print ("\n")
print ("chances of getting hired for currently employed person is : "+str(emp[0]*100)+"%")
print ("\n")

#...and an unemployed 10-year veteran
un_emp = rfr.predict([[10, 0, 4, 0, 0, 0]])

print ("chances of getting hired for currently un-employed person is : "+str(un_emp[0]*100)+"%")

















