# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:18:54 2020

@author: user
"""

from random import randrange
a = [[randrange(2) for i in range(10)] for j in range(10)]
for i in a:
    for j in i:
        print(j,"", end="")
    print()
x,y = input("Enter cordinates: ").split(",")
if a[int(x)][int(y)] == 1:
    print("Success")
else:
    print("loss")
