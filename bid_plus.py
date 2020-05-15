# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:09:01 2020

@author: user
"""


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""


      
from selenium import webdriver
import pandas as pd
bid_no = []
address=[]
item=[]
item_required=[]
start_date=[]
end_date=[]

#driver = webdriver.Chrome('E:/New folder/chromedriver.exe')
driver = webdriver.Chrome('E:/New folder/chromedriver.exe')
driver.get("https://bidplus.gem.gov.in/bidlists")
c=0
while(c<=20): 
    c+=1
    bid_table = driver.find_element_by_id('pagi_content')
    bid_table = bid_table.find_elements_by_class_name('border')
    for i in bid_table:
            bid_no.append(i.find_elements_by_tag_name('a')[0].text.strip())            
            item.append(i.find_elements_by_tag_name('span')[0].text.strip())
            item_required.append(i.find_elements_by_tag_name('span')[1].text.strip())
            start_date.append(i.find_elements_by_tag_name('span')[2].text.strip())
            end_date.append(i.find_elements_by_tag_name('span')[3].text.strip())
            address.append(i.find_element_by_class_name('add-height').text.strip())
    driver.find_element_by_xpath("//a[@rel='next']").click()
driver.quit() 
dff = pd.DataFrame(zip(bid_no,item,item_required,address,start_date,end_date),columns=['BID NO','Item','Item Reuired','Address','Start Date','End Date'])
dff.to_csv("former5.csv")




