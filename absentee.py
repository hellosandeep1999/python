# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:33:40 2020

@author: user
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""



f= open("absentee.txt","w+")

i = 0
while i < 25:
    name = input("Enter a name: ")
    if not name:
        break
    f.write("%s\n" %name)
    
f.close()
f= open("absentee.txt","r")   

f1 = f.readlines()
for x in f1:
    print(x)

