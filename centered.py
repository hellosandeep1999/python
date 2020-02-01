# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:37:47 2020

@author: user
"""
import math
import numpy 
inp = input("Enter a list of numbers: ").split()
c = []
for i in inp:
    c.append(int(i))
c.remove(min(c))
c.remove(max(c))
print("Centered Average : ",numpy.mean(c))







