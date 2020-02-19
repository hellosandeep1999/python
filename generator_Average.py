# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:00:40 2020

@author: user
"""
"""
Code Challenge
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]



"""

import time

def f1():
    l = [7, 13, 17, 231, 12, 8, 3]
    yield sum(l)/(len(l))


def f2():
    l = [7, 13, 17, 231, 12, 8, 3]
    return sum(l)/(len(l))

t1 = time.clock()
print(next(f1()))
t2 = time.clock()


t3 = time.clock()
print(f2())
t4 = time.clock()
print(t2-t1)
print(t4-t3)
