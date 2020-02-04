# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:45:59 2020

@author: user
"""


"""
Name: 
    Letter Distribution       
Filename:
    letter_dist.py 
Problem Statement:
    Ask the user to enter some text. 
    Display the distribution of letters from within the text. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Use dictionaries to solve 
    import string and use string.ascii_lowercase 
Algorithm:
    Convert all letters to lowercase
    Ignore characters that aren't lowercase letters
    Create a dictionary in which the keys are letters and the values are the counts. 
Boiler Plate Code:
    Not Available 
Sample Input:
    This is a test.  Show me the distribution, already!
Sample Output:
    t: 6 15%
    h: 3 7%
    i: 5 12%
    s: 5 12%
    a: 3 7%
    e: 4 10%
    o: 2 5%
    w: 1 2%
    m: 1 2%
    d: 2 5%
    r: 2 5%
    b: 1 2%
    u: 1 2%
    n: 1 2%
    l: 1 2%
    y: 1 2%
""" 


inp = input("Enter a string: ")
a = inp.lower()
b = []
for i in a:
    if ord(i) >= 97 and ord(i) <= 122:
        b.append(i)
c = "".join(b)
k = len(c)
d = {}
for i in c:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
e = []   
for i in d.values():
     a = int((i*100)/k)
     e.append(a)
index = 0    
for k,v in d.items():
     print(k,v,e[index],"%")
     index += 1     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
for x,y in d.items():
     print(x,y)    
















     
def f1(x,y):
    return x,y

f = list(map(f1,d,e))


for x,y in d.item:
    

    
    
from collections import Counter  

a = Counter(c)
