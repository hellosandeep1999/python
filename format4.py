# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:45:26 2020

@author: user
"""

#Formated string
inp = input("Enter a string")
a = inp.split()
b = list(reversed(a))
c = " ".join(b)
print(c)












sentence = "The quick brown fox jumped over the lazy dog."
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print (sentence_rev)