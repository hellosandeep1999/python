# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:48:46 2020

@author: user
"""

class py_solution:
    def Roman_to_int(self,s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
                int_val += rom_val[s[i]] - 2*rom_val[s[i-1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

obj = py_solution()
print(obj.Roman_to_int('XLVIII'))