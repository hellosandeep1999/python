# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:13:38 2020

@author: user
"""

class book(object):
    def __init__(self,authorfirst,authorlast,title,price,year,publisher):
        self.authorfirst = authorfirst
        self.authorlast = authorlast
        self.title = title
        self.price = price
        self.year = year
        self.publisher = publisher
    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst + ', ' + self.title + ', ' + self.price + ':  ' + self.publisher + ', ' + self.year + '.'
    def make_authoryear(self):
        self.authoryear = self.authorlast + '('+ self.year +' )'

# Create a few instances of Book and Article classes:
b1 = book('ravi','teja',"Valentine's day",'532','2020',"kumar ji")  

#If you type print beauty.write_bib_entry() at the interpreter, what will happen?        
print(b1.make_authoryear())


#How would you change the publication year for the beauty book to"2010"?
b1.year="2010"
print(b1.write_bib_entry()) # It will year 2010 along with remaining attributes

