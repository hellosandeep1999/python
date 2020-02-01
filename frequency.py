# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:33:41 2020

@author: user
"""
"""
Name: 
    Character Frequency       
Filename:
    frequency.py 
Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    www.google.com
Sample Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
""" 




list = 'www.facebook.com'


dict = {}

for item in list:
    if item not in dict:
        dict[item] = 1
    else:
        dict[item] = dict[item] + 1

print(dict)














