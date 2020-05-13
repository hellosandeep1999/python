# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:45:02 2020

@author: user
"""



"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""









"""
Write a program which returns a list of list with 
    [order number, total amount of order].
"""



orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

import functools
list2 = []
for i in orders:
    order_number = i[0]
    list1 = list(map(lambda x : x[1]*x[2] , i[1:]))
    amount = functools.reduce(lambda a,b : a+b,list1)
    list2.append([order_number,round(amount,2)])
print(list2)  
    




