# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:39:16 2020

@author: user
"""


"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""


import csv
water_elephant=0
water_tiger=0
water_lion=0
water_zebra=0
water_kangaroo=0
counter=0
counter1=0
counter2=0
counter3=0
counter4=0
with open("zoo.csv") as zoo:
        zoo_reader = csv.DictReader(zoo)

        for row in zoo_reader:
               
              #print(row['animal'])
             if row['animal']=='elephant':
                        if(counter==0):
                             print("Elephant :")
                             print(row['animal'],row['uniq_id'],row['water_need'] )
                             water_elephant+=int(row['water_need'])
                             counter+=1

             elif row['animal']=='tiger':

                        if(counter1==0):
                             print("Tiger :")
                             print(row['animal'],row['uniq_id'],row['water_need'] )
                             water_tiger+=int(row['water_need'])
                             counter1+=1

             elif row['animal']=='lion':
                         if(counter2==0):
                             print("Lion :")
                             print(row['animal'],row['uniq_id'],row['water_need'] )
                             water_lion+=int(row['water_need'])
                             counter2+=1

             elif row['animal']=='zebra':
                         if(counter3==0):
                            print("Zebra :")
                            print(row['animal'],row['uniq_id'],row['water_need'] )
                            water_zebra+=int(row['water_need'])
                            counter3+=1

             elif row['animal']=='kangaroo':
                         if(counter4==0):
                            print("Kangaroo :")
                            print(row['animal'],row['uniq_id'],row['water_need'] )
                            water_kangaroo+=int(row['water_need'])
                            counter4+=1

        print("Water needed for elephant :",water_elephant)
        print("Water needed for tiger :",water_tiger)
        print("Water needed for lion :",water_lion)
        print("Water needed for zebra :",water_zebra)
        print("Water needed for kangaroo :",water_kangaroo)
        total=0
        total=water_elephant + water_lion + water_tiger + water_zebra + water_kangaroo
        print("Total water consume by animal",total)

