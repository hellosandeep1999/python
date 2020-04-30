# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:19:53 2020

@author: user
"""

"""


Q.3. Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 monster_com-job_sample.csv
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
 
 
"""



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('monster_com-job_sample.csv')

dataset.isnull().any(axis=0)

#Remove location from Organization column?

for i in dataset["location"]:
    if "Organization" in i:
        dataset["location"] = dataset["location"].fillna(0)








