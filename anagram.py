# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:21:06 2020

@author: user
"""

inp1 = input("Enter first string: ")
inp2 = input("Enter second string: ")
a = len(inp1)
b = len(inp2)
count = 0
if a == b:
    for i in inp1:
        if i in inp2:
           count += 1
if count == a and count == b:
    print("Anagram")
else:
    print("Not Anagram")
    
 
    