# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:07:25 2020

@author: user
"""

# Write a program to count the number of words in a sentence.
string = "Forsk technologies coding school is best the learning platform for computer science engineering"
print(len(string.split()))




# Develop a program that will display a sentence backwards after entered.
string = input("Enter a string")
print(string[::-1])




# Given a string s, print the string again
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: try using replace function
inp = input("Enter a string: ")
k = inp[0]
l = inp[1:]
print(k+l)
m = l.replace(k,"*")
print(k+m)




# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

inp = input("Enter a string: ")
a = inp.find("not")
b = inp.find("bad")
c = b+3
d = inp.replace(inp[a:c:1],"good")
print(d)



# Clean the Messy salary into integers for Data Processing
sal = '$876,001' 
a = sal[0:4]
b = sal[4:]
c = a.replace(sal[0],'')
d = b.replace(sal[4],'')
print(c+d)
 





















        
