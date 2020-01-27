# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:32:22 2020

@author: user
"""

a = input("Enter some numbers: ").split(",")
b = []

for i in a:
    b.append(int(i))
print(b)
c = tuple(b)
print(c)
