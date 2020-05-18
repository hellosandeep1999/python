# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:56:27 2020

@author: user
"""






"""
Code Challenge 2
icccricket_db.py


Scrap the data from the URL below and store in mySQL database
https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""



import mysql.connector

conn = mysql.connector.connect(user='forsk_root',password='cooler2112',host='db4free.net',database='forsk_test')

c = conn.cursor()



#Web scrapping from icc cricket site
from selenium import webdriver
import pandas as pd
from collections import OrderedDict

website = "https://www.icc-cricket.com/rankings/mens/team-rankings/test"

browser = webdriver.Chrome("E:/New folder/chromedriver.exe")

browser.get(website)
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



c.execute("""CREATE TABLE table4(
        pos TEXT,
        team TEXT,
        weighted TEXT,
        points TEXT,
        rating TEXT
        )"""
        )

#c.execute("drop table employees")
conn.commit()

sql = "INSERT INTO table4 (pos,team,weighted,points,rating) VALUES (%s, %s, %s, %s, %s)"
val = []
for i in range(len(A)):
    sets = (A[i],B[i],C[i],D[i],E[i]) 
    val.append(sets)

c.executemany(sql, val)

conn.commit()

print(c.rowcount, "was inserted.")
