# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:31:18 2020

@author: user
"""

 Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    
x,y = input("Enter an input: ").split()
a = int(x)
b = int(y)
c = int((b-3)/2)
e = int((b-7)/2)
d = int(a/2)
if a%2 != 0 and b == a*3:
    for i in range(d):
        print('-'*(c-(3*i))+'.|.'*(2*i+1)+'-'*(c-(3*i)))
    print('-'*e+"WELCOME"+'-'*e)
    for i in range(d):
        print('-'*(3+(3*i))+'.|.'*(2*d-(2*i)-1)+'-'*(3+(3*i)))
        
 



       
 
        
        
        
        
        
        
        