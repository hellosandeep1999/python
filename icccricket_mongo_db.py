# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:55:47 2020

@author: user
"""

from pymongo import MongoClient

import pandas as pd

cluster = MongoClient("mongodb+srv://sandeepjain:sj9252011759@cluster0-rhimv.mongodb.net/test?retryWrites=true&w=majority")

db = cluster['test']
collection = db['test']

def add_employee(idd, first, last, pay):
    unique_employee = collection.find_one({"_id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        collection.insert_one(
                {
                "_id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = collection.find()
    for i in user:
        print (i)

add_employee(1,'Sylvester', 'Fernandes', 50000)
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()


df = pd.read_csv("Desktop/New folder/former4.csv")

records = df.to_dict(orient = 'records')

result = collection.insert_many(records)



#collection.drop()














post = {"_id":'02',"name":"sandeep","score":"60"}

collection.insert_one(post)

collection.drop()