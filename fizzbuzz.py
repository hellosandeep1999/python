# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:30:56 2020

@author: user
"""



# FizzBuzz


 
i = 1
while (i <= 50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i = i+1
        