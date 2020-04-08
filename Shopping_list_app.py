# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:22:20 2020

@author: user
"""


shopping_list = []

print("What should we buy from the shops")
print("Enter 'DONE' to stop adding items")

while True:
    #asks for new items
    new_item = input("> ")

    #be able to quit the app
    if new_item == 'DONE':
        break

    #add items to shopping list
    shopping_list.append(new_item)

print("Here's your list:")

for item in shopping_list:
    print(item)

