# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:23:05 2020

@author: user
"""
orders = [ ["34587", "Learning Python", "Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python", "Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python", "Paul Barry", 3,132.95],
           ["88112", "Einführung in Python3", "Bernd Klein",3, 24.99]]


min_order = 100

invoice_totals1 = list(map(lambda x: (x[0],x[4]*x[3]),orders))
print(invoice_totals1)

print("The product should be increased by 10 INR if the value of the order is smaller than 100.00 INR.")
invoice_totals2 = list(map(lambda x: (x[0],x[4]*x[3]) if x[4]*x[3] >= min_order else (x[0], (x[4]*x[3]) + 10),orders))
			                                                         
print(invoice_totals2)