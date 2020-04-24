# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:56:25 2020

@author: user
"""

"""

Q4. tree_addhealth.csv
For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set,
 an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina’s Carolina Population Center, 
http://www.cpc.unc.edu/projects/addhealth/data.

 

Import tree_addhealth.csv

 

The attributes are:

 

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale
 
Build a classification tree model evaluating if an adolescent would smoke
 regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, 
 Black, Native American and Asian, alcohol use, alcohol problems, marijuana 
 use, cocaine use, inhalant use, availability of cigarettes in the home, 
 depression, and self-esteem.

Build a classification tree model evaluation if an adolescent gets expelled 
or not from school based on their Gender and violent behavior.
Use random forest in relation to regular smokers as a target and explanatory 
variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each 
and every section)


"""









--------------------------------------------------------------------------------------------------------------------


#cigrate available in home accuracy


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

# This is  a regression problem
dataset = pd.read_csv('tree_addhealth.csv')  

#data analysis
dataset.shape


# Checking for Categorical Data
dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)

age_mean = dataset["age"].mean()
dataset["age"] = dataset["age"].fillna(age_mean)



features = dataset.loc[:,['BIO_SEX', 'HISPANIC', 'WHITE', 'BLACK', 'NAMERICAN', 'ASIAN', 'age', 'ALCEVR1', 'ALCPROBS1', 'marever1', 'cocever1', 'inhever1','TREG1']].values  
labels = dataset['cigavail'].values

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

# Model Score = 0.7222222222222222 times out of 100 model prediction was RIGHT
print((cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))




#Output  --->  we have get 72.22% accurecy of model








-------------------------------------------------------------------------------------------------------









"""

Build a classification tree model evaluating if an adolescent would smoke
 regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, 
 Black, Native American and Asian, alcohol use, alcohol problems, marijuana 
 use, cocaine use, inhalant use, availability of cigarettes in the home, 
 depression, and self-esteem.
 
 """

#here we need to find that smoke regularly or not accruracy
 
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

# This is  a regression problem
dataset = pd.read_csv('tree_addhealth.csv')  

#data analysis
dataset.shape


# Checking for Categorical Data
dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)

age_mean = dataset["age"].mean()
dataset["age"] = dataset["age"].fillna(age_mean)



features = dataset.loc[:,['BIO_SEX', 'HISPANIC', 'WHITE', 'BLACK', 'NAMERICAN', 'ASIAN', 'age', 'ALCEVR1', 'ALCPROBS1', 'marever1', 'cocever1', 'inhever1','cigavail']].values  
labels = dataset['TREG1'].values

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

# Model Score = 0.7222222222222222 times out of 100 model prediction was RIGHT
print((cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))












-------------------------------------------------------------------------------------------------------------------------------













 

"""
Build a classification tree model evaluation if an adolescent gets expelled 
or not from school based on their Gender and violent behavior.
Use random forest in relation to regular smokers as a target and explanatory 
variable specifically with Hispanic, White, Black, Native American and Asian.

"""






import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

# This is  a regression problem
dataset = pd.read_csv('tree_addhealth.csv')  

#data analysis
dataset.shape


# Checking for Categorical Data
dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)

age_mean = dataset["age"].mean()
dataset["age"] = dataset["age"].fillna(age_mean)

dataset.columns


features = dataset.loc[:,['BIO_SEX', 'HISPANIC', 'WHITE', 'BLACK', 'NAMERICAN', 'ASIAN', 'age']].values  
labels = dataset['EXPEL1'].fillna(0)


# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20)  

# Training and making predictions 
from sklearn.ensemble import RandomForestClassifier


classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
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




 
 
 
 
 
 
 




