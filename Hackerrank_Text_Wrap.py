# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:26:48 2020

@author: user
"""

import textwrap


def wrap(string, max_width):
        l = []
        j = 0
        k = max_width
        for i in range(int(len(string)/max_width)+1):
              l.append(string[j:k])
              j += max_width
              k += max_width
        return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)