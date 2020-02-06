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


a = input("Enter a list: ")                  #words = ['aba', 'xyz', 'aa', 'x', 'bbb']
b = a.split() 
c = []
for i in b:
    if len(i) >= 2 and i[0] == i[-1]:
        c.append(i)
print(len(c))





# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.


inp = input("Enter a list: ")        # e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
a = inp.split() 
b = []
c = []
for i in a:
    if i[0] == "x":
        c.append(i)
    else:
        b.append(i)
c.extend(b)
print(c)





# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.


inp = input("Enter alist of numbers: ")
nums = inp.split()
for i in nums:
    x = nums.count(i)
    for j in range(1,x):
        nums.remove(i)
nums.sort()
print(nums)       

        


'''Hands On'''

# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

inp1 = input("Enter first list: ")
list1 = inp1.split()
inp2 = input("Enter second list: ")
list2 = inp2.split()
list2.extend(list1)
list2.sort()
print(list2)



'''Hands On'''

# Make a function days_in_month to return the number of days in a specific month of a year

thisdict = {
  "january": 31,
  "fabruary": 29,
  "march": 31,
   "april": 30,
  "may": 31,
  "june": 30,
   "july": 31,
  "august": 31,
  "september": 30,
  "october": 31,
  "november": 30,
  "december": 31,
}

def days_in_month(inp):
    return thisdict.get(inp)

inp = input("Enter a month: ")
days_in_month(inp)




'''Hands On'''


#Create a dictionary myaddress using your address. 
#Choose relevant keys(they will probably be strings), 
#and separate your address into street address,
#city, state, and postal code portions, all of which are strings (for your ZIP
#Code, don’t enter it in as a number).

myaddress = {'street':'3225 West Foster Avenue',
             'city':'Chicago', 
             'state':'IL',
             'zip':'60625'
             }

for i in myaddress.values(): #different 1
    print(i)


for x,y in myaddress.items():      #different 2
    print(x,"=",y)


print(myaddress['street'])        #different 3





































































    








































































    

    
    

    



































 
























