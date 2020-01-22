# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:13:56 2020

@author: user
"""

#  Ponderal Index Calculator  

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = weight/(height*height)
ponderal_index = BMI/height
print("your poderal index is",ponderal_index,BMI)