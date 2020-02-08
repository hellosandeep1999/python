# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:04:13 2020

@author: user
"""

'''
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your working diretory with the same
name as the image name.

Do not hardcode the name of the image

'''


import requests 
image_url = "http://forsk.in/images/features_images/device_icon.png"
  
 
r = requests.get(image_url)
 
with open("Desktop/New folder/device_icon.png",'wb') as f: 
  
    f.write(r.content) 