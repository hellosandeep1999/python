# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:51:38 2020

@author: user
"""

# Generate floating random numbers from interval [3,7]


import random
print("float random number is", random.uniform(3,7))


# Simulate the dice, random number between 1 and 6
from random import randint
print(randint(1,6))


# Random element from a list of rock, paper and scissors

import random
list = ["rock","paper","scissors"]
print(random.choice(list))