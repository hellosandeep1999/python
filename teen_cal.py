# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:08:28 2020

@author: user
"""


"""
Name: 
    Teen Calculator       
Filename:
    teen_cal.py
Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    from ast import literal_eval
    dict1 = literal_eval("{'a': 2, 'b' : 15, 'c' : 13}") 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    {'a' : 2, 'b' : 15, 'c' : 13}
Sample Output:
    Sum = 17
""" 


import ast

def fix_teen(v):
    if(v == 15 or v == 16):
        return v
    elif v >=13 and v <=19:
        return 0
    else:
        return v
dict1 = ast.literal_eval("{'a': 45, 'b' : 15, 'c' : 17}") 
s = 0
for k in dict1.values():
    v = fix_teen(k)
    s += v
print(s)
























