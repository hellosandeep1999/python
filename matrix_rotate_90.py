# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:11:14 2020

@author: user
"""

n = int(input("Enter rows of square matrix: "))
arr_list = []
for i in range(n):
    l = list(map(int,input().split()))
    arr_list.append(l)

print("the 90 Degree rotate matrix: ")
for i in range(n):
    for j in range(n):
        print(arr_list[j][n-(i+1)] ,end=" ")
    print()