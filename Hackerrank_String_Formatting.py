# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:31:17 2020

@author: user
"""

def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1,number+1):
         a = oct(i)
         b = hex(i)
         c = bin(i)
         print(str(i).rjust(w),str(a[2:]).rjust(w),str(b[2:].upper()).rjust(w),str(c[2:]).rjust(w))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    