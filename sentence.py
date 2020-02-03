# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:19:34 2020

@author: user
"""
"""
Name: 
    Sentence       
Filename:
    Sentence.py
Problem Statement:
    You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code. 
    The sentence you want to encode is the lazy dog jumped over the quick brown 
    fox and the output should be ’vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz’ 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Create a dictionary mapping each letter to its number in the alphabet
    Create a dictionary mapping each number to its letter in the alphabet
    Go through each letter in the sentence and find the corresponding number, add 2 and then find the new corresponding letter
    Make sure to take care of the edge cases so that if you get the letter z, it maps to b… ect
    Print the encoded string  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available
Sample Output:
    Not Available
""" 




inp = input("Enter a string: ")
list = []
for i in inp:
    if ord(i) >= 97 and ord(i) <= 120:
        a = ord(i) + 2
        b = chr(a)
        list.append(b)
    elif i == 'y':
        list.append('a')
    elif i == 'z':
        list.append('b')
    elif i == ' ':
        list.append(' ')
c = "".join(list)
print(c)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    