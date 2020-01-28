# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:17:25 2020

@author: user
"""

a = [1,3,6,78,35,55,88]
b = [12,24,35,24,88,120,155]
s1 = set(a)
s2 = set(b)

s1.intersection(s2)


'''


c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)


'''            