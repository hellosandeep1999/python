# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:17:46 2020

@author: user
"""

a = [12,24,35,24,88,120,155,88,120,155]
b = []
for i in a:
     if i not in b:
         b.append(i)
b.reverse()
print(b)             
