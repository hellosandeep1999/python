# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:02:16 2020

@author: user
"""

from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

browser = webdriver.Chrome("E:/New folder/chromedriver.exe")

browser.get(wiki)

right_table=browser.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

df = pd.DataFrame(col_data) 
df.to_csv("Desktop/New folder/former.csv")



