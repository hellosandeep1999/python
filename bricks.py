# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:43:53 2020

@author: user
"""


"""
Name: 
    Bricks         
Filename:
    bricks.py
Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
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
    2, 2, 11
Sample Output:
    True
""" 



def f1(x,y,z):
    a = x*1 + y*5
    if a == z:
        return True
    else:
        return False

a = []

inp = input("Enter a string: ").split()
for i in inp:
    a.append(int(i))
    


f1(a[0],a[1],a[2])

