# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:54:14 2020

@author: user
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing in human readable format
"""

import requests
import time

city = input("Enter a city name: ")

url1 = "http://api.openweathermap.org/data/2.5/weather"

payload = {"q":city,"appid":"3d55c06df10298fb235d9b245f4a78ae"}

response = requests.get(url1,params=payload)

jsondata = response.json()

print("Current temprature of " +city,":", int(jsondata["main"]["temp"] - 273.15))
print("Latitude of "+city,":",jsondata["coord"]["lat"])
print("Longitude of "+city,":",jsondata["coord"]["lon"])
print("Weather condition of  "+city,":",jsondata["weather"][0]["description"],)
print("Wind Speed "+city,":",jsondata["wind"]["speed"])
print("Sunrise time of "+city,":",time.ctime(jsondata["sys"]["sunrise"]))
print("Sunset time of "+city,":",time.ctime(jsondata["sys"]["sunset"]))