# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:23:25 2020

@author: user
"""


"""
Name: 
    Unlucky 13         
Filename:
    unlucky.py
Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user
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
    13, 1, 2, 13, 2, 1, 13 
Sample Output:
    3 
"""   
 



list = [13, 1, 2, 13, 2, 1, 13]
a = []

for index,i in enumerate(list):
    if list[index] == 13:
        a.append(index)
        if index < len(list)-1:
             a.append(index+1)


suml = 0
for index,i in enumerate(list):
    if index not in a:
        suml = suml + list[index]
        
print(suml)

    
        
        
