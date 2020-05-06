
"""
Name:
    Infinite input
Filename: 
    infinite.py    
Problem Statement:
    Write a program that asks the user, again and again, to enter a number.
    When the user enters an empty string, then stop asking for additional inputs.
    Along the way, as the user is entering numbers, 
    I want you to store those numbers in a list. 
    I also want you to keep track of the minimum and maximum values that you've seen so far.
    When the user has finished entering numbers, your program should print out:
         The sum of these numbers
         The average (mean) of these numbers
         The largest and smallest numbers you received from the user 
"""





#infinite input


list = []
while (True):
    inp = input("Enter a number: ")
    if not inp:
        break
    list.append(int(inp))

print(list)
sum = 0
for i in list:
    sum = sum + int(i)
print("Sum fo the list",sum)
print("Average of list",sum/(len(list)))
list.sort()
print("Largest number in list",list[-1])   
print("Smallest number in list",list[0])
