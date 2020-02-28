# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:04:18 2020

@author: user
"""
-------------------------------------------------------------------------------------

"""
How many people in the given training set survived the disaster ?

"""
import pandas as pd

df1 = pd.read_csv("training_titanic.csv")

print("people in the given training set survived the disaster: ",df1[df1["Survived"] == 1].count()[1])

-------------------------------------------------------------------------------------------





"""

How many people in the given training set died ?

"""
import pandas as pd

df1 = pd.read_csv("Desktop/New folder/training_titanic.csv")

print("people in the given training set survived the disaster: ",df1[df1["Survived"] == 0].count()[1])






-----------------------------------------------------------------------------------------------







"""
Calculate and print the survival rates as proportions (percentage)

"""
import pandas as pd

df1 = pd.read_csv("Desktop/New folder/training_titanic.csv")

print('the survival rates as proportions: ',"%.2f"%((df1[df1["Survived"] == 1].count()[1])*(100/df1.count()[1]))+"%")







----------------------------------------------------------------------------------------------







"""

by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
"""



print("Male & Female that are survived:\n ",df1[(df1["Survived"] == 1)]['Sex'].value_counts(normalize = True))
print("----------------------------")
print("Male & Female that are died:\n ",df1[(df1["Survived"] == 0)]['Sex'].value_counts(normalize = True))





-----------------------------------------------------------------------------------------------------





"""
     Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
 """ 
    
    
df1["Child"] = df1["Age"].map(lambda x : 1 if x <= 18 else 0)

df1[(df1["Child"] == 1)]['Survived'].value_counts(normalize = True)

   
"""

  
    
    
    
    
    
    
    
    
    
    




















