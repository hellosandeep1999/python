# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:39:40 2020

@author: user
"""

import pymongo

client = pymongo.MongoClient("mongodb://sandeepjain:sj9252011759@cluster0-shard-00-00-rhimv.mongodb.net:27017,cluster0-shard-00-01-rhimv.mongodb.net:27017,cluster0-shard-00-02-rhimv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client['icc_cricket']
collection = db['icc_cricket']

def add_cricket_coll(pos, team, weighted, points,rating):
    unique_cricket_coll = collection.find_one({"team":team})
    if unique_cricket_coll:
        return "cricket data already exists"
    else:
        collection.insert_one(
                {
                "pos" : pos,
                "team" : team,
                "weighted" : weighted,
                "points" : points,
                "rating" : rating
                })
        return "cricket data added successfully"
    


#Web scrapping from icc cricket site
from selenium import webdriver


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
    

for i in range(len(A)):
    add_cricket_coll(A[i],B[i],C[i],D[i],E[i])
    
    
def fetch_all_cricket_coll():
    user = collection.find()
    for i in user:
        print (i)
        
fetch_all_cricket_coll()
















   
