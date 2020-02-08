# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:50:18 2020

@author: user
"""



"""
Code Challenge

Download the image from the URL and store in a file

logo by other name in file

https://imgs.xkcd.com/comics/python.png

"""







import requests

url1 = 'https://imgs.xkcd.com/comics/python.png'

r = requests.get(url1)

with open('Desktop/New folder/other_name.png','wb') as f:
    
    f.write(r.content)

