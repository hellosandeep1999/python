# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:49:35 2020

@author: user
"""



"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""





file_name = input("Enter a file name which you want to open: ")
command = input("Write the wc command: ")
file = open(file_name,'r')
Lines = file.readlines()

count = 0
num_word = 0
characters = 0
dict = {}
for line in Lines:
    characters += len(line)
    line = line.split()
    count += 1
    for word in line:
        num_word += 1
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1

if  command.lower() == 'wc':       
        print("Number of characters (including whitespace): ",characters)  
        print("Number of words (separated by whitespace): ",num_word)      
        print("Number of lines: ",count)
        print("Number of unique words: ",len(dict.keys()))
else:
    print("command is wrong")