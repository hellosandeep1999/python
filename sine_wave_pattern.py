# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:43:46 2020

@author: user
"""

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        x = 0
        for k in range(j):
            x = x+n
        if j%2 == 0:
            print(x+i+1,end=" ")
        else:
            print(x+n-i,end=" ")
    print()
    
    