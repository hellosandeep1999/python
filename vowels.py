# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:40:08 2020

@author: user
"""
"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of states  
Hint: 
    Use nested for loops and while
Data:
    Not required
Extension:
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""



from re import sub

inp = input("Enter a string: ")

def f1(string):
    return (sub("[aeiouAEIOU]","",string))


print(f1(inp).split())
















