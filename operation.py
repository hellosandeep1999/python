# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:15:12 2020

@author: user
"""
"""
Name: 
    Operations Function         
Filename:
    operation.py
Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)
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
    5,2,6,2,3
Sample Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]
""" 


import functools

inp = input("Enter a list: ").split()
def f_sum(inp):
    a = [int(i) for i in inp]
    return (functools.reduce((lambda x,y : x+y),a))
def f_mul(inp):
    a = [int(i) for i in inp]
    return (functools.reduce((lambda x,y : x*y),a))
def f_max(inp):
    a = [int(i) for i in inp]
    return max(a)
def f_min(inp):
    a = [int(i) for i in inp]
    return min(a)
def f_sort(inp):
    a = [int(i) for i in inp]
    a.sort()
    return a
def f_duplicate(inp):
    a = [int(i) for i in inp]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b



print("Sum = ",f_sum(inp),"\nMultiply = ",f_mul(inp),"\nLargest = ",f_max(inp),"\nSmallest = ",f_min(inp),"\nSorted = ",f_sort(inp),"\nWithout Duplicate = ",f_duplicate(inp))







    
    















