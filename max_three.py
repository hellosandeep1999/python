# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:42:34 2020

@author: user
"""

#max of Threee number


a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

max = a if a>b>c else b if b>c else c
print(max)
