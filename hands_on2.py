# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:07:25 2020

@author: user
"""

# Write a program to count the number of words in a sentence.
string = "Forsk technologies coding school is best the learning platform for computer science engineering"
print(len(string.split()))



a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

max = a if a>b>c else b if b>c else c
print(max)





n = int(input("Enter number of n: "))
for i in range(n):
    for j in range(n-i):
        print(j+1,end="")
    print()
    

n = int(input("Enter number of n: "))
for i in range(n):
    print(" "*(n-i-1),(str(i+1)+' ')*(i+1))
    
    
    
    
    
    
for i in range(4):#0,1,2,3
    print("* "*(i+1))
    











n = int(input("Enter number of n: "))
for i in range(n):
    for j in range(n-i):
        print(j+1,"",end="")
    print()


chr(65)