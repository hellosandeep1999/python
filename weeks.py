# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:28:38 2020

@author: user
"""
"""
Name: 
    weeks       
Filename:
    weeks.py 
Problem Statement:
    Write a program that adds missing days to existing tuple of days 
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
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
Sample Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
""" 





inp = input("Enter day: ").split()
a = []
if inp[0] == 'Monday' :
    a.append('Monday')
else:
   a.append('Monday')
if inp[1] == 'Tuesday' :
    a.append('Tuesday')
else:
   a.append('Tuesday')
if inp[0] == 'Wedneday' :
    a.append('Wedneday')
else:
   a.append('Wedneday')
if inp[0] == 'Thrusday' :
    a.append('Thrusday')
else:
   a.append('Thrusday')
if inp[0] == 'Friday' :
    a.append('Friday')
else:
   a.append('Friday')
if inp[0] == 'Saturday' :
    a.append('Saturday')
else:
   a.append('Saturday')
if inp[0] == 'Sunday' :
    a.append('Sunday')
else:
   a.append('Sunday')
   
b = tuple(a)
print(b)



















    
    

    
    
    