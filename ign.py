# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:27:22 2020

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("ign.csv")



"""

 Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
"""

df3 = dataset[(dataset["platform"] == "Xbox One") & (df3["score"] > 7)]


"""

review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   """
   

x = dataset[(dataset["platform"] == "PlayStation 4")]
y = dataset[(dataset["platform"] == "Xbox One")]



plt.hist(x["score"],bins=[0,2,4,6,8,10]) 
plt.xlabel('distance')
plt.ylabel('number')

plt.hist(y["score"],bins=[0,2,4,6,8,10]) 
plt.xlabel('distance')
plt.ylabel('number')























