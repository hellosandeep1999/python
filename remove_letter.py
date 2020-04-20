# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:10:06 2020

@author: user
"""


#remove a specific letter from list:


list1 = ["priya","ram","yiot"]
for name in list1:
    if "y" in name:
        print(name.replace('y',''))
    else:
        print(name)