# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:39:16 2020

@author: user
"""


"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

import csv

list1 = []
dict = {}
with open('zoo.csv') as file1:
    file = file1.readlines()
    for row in file[1:]:
        line = row.strip().split(',')
        if line[0] not in list1:
            list1.append(line[0])
        if line[0] not in dict:
            dict[line[0]] = int(line[2])
        else:
            dict[line[0]] += int(line[2])
            
            
print("animals: ",list1)
total_water = 0
for name,water in dict.items():
    print(name,"-->",water)
    total_water += water
print("Total water",total_water)

