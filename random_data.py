# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:26:14 2020

@author: user
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""


#Create a random array of 40 integers from 5 - 15 using NumPy. 

import numpy as np 
x = np.random.randint(5, 15, 40)

# Find the most frequent value with Numpy.
print("Most frequent value in the above array :",np.bincount(x).argmax())

#Find the most frequent value without Numpy
from collections import Counter
b = Counter(x)
print(b.most_common(1))
