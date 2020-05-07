# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:09:58 2020

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
