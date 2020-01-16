# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:28:18 2020

@author: user
"""

#Replacing of characters
#RESTART



inp = input("Enter a string: ")
a = inp[0]
b = inp[1:]
c = b.replace("R","$")
print(a+c)
