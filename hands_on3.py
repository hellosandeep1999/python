# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:17:28 2020

@author: user
"""

#Hand On - 1

# Take donut count from the user and print a string of the 
# form 'Number of donuts: <count>'
# where <count> is the donut count entered by the user. 
# However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Number of donuts: 5
# Number of donuts: many

donut = int(input("Enter count of donuts: "))
a = "Many"
b = donut
if donut >= 10:
    print("Number of donuts: ",a)
else:
    print("Nuber of donuts: ",b)
    
    

#Hand On - 2

# Take input string from the user, 
# print a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
    
inp = input("Enter a string: ")
a = len(inp)
if a < 2:
    print("Empty string")
else:
    b = inp[:2]
    c = inp[-2:]
    print(b+c)
    
    
    
#Hand On - 3

# Take the age as input from the user and print whether he is a infant, Child , 
# Adult,  Senior Citizen
# 0 - 1 is Infant
# > 1 and < than 18 is Child 
# > 18 and < 60 is Adult
# > 60 is Senior Citizen 

while(True):
    age = int(input("Enter your age: "))
    if age<0:
        print("Age should be positive ")
    elif age == 0:
        print("Infant")
    elif age == 1:
        print("Infant")
    elif age > 1 and age < 18:
        print("Child")
    elif age > 18 and age < 60:
        print("Adult")
    else:
        print("Senior Citizen")
    
    
#Hand On - 4

# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Print the resulting string.
        
        
inp = input("Enter a string: ")
b = len(inp)
c = "ing"
if b < 3:
    print(inp)
else:
    if inp[-3::] == c:
        print(inp+"ly")
    else:
        print(inp+c)



#Hand On - 5
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
        
inp =  input("Enter a string: ")
a = len(inp)
b = int(a/2)
if a % 2 == 0:
    print("the front half is : ",inp[:b])
    print("\nThe back half is : ",inp[b:])
else:
    print("the front half is : ",inp[:b+1])
    print("\nThe back half is : ",inp[b+1:])






#Hand On - 6


# Print all the numbers from 1 to 10 using condition in while loop
    
i = 1
while (True):
    print(i)
    i = i+1
    if i == 11:
        break


#Hand On - 7

# Print all the even numbers from 1 to 10 using condition in while loop


i = 1
while (i<=10):
    if i % 2 == 0:
        print(i)
    i = i+1
    
    
    
    
#Hand On - 8
    
#Print all the even numbers from 1 to 10 using while True loop   

i = 1
while (True):
    if i % 2 == 0:
        print(i)
    i = i+1
    if i == 11:
        break





#Hand On - 8
        
# Print all the odd numbers from 1 to 10 using condition in while loop
        

i = 1
while (i<=10):
    if i % 2 == 0:
        i = i+0
    else:
        print(i)
    i = i+1
     

#Hand On - 8
    
# Print all the odd numbers from 1 to 10 using while True loop

i = 1
while (True):
    if i % 2 == 0:
        i = i+0
    else:
        print(i)
    i = i+1
    if i ==11:
        break



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
