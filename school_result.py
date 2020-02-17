# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:26:08 2020

@author: user
"""

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS



url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"

browser = webdriver.Chrome("E:/New folder/chromedriver.exe")


browser.get(url)
sleep(5)

school_code = browser.find_element_by_name("treg")


school_code.send_keys(2000)
sleep(3)

get_school_result = browser.find_element_by_name('bsubmit')

#or
#get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')

get_school_result.click()



