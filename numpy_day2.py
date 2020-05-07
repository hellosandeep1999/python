# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:17:14 2020

@author: user
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""



import numpy as np

numbers = input("Enter 9 number with space: ").split()
if len(numbers) == 9:
    numbers = list(map(int,numbers))
    numbers = np.array(numbers)
    numbers = numbers.reshape(3,3)
    print(numbers)
else:
    print("number should be 9 only")











-------------------------------------------------------------------------------------------------------------


"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""





import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
                          
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

plt.hist(incomes,50)
plt.show()



        






----------------------------------------------------------------------------------------------
    
    




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











---------------------------------------------------------------------------------------------







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








