# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:29:42 2020

@author: user
"""

import random 

print("Number guessing game") 
 
number = random.randint(1, 9) 
chances = 0
print("Guess a number (between 1 and 9):") 

while chances < 5: 
	guess = int(input()) 
	if guess == number: 
		print("Congratulation YOU WON!!!") 
		break
	elif guess < number: 
		print("Your guess was too low: Guess a number higher than", guess) 	 
	else: 
		print("Your guess was too high: Guess a number lower than", guess) 
	chances += 1
	if not chances < 5: 
	  print("YOU LOSE!!! The number is", number)
      
      
      
