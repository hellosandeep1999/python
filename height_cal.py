# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:55:12 2020

@author: user
"""

"""
    Lets assume your height is 5 Foot and 11 inches 
    Convert 5 Foot into meters and 
    Convert 11 inch into meters and 
    print your total height in meters and 
    print your total heigjt in centimetres also
    
"""

height_feet = int(input("Enter your height in feet"))
height_inch = int(input("Enter last some inches"))
meter = height_feet*0.3048 + height_inch*0.0254 
centimeter = meter*100
print("your height in meter",meter,"\nyour height in centimeter",centimeter)