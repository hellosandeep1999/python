# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:50:20 2020

@author: user
"""


import requests

    
rt = int(input('Enter route number:'))

stp = int(input('Enter Stop number: '))


url1 = 'http://ctabustracker.com/bustime/map/getStopPredictions.jsp'

payload = {'route':rt,'stop':stp}

r = requests.get(url1,params = payload)

with open('Desktop/New folder/helo.json','w') as f:
    
    f.write('r.content')



items = response.json()
