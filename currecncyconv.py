# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:46:53 2020

@author: user
"""

import requests

dollar = int(input("Enter dollar($): "))

url1 = "http://data.fixer.io/api/latest?access_key=dcb056cfb1d63e8deaf2d042c1942b92&format=1"


response = requests.get(url1)

jsondata = response.json()

print('Current Price of 1 Usd Dollar($) %.2f' % (jsondata['rates']['INR']/jsondata['rates']['USD']),"Rs")
conversion = (jsondata['rates']['INR']/jsondata['rates']['USD'])*dollar
print("Indian rupees in",dollar,"Dollar: %.2f" % conversion,"Rs")