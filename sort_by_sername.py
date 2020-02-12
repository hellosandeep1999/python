# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:08:06 2020

@author: user
"""

#Sort by sername


n = int(input("How many person: "))
a = []
for i in range(n):
    f = input("Enter first name: ")
    l = input("Enter last name: ")
    d = {}
    d["f"] = f
    d["l"] = l
    a.append(d)
    
def f1(e):
    return e['l']

a.sort(key=f1)

for i in a:
    print(i['f'],i['l'])
    