# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:51:14 2020

@author: user
"""

#infinite input


list = []
while (True):
    inp = input("Enter a number: ")
    list.append(inp)
    if not inp:
        break
del list[-1]
print(list)
sum = 0
for i in list:
    if i.isnumeric():
        sum = sum + int(i)
print("Sum fo the list",sum)
print("Average of list",sum/(len(list)))
list.sort()
print("Largest number in list",list[-1])   
print("Smallest number in list",list[0])




    
    


        
        
        
        