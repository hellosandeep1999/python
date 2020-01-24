# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:05:38 2020

@author: user
"""

A1,A2,A3,E1,E2 = int(input("Marks Assignment1: ")),int(input("Marks Assignment2: ")),int(input("Marks Assignment3: ")),int(input("Marks Exam1: ")),int(input("Marks Exam2: "))
weighted_score = ( A1 + A2 + A3 ) * 0.1 + (E1 + E2 ) * 0.35
print("Your Weighted score is: ",weighted_score)