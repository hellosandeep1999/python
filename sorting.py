# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:06:04 2020

@author: user
"""
"""
Name: 
    Sorting         
Filename:
    sorting.py
Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
Sample Input:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
Sample Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
""" 






n = int(input("Enter number of person:"))
b = []
for i in range(n):
    a = input("Enter name, age , height: ").split(',')
    g = [a[0],int(a[1]),int(a[2])]
    c = tuple(g)
    b.append(c)
b.sort()
print(b)

