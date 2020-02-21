# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:13:02 2020

@author: user
"""

import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

#list of prime numbers
    
#is_prime(n) Will return True
# 2,3,5,7,11,13,17,19,23
    
#is_prime(n) Will return False
# 1,4,6,8,9,10,12,14,15,16,18

is_prime(2) SUCCESS
is_prime(3) SUCCESS
is_prime(8) Fail
is_prime(10) SUCCESS
is_prime(13) SUCCESS
is_prime(15) Fail
is_prime(23) SUCCESS
is_prime(18) SUCCESS
