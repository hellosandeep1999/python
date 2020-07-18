# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:46:52 2020

@author: user
"""
import math

inp = input().split()
inp = [int(i) for i in inp]

if len(inp)%2 == 0:
    j = 0
    for i in inp:
        j = j + i
    print(math.ceil(j/2))
else:
   j = 0
   for i in inp:
        j = j + i
   print(math.ceil(j/3)) 













