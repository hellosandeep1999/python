# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:06:19 2020

@author: user
"""

import pandas as pd


f = open("zoo.txt","r")

animal = []
uniq_id = []
water_need = []
dict = {}


lines = f.readlines()
last_line = len(lines)-1
for index,line in enumerate(lines):
    if index == 0:
        continue
    elif index == last_line:
            line = line.split(",")
            print(line)
            animal.append(line[0])
            uniq_id.append(line[1])
            water_need.append(line[2][:])
    else:
            print(line)    
            line = line.split(",")
            animal.append(line[0])
            uniq_id.append(line[1])
            water_need.append(line[2][:-1])

dict["animal"] = animal
dict["uniq_id"] = uniq_id
dict["water_need"] = water_need

df = pd.DataFrame(dict)

df.to_csv("zoo_new.csv")

f.close()
    
