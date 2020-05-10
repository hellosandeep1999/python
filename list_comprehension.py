# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:33:04 2020

@author: user
"""

"""
Code Challenge 4

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by 3
"""




results = [max([divisor for divisor in range(1,10) if number % divisor == 0]) \
           for number in range(1,1001) if number % 3 == 0]
print(results)
