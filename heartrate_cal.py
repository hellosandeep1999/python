# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:37:59 2020

@author: user
"""
#Target Heart Rate Calculator  
age = int(input("Enter your age: "))
Max_rate = 220 - age               #formula of max rate
low_end = 199*0.7
high_end = 199*0.85
print("Your max Rate: ",Max_rate,"\nLower End",low_end,"\nHigh End",high_end)
