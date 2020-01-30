# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:43:46 2020

@author: user
"""

"""
Name: 
    Pangram         
Filename:
    pangram.py
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
Data:
    Not required
Extension:
    Not Available  
Hint: 
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    The five boxing wizards jumps. 
    Sphinx of black quartz, judge my vow.
    The jay, pig, fox, zebra and my wolves quack!
    Pack my box with five dozen liquor jugs.
Sample Output:
    NOT PANGRAM 
    PANGRAM
    PANGRAM
    PANGRAM
"""  



inp = input("Enter a string: ")
a = inp.lower()
b = 'abcdefghigklmnopqrstuvwxyz'
count = 0
for i in b:
    if i in inp:
        count += 1
if count == 26:
    print("PANGRAM")
else:
    print("NOT PANGRAM")
    