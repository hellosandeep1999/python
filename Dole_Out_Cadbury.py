# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:56:26 2020

@author: user
"""

m = input()
n = input()
p = input()
q = input()
ll = int
bb = int
count = 0

def cadbury(m, n, p, q):
    leng = [m, n]
    brd = [p, q]
    for l in leng:
        for b in brd:
            call(l, b)

def call(l, b):
    #print l,b
    global count
    area = l * b
    if l > b:
        bb = l
        rem = bb - b
        #print rem
        rem_part1 = rem
        #print rem_part1
        rem_part2 = b
        #print rem_part2
        l = rem_part1
        #print l
        b = rem_part2
        #print b
        if l != b:
            if (l==1) or (b==1):
                count += 1
                count += (l*b)
                #print count
                return
            else:
                count += 1
                #print count
                call(l, b)
        if l==b:
            count+=2
            #print count
            return
    elif b > l:
        ll = b
        #print ll
        rem = ll - l
        #print rem
        rem_part1 = rem
        #print rem_part1
        rem_part2 = l
        #print rem_part2
        l = rem_part1
        #print l
        b = rem_part2
        #print b
        if l != b:
            if (l==1) or (b==1):
                count += 1
                count += (l*b)
                #print count
                return
            else:
                count += 1
                #print count
                call(l, b)
        if l==b:
            count+=2
            #print count
            return
cadbury(int(m), int(n), int(p), int(q))

print(count)   