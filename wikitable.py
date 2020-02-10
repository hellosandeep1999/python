# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:26:58 2020

@author: user
"""

from bs4 import BeautifulSoup
import requests
from collections import OrderedDict
import pandas as pd


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

source = requests.get(wiki).text

soup = BeautifulSoup(source,"lxml")


table = soup.find('table',class_="wikitable")

A = []
B = []
C = []
D = []
E = []
F = []

for row in table.findAll('tr'):
    states = row.findAll('th')
    cells = row.findAll('td')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

df = pd.DataFrame(col_data)
df.to_csv("Desktop/New folder/former.csv")






















    