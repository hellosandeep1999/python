# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:37:39 2020

@author: user
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""




dict = {}
f = open("romeo.txt",'r')
lines = f.readlines()
for line in lines:
    line = line.split()
    for word in line:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1

print(dict)
