# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:18:33 2020

@author: user
"""
"""
Name: 
    Pallindromic Integer
Filename: 
    pallindromic.py
Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)        
Data:
    Not required
Extension:
    Not Available  
Hint: 
    A palindromic number or numeral palindrome is a number that remains the same
    when its digits are reversed. 
    Like 16461, for example, it is "symmetrical"  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    12 9 61 5 14 
Sample Output:
    Flase   
"""





inp = input("Enter a list of number").split()
b = inp[::-1]
a = []

for i in b:
    a.append(i[::-1])
    
if a == inp:
    print("Pallindromic Integer")
else:
    print("not pallindromic")
    
    