# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:06:04 2020

@author: user
"""
n = int(input("Enter number of person:"))
b = []
for i in range(n):
    a = input("Enter name, age , height: ").split(',')
    g = [a[0],int(a[1]),int(a[2])]
    c = tuple(g)
    b.append(c)
b.sort()
print(b)

