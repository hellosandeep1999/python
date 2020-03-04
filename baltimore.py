# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:14:48 2020

@author: user
"""
"""
 remove the dollar signs in the AnnualSalary field and assign it as a int
 
 
"""


import pandas as pd

df4 = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

df4["AnnualSalary"] = df4["AnnualSalary"].astype("int64")



"""

Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
Sort the data and display to show who get the highest salary
       
"""
df4[["AnnualSalary","JobTitle"]]
df4["AnnualSalary"].agg(['sum','mean'])

a = sorted(df4["AnnualSalary"])

df4["AnnualSalary"].max()

df4["AnnualSalary"].min()




"""

Try to group on JobTitle only and sort the data and display


"""
sorted(df4["JobTitle"])


"""

How many employess are there for each JobRoles and Graph it

"""
import matplotlib.pyplot as plt
plt.pie(df4["JobTitle"].value_counts(),labels = df4["JobTitle"].unique(),autopct = "%.2f",radius = 3)

"""

Graph and show which Job Title spends the most

"""


import matplotlib.pyplot as plt
plt.pie(df4["HireDate"].value_counts(dropna = False),labels = df4["HireDate"].unique(),autopct = "%.2f",radius = 3)

























