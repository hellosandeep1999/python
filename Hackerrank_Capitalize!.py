# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:29:31 2020

@author: user
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    list = s.split(" ")
    list2 = []
    for i in list:
        if i != '':
            name = i[0].upper() + i[1:]
            list2.append(name)
        else:
            list2.append('')
    return " ".join(list2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()