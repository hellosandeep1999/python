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


# remove all 3 from the list

inp = input("Enter the number: ")
some_list = inp.split()
a = some_list.count("3")
for i in range(0,a):
    some_list.remove("3")
print(some_list)




# Take the list of the parts of your street address
# Write a loop that goes through that list and prints out each item in that list
list1 = ["kk","hostel","india","gate"]
list2 = []
for i in list1:
    list2.append(i)
print(list2)




#Write a loop that checks each temperature in T and sets the corresponding
#Tflags element to True if the temperature is above the freezing point of water.
T = [273.4, 265.5, 277.7, 285.5]
Tflags = []
for i in T:
    Tflags.append(i>273)
print(Tflags)
       






# Clean the Messy salaries into integers for Data Processing

salaries = ['$876,001', '$543,903', '$2453,896'] 
b = []
for i in salaries:
    b.append(i.replace("$","").replace(",",""))
print(b)








# Create a list of Fibonnaci numbers up to the 50th term.
# The program will then ask the user for which position in the sequence
inp = int(input("Enter the position: "))
i = 0
j = 1
count = 0
while count < inp:
    print(i,", ",end="")
    sum = i + j
    i = j
    j = sum
    count +=1





'''Hands On'''
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.


a = input("Enter a list: ")
b = a.split() 
c = []
for i in b:
    if len(i) >= 2 and i[0] == i[-1]:
        c.append(i)
print(len(c))





    








































































    

    
    

    



































 
























