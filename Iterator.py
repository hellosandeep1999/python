# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:27:46 2020

@author: user
"""
# Using Itertools


class Topten:
    def __init__(self):
        self.nums = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.nums <= 10:
            val = self.nums
            self.nums += 1
            
            return val
        else:
            raise StopIteration

values = Topten()

for i in values:
     print(i)   