# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:22:16 2020

@author: user
"""
Name: 
    List of File Names       
Filename:
    list_dict.py 
Problem Statement:
    Assume you’re given the following list of files:
    ist_of_files = ['data0001.txt', 'data0002.txt','data0003.txt']

    Create a dictionary filenum where the keys are the filenames and the
    value is the file number (i.e., data0001.txt has a file number of 1) 
    as an integer.

    Make your code fill the dictionary automatically, assuming that you 
    have a list list of files. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    To convert a string to an integer, use the int function on the string, 
    and the list and array sub-range slicing syntax also works on strings 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
    
    
    
  
    
    
    
""" 

s = ['data0001.txt', 'data0002.txt','data0003.txt']
b = []
for i in s:
    for j in i:
        if j.isdigit():
            if int(j) > 0:
                c = int(j)
                b.append(c)             
res = {} 
for key in s: 
    for value in b: 
        res[key] = value 
        b.remove(value) 
        break  
    


"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

