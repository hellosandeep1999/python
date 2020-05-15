# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:46:30 2020

@author: user
"""

"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:(odd_number.py)

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""




from functools import reduce

def productOfOdds(listt1):
    return reduce(lambda x,y: x*y , list(filter(lambda a: a%2==1, list1)))

list1= map(int, input('Enter the numbers: ').split(","))  
print('Product of Odd numbers:',productOfOdds(list1))
