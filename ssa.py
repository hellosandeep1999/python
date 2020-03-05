# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:03:59 2020

@author: user
"""

import pandas as pd
file = open("baby_data.csv",'a')

files = []
for i in range(1880,2018):
    f = open("baby_names/"+"yob"+str(i)+".txt",'r')
    file.write(f.read())
    f = open("baby_names/"+"yob"+str(i)+".txt",'r')
    data = f.readlines()
    new_year = len(data)*[i]
    files.extend(new_year)
    f.close()

file.close()
df = pd.read_csv("baby_data.csv",names = ["name","age","count"])
df["Year"] = files


