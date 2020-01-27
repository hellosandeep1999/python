# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:04:42 2020

@author: user
"""

inp = input("Enter input: ")
k = 0
p = 0
for i in inp:
    if i.isalpha():
        k += 1
    elif i.isdigit():
        p +=1
print(k)
print(p)

