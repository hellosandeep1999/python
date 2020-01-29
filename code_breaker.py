# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:59:12 2020

@author: user
"""
"""
Name: 
    CodeBreaker         
Filename:
    code_breaker.py
Problem Statement:
    The computer generates a 4 digit code
    The user types in a 4 digit code. Their guess.
    The computer tells them how many digits they guessed correctly
Data:
    Not required
Extension:
    the computer tells them how many digits are guessed correctly 
    in the correct place and how many digits have
    been guessed correctly but in the wrong place.
    The user gets 12 guesses to either 
    WIN – guess the right code. 
    Or
    LOSE – run out of guesses.  
Hint: 
    Not Available  
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""   



import itertools 
from random import randint
a = [randint(0,9) for i in range(4)]
b = input("Enter a 4 digit list: ")
c = b.split()


count = 0
for (i,index) in zip(c,a):
    if int(i) == index:
        count += 1

if count == 4:
    print("WIN")
elif count == 0:
    print("LOSS")
else:
    print(""count)




