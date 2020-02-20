# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:48:00 2020

@author: user
"""
from selenium import webdriver
import pandas as pd
from collections import OrderedDict

wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/test"

browser = webdriver.Chrome("E:/New folder/chromedriver.exe")

browser.get(wiki)



table1=browser.find_element_by_class_name('table')

A=[]
B=[]
C=[]
D=[]
E=[]


for row in table1.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())



col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

df = pd.DataFrame(col_data) 
df.to_csv("Desktop/New folder/former5.csv")




















