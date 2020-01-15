# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:25:31 2020

@author: user
"""

#Adult body mass index calculater




Weight = int(input("Enter your weight in Kg: "))
height = float(input("Enter your height in meter: "))

BMI = Weight/(height*height)   #Formula of BMI

print("Your BMI is: ",BMI) 