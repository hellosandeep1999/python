# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:04:30 2020

@author: user
"""

from re import sub

def f1(string):
    c = []
    for i in string:
            if ord(i) == 32:
                c.append(i)
            elif ord(i) >= 65 and ord(i) <= 90:
                if (sub("[aeiouAEIOU]","",i)) == '':
                    c.append(i)
                else:
                   b = i + 'o' + i
                   c.append(b)
            elif ord(i) >= 97 and ord(i) <= 122:
                if (sub("[aeiouAEIOU]","",i)) == '':
                    c.append(i)
                else:
                   b = i + 'o' + i
                   c.append(b)
    return c

          
            

inp = input("Enter a string: ")
b = f1(inp)
d = "".join(b)
print(d)









        