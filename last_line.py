# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:39:36 2020

@author: user
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""





file_name = input("Enter a file name which you want to open: ")

with open(file_name, "r") as file:
    for last_line in file:
        pass

print(last_line)

