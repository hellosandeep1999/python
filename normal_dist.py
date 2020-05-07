# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:10:48 2020

@author: user
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""






import matplotlib.pyplot as plt
import numpy as np
dist = np.random.normal(150, 20, 1000)

print("Standard Deviation is: ", np.std(dist))
print("Variance value is: ",np.var(dist))


plt.hist(dist,100)
plt.show()
