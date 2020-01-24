# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:41:31 2020

@author: user
"""

#ride cost Calculator


travel_car,mlg_car = float(input("Enter total kilometer: ")),float(input("Enter mileage(in leter): "))
ptrl_car = travel_car/mlg_car
ridecost_car = ptrl_car*80
print("The cost of driving per day to office: ",ridecost_car)

