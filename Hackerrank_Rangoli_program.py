# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:13:36 2020

@author: user
"""

"""
=================================================

Rangoli program

===============================================

"""




def print_rangoli(size):
    for i in range(size):
        print("-"*(size+(size-2)-(i*2)),end="")
        for j in range(i+1):
            if i+1 == 1:
                print(chr(96+(size-j)),end="")
            else:
                print(chr(96+(size-j))+'-',end="")
        for j in range(i):
            if j == (i-1):
                print(chr(96+((size+1)-(i-j))),end="")
            else:
                print(chr(96+((size+1)-(i-j)))+'-',end="")
        print("-"*(size+(size-2)-(i*2)),end="")
        print()
    for i in range(size-1):
        print("-"*(2+(i*2)),end="")
        for j in range(size-(i+1)):
            if i+1 == (size-1):
                print(chr(96+(size-j)),end="")
            else:
                print(chr(96+(size-j))+'-',end="") 
        for j in range(size-(i+2)):
            if j == (size-(i+3)):
                print(chr(96+size-((size-(i+3)-j))),end="")
            else:
                print(chr(96+size-((size-(i+3)-j)))+'-',end="")
        print("-"*(2+(i*2)),end="")
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)