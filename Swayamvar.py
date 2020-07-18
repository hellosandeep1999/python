# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:17:33 2020

@author: user
"""


N = int(input("Enter a number: "))
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
string2 = list(string2)

if len(string1) == N and len(string2) == N:
    n = N 
    count = 0
    for bride in string1:
        i = 0
        while i < n:
            if bride == string2[0]:
                string2.pop(0)
                n = n - 1
                count += 1
                break
            else:
                string2.insert(n,string2[0])
                string2.pop(0)
                i += 1
            if i == n-1:
                break
                break
        
    print(N-count)
                
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    