# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:34:57 2020

@author: user

"""
"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K


---------------------------------------------------------------------------------------------------------
"""


#1. Which Male and Female Professor has the highest and the lowest salaries




import pandas as pd

df = pd.read_csv("Salaries.csv")

for_M = df.loc[(df['rank'] == 'Prof') & (df['sex'] == 'Male' ) & df['salary']]

for_F = df.loc[(df['rank'] == 'Prof') & (df['sex'] == 'Female' ) & df['salary']]

print(for_M.max())
print(for_M.min())
print(for_F.max())
print(for_F.min())

-------------------------------------------------------------------------------------------------

"""

2. Which Professor takes the highest and lowest salaries.

"""
sal = df.loc[(df['rank'] == 'Prof') & df['salary']]

print(sal.max())
print(sal.min())




----------------------------------------------------------------------------------------------------
"""

3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
   
"""
mis = df[df['salary'].isnull()]

for i in mis["service"]:
    mean_sal = df.loc[(df['service'] == i) & df['salary']].mean()
    df[df['service'] == i] = df[df['service'] == i].fillna(mean_sal)

    
---------------------------------------------------------------------------------------------------
"""

4. Missing phd - should be mean of the matching service 

"""



mis_phd = df[df['phd'].isnull()]

for i in mis_phd["service"]:
    mean_phd = df.loc[(df["service"] == 33) & df['phd']].mean()[0]
    df[df['service'] == i] = df[df['service'] == i].fillna(mean_phd)


--------------------------------------------------------------------------------------------------
"""

5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
   
   
"""

male1 = df.loc[(df['sex'] == 'Female')]
male2 = df.loc[(df['sex'] == 'Male')]
print(male1.count()[4])
print(male2.count()[4])

import matplotlib.pyplot as plt
labels = 'Female','Male'
sizes = [male1.count()[4],male2.count()[4]]
colors = ['gold','yellowgreen']
explode = [0,0]
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=180)
plt.axis("equal")
plt.show()



-------------------------------------------------------------------------------------------------

"""
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
   
"""
print("Total Professor",df['rank'].value_counts(dropna = False)[0])
print("Total AsstProf",df['rank'].value_counts(dropna = False)[1])
print("Total AssocProf",df['rank'].value_counts(dropna = False)[2])

import matplotlib.pyplot as plt
labels = 'Professor','AsstProf','AsstProf'
sizes = [df['rank'].value_counts(dropna = False)[0],df['rank'].value_counts(dropna = False)[1],df['rank'].value_counts(dropna = False)[2]]
colors = ['gold','yellowgreen','lightcoral']
explode = [0,0.5,0]
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=180)
plt.axis("equal")
plt.show()
   


-------------------------------------------------------------------------------------------------   
"""

7. Who are the senior and junior most employees in the organization.

"""

df[(df["service"] == df['service'].max()) | (df["service"] ==df['service'].min())]





-------------------------------------------------------------------------------------------------------
"""


8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
   

"""
import matplotlib.pyplot as plt
customerWaitTime = list(df["salary"])
customerWaitTime.sort()

plt.style.use('ggplot')
plt.hist(customerWaitTime,bins=[50000,65000,80000,95000,110000,125000,140000,155000,170000,185000,200000]) 

#plt.axis([50000,250000, 0, 10]) 
plt.xlabel('salary')
plt.ylabel('prof,asscprof,assocprof')


--------------------------------------------------------------------------------------------------















   
   
   
   
   
   
   
   
   
   








































