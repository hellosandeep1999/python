# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:34:34 2020

@author: user
"""

#2 Dimensional Random List    


from random import randrange

a= [ [randrange(256) for i in range(10)] for j in range(10) ]
for i in a:
    for c in i:
        print(c,"" , end="")
    print()

