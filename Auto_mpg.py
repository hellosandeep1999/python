# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 08:00:16 2020

@author: user
"""

"""

Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight",
    "acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 
    22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)




"""


# first we need to convert .txt file into .csv file so using file handling we will

 
import pandas as pd
fp = open(r'Auto_mpg.txt','r')
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
while(True):
    data=fp.readline()
    print(data)
    if data!='':
#         a,b,c,d,e,f,g,h,i=data.split()
        a.append(data.split()[0])
        b.append(data.split()[1])
        c.append(data.split()[2])
        d.append(data.split()[3])
        e.append(data.split()[4])
        f.append(data.split()[5])
        g.append(data.split()[6])
        h.append(data.split()[7])
        i.append(data.split()[8])
        
    else:
        break
# print() 
df=pd.DataFrame(zip(a,b,c,d,e,f,g,h,i))
# pd.to_csv('auto_mpg.csv')
df.to_csv('Auto_mpg.csv', encoding='utf-8')

------------------------------------------------------------




"""

Give the column names as "mpg", "cylinders", "displacement","horsepower","weight",
    "acceleration", "model year", "origin", "car name" respectively
    
"""


#now from here we will solve the problem 

#*************Most Step******************
#go on csv file and delete the first index row and column for our dataset



import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt



col_names = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
dataset = pd.read_csv("Auto_mpg.csv",names=col_names, header=None)








---------------------------------------------------------------------------------------


"""

Display the Car Name with highest miles per gallon value


"""
dataset[dataset["mpg"] == dataset["mpg"].max()]["car name"]





--------------------------------------------------------------------------------------









"""
Build the Decision Tree and Random Forest models and find out which of the two is more accurate 
in predicting the MPG value

"""

dataset = pd.read_csv("Auto_mpg.csv") 


dataset.isnull().any(axis=0)


# Preparing the dataset
# This technique of dropping can be used when the label is in between features
features = dataset.iloc[:,[1,2,3,4,5,6,7]].values


  
labels = dataset.iloc[:,0].values


# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20)  

# Training and making predictions 
# We need to be careful in using DecissionTreeClassifier or DecissionTreeRegressor

#this predoiction from decision tree
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

# Model Score = 98.90 times out of 100 model prediction was RIGHT
print((cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))









#And this prection from random forest


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

# Model Score = 98.90 times out of 100 model prediction was RIGHT
print( (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))


#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))



#Output  --->  than will find a best accuracy of algo.





--------------------------------------------------------------------------------------------------



"""

Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 
    22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)


"""
























