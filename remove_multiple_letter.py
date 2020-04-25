# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:47:57 2020

@author: user
"""

#Multiple letter Remove from a list.

list1 = ["priya","ram","yiot","rajesh","devesh"]
for name in list1:
    if "y" in name:
        a = name.replace("y",'')
        if "r" in a:
            print(a.replace("r",''))
        else:
            print(a)
    elif "r" in name:
        a = name.replace("r",'')
        if "y" in a:
            print(a.replace("y",''))
        else:
            print(a)
    else:
        print(name)