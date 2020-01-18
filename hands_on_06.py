# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:45:13 2020

@author: user
"""

#Hands_on


# Take your street address and make it a list variable myaddress
# where each token is an element.
inp = input("Enter a string: ")
a = inp.split()
print(a)


# What would be the code to set the sum of the numerical portions of
# your address list to a variable called address sum?
inp = input("Enter a string: ")
a = inp.split()
sum = 0
for i in a:
    if i.isnumeric():
        sum = sum+int(i)
print(sum)
        
        


# What would be the code to change one of the string elements of the
# list to another string (e.g., if your address had "West" in it, how would
# you change that string to "North")?        
inp = input("Enter a string: ")
a = inp.split()   
if "west" in a:
    b = a.index("west")
    a[b]="North"
    print(a)
else:
    print(a)
    


# Change the street portion of myaddress to have the street first 
# and the building number at the end. 
inp = input("Enter a string: ")
a = inp.split()
a.remove("india") 
a.remove("101")
a.append("101")
a.insert(0,"india")
print(a)





 
























