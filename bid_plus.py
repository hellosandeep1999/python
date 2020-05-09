# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:09:01 2020

@author: user
"""

from selenium import webdriver
import pandas as pd
from collections import OrderedDict
from time import sleep

bid_plus = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("E:/New folder/chromedriver.exe")

browser.get(bid_plus)
sleep(5)

content=browser.find_element_by_class_name('pagi_content')
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
first = content.find_element_by_class_name('border block ')
first1 = first.find_element_by_class_name('block_header')
cells = row.find_elements_by_tag_name('td')
if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())



col_name = ["BID NO","items(s)","Quantity Required","Department Name And Address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

df = pd.DataFrame(col_data) 
df.to_csv("Desktop/New folder/former4.csv")


















for row in content.find_element_by_class_name('border block '):
    cells = row.find_elements_by_tag_name('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())